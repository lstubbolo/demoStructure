from scipy.io import wavfile

import sounddevice as sd
#from sounddevice import rec as sd_rec
#from sounddevice import wait as sd_wait

from scipy.io.wavfile import write
from scipy.fftpack import fft, fftfreq
from Settings_Functions import *

#   this function records an audio file to of the specified length
#   and saves it to the specified path

#   WARNING WAITS FOR SPECIFIED TIME
def recordAudio(path, recTime = .5):
    sampleRate = 44100  # Sample rate
    myrecording = sd.rec(int(recTime * sampleRate), samplerate=sampleRate, channels=1)
    sd.wait()       # Wait until recording is finished
    write(path, sampleRate, myrecording)  # Save as WAV file


#   returns fundamental frequency of the sound file at the specified path
def getFund(path):
    #   loads audio file
    samplerate, data = wavfile.read(path)
    samples = data.shape[0]

    fourier = fft(data)
    freqs = fftfreq(samples, 1 / samplerate)

    # Find the x value corresponding to the maximum y value
    max_Freq = freqs[abs(fourier).argmax()]

    return max_Freq


#   compares the two provided frequencies, returns true if sample is close to reference
def compareFreqs(sample, reference):
    sensitivy = .05

    print(f"\tComparing fund. freq of sample: {sample} with reference: {reference}")

    min_range = reference*(1. - sensitivy)
    max_range = reference*(1. + sensitivy)

    #detected = (sample in range(min_range, max_range))
    detected = (sample > min_range) and (sample < max_range)

    return detected


#   records the reference audio sample, saves fundamental, sets mainSettings flag
def recordRef():
    settings = loadSettings('audioSettings.json')
    path = getFullPath(settings['refPath'])
    recordAudio(path, 1)

    # save the fundamental to file
    changeSetting(settings, 'reference', getFund(path))

    # set setup flag in main settings to true
    changeSetting(loadSettings('mainSettings.json'), 'Audio_Setup', True)


