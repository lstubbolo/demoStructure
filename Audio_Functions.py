from scipy.io import wavfile
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.fftpack import fft, fftfreq
import os
import json

#   this function records an audio file to of the specified length
#   and saves it to the specified path

#   WARNING WAITS FOR SPECIFIED TIME
def recordAudio(path, recTime):
    sampleRate = 44100  # Sample rate
    myrecording = sd.rec(int(recTime * sampleRate), samplerate=sampleRate, channels=1)
    sd.wait()       # Wait until recording is finished
    write(path, sampleRate, myrecording)  # Save as WAV file


#   returns fundamental frequqnecy of the sound file at the specified path
def getFundamental(path):
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

    min_range = reference*(1 - sensitivy)
    max_range = reference*(1 + sensitivy)

    detected = (sample in range(min_range, max_range))
    return detected


#   setup for Audio - records reference audio, saves fundamental at provided file path
def setupAudio(fundPath):
    #  create reference audio file path
    fileName = "ref.wav"
    directory = os.path.dirname(__file__)
    filePath = os.path.join(directory, fileName)

    #   record ref audio, save fundamental
    recordAudio(filePath, 1)
    refFundamental = getFundamental(filePath)

    #save fundamental to file
    with open(filePath, 'w') as myFile:
        myFile.write(json.dumps({'fundamental' : refFundamental}))


#   gets reference fundamental from file
def get_Reference(fundPath):
    reference = {}
    with open(fundPath, 'r') as myFile:
        reference = json.loads(myFile.read())

    return reference['fundamental']



