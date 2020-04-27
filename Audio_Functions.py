from scipy.io import wavfile
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.fftpack import fft, fftfreq
from Settings_Functions import *

#   this function records an audio file to of the specified length
#   and saves it to the specified path

#   WARNING WAITS FOR SPECIFIED TIME
def recordAudio(path = getFullPath('reference.wav'), recTime = .5):
    sampleRate = 44100  # Sample rate
    try:
        myrecording = sd.rec(int(recTime * sampleRate), samplerate=sampleRate, channels=1)
        sd.wait()       # Wait until recording is finished
    except sd.PortAudioError:
        print(f"No audio device connected. myrecording set to empty")
        myrecording = []
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
    print(f'Recording Reference')

    #   record new reference wav file
    settings = loadSettings('audioSettings.json')
    path = getFullPath(settings['refPath'])
    recordAudio(path, 1)

    #   get new reference fundamental
    newRef = getFund(path)
    print(f"New Fundamental: {newRef}")

    # save the fundamental to file
    changeSetting(settings, 'reference', newRef)

    # set setup flag in main settings to true
    changeSetting(loadSettings('mainSettings.json'), 'Audio_Setup', True)


#   plays the reference audio file using a bash script
def playReference():
    print(f'Playing Reference...')
    filePath = getFullPath('reference.wav')
    if(os.path.exists(filePath)):
        runBashScript('playSound.sh', filePath)
    else:
        print("No file to play, you fool! Record one first!")

#   deletes all audio files in the project directory
def clearAudio():
    print("wiping ")
    wipeAll('.wav')

