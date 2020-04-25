import time
from PiResponses import respInter
from Audio_Functions import*

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
    endNow = check_LoopMode(mySet)

    #   unique end conditions go here

    return endNow
    

#   sub controller function -> runs everything needed for OCR runs
def start():
    print("Audio Start function")
    setupSuccess = init()
    settings = loadSettings('audioSettings.json')

    if (setupSuccess == False):
        print("setup failed, returning to OCR menu")

    else:
        print("setup successful, Starting OCR Run")

    #   dummy flag and counter for ending the run
    endNow = False
    dummyCounter = 0

    #   not so sure about this loop
    while (endNow == False):
        print("\n\nNEW RUN!")

        print("Checking for kill signal")
        response = respInter("Checking", "OCR")
        if response == "Stop":
            endNow = True
        else:
            endNow = dummyCounter > 50

        if (endNow == False):
            dummyCounter += 1
        else:
            print("\tProceeding")

        print(f"\nSampling... {dummyCounter}")
        runOnce(settings)
        print("Done Sampling - waiting")
        

    print("\n\nSample Loop Completed!")


#   single sampling run ->
'''
mySet = Audio settings, loaded in start
'''
def runOnce(mySet):
    print("In sample Run")
    getData(mySet['smplPath'])
    detected = processData(mySet['smplPath'], mySet['reference'])
    
    mySet = updateLocal(mySet, detected)
    updateServer(detected)


