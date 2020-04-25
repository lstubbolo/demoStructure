import time
from PiResponses import respInter
from Audio_Functions import *


#   record new sample
def getData(samplePath):
    print("\tRecording Sample")
    recordAudio(samplePath)


#   called during loop
#   get fundamental from sample, compare with reference, return result
def processData(samplePath, reference):
    print("\tgetting Fundamental from sample")
    newFund = getFund(samplePath)

    print("\t comparing with reference fundamental")
    detected = compareFreqs(newFund, reference)

    print(f"\t done - reference detected : {detected}")
    print()
    return detected


#   called during loop - > updates local values
#   any function calls that need to happen depending loop data should happen here
def updateLocal(mySet, detected):
    print(f"\tSetting Audio Setting 'detected' to {detected}")
    mySet = changeSetting(mySet, 'detected', detected)
    print("Updating Screen, Local Triggers")
    print()
    return mySet


#   called during loop -> Push results to Firebase
def updateServer(detected):
    fb_message = {'audioDetected': detected}
    print(f"\tUpdating Firebase with {fb_message}")
    time.sleep(.25)
    print()


#   checks that main settings[Audio_Setup] flag is true
def init():
    success = True
    mainSet = loadSettings('mainSettings.json')
    success = mainSet['Audio_Setup']

    return success


#   checks internal end conditions for the sampling loop
def getEndConditions(mySet):
    print("Checking Internal Ending Conditions...")

    #   checks for loop end due to loopMode Settings
    if check_LoopMode(mySet):
        return True

    #   Checks for loop end from to external input
    if respInter("Checking", "OCR") == "Stop":
        return True

    #   unique end conditions go here

    return False


#   sub controller function -> runs everything needed for OCR runs
def start():
    print("Audio Start function")
    #   checks that device setup was completed
    setupSuccess = init()

    #   loads audioSettings.json
    settings = loadSettings('audioSettings.json')

    if not setupSuccess:
        print("setup failed, returning to OCR menu")
    else:
        print("setup successful, Starting OCR Run")

    endFlag = False

    while not endFlag:
        print("\n\nNEW Loop!")

        endFlag = getEndConditions(settings)

        loopOnce(settings)

    #   loop has terminated
    print("\n\nSample Loop Completed!")


#   single sampling run ->
#   mySet = Audio settings, loaded in start
def loopOnce(mySet):
    print("In sample Run")
    getData(mySet['smplPath'])
    detected = processData(mySet['smplPath'], mySet['reference'])

    mySet = updateLocal(mySet, detected)
    updateServer(detected)
    print("done run")
