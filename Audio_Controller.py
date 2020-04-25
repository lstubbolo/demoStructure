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
    newFund = float(getFund(samplePath))
    reference = float(reference)

    #print("\tcomparing with reference fundamental")
    detected = compareFreqs(newFund, reference)

    print(f"\tDone Comparison -> reference detected: {detected}")
    print()
    return detected


#   called during loop - > updates local values
#   any function calls that need to happen depending loop data should happen here
def updateLocal(mySet, detected):
    #   update local values if audio signal was detected
    if(detected):
        print("Updating Local Variables")
        print(f"\tSetting Audio Setting 'detected' to {detected}")
        mySet = changeSetting(mySet, 'detected', detected)
        print("\tUpdating Screen, Local Triggers")
        print()
    else:
        print(f"\tLocal Update Skipped Because detected: {detected}")

    return mySet


#   called during loop -> Push results to Firebase
def updateServer(detected):
    if(detected):
        fb_message = {'audioDetected': detected}
        print(f"\tUpdating Firebase with {fb_message}")
        print(f"\t***STILL IN DEVELOPMENT***")
        time.sleep(.25)
        print("\tFirebase Update Complete")
        print()

    else:
        print(f"\tFirebase Update Skipped Because detected: {detected}")

#   checks internal end conditions for the sampling loop
def getEndConditions(mySet):
    print("Checking Audio End Conditions")

    #   checks for loop end due to loopMode Settings
    if check_LoopMode(mySet):
        print("\tLoop Ended Due to Internal Trigger")
        print()
        return True

    #   Checks for loop end from to external input
    if respInter("Checking", "OCR") == "Stop":
        print("\tLoop Ended Due to External Trigger")
        print()
        return True

    #   unique end conditions go here

    print("\tLoop Continuing")
    return False

#   checks that main settings[Audio_Setup] flag is true
def init_Audio():
    print("In init_Audio: Checking Audio Initialization")

    mainSet = loadSettings('mainSettings.json')
    flag = mainSet['Audio_Setup']
    print(f"Main Settings Audio Setup Flag: {flag}")

    #   flag must be evaluated as string!
    return flag == "True"


#   sub controller function -> runs everything needed for OCR runs
def start():
    print("Audio Start function")

    #   checks that device setup was completed
    setupSuccess = init_Audio()

    if not setupSuccess:
        print("\tAudio Not Set Up! -> Running recordRef")
        print()
        recordRef()

        print(f"Reference Recorded -> Loading Audio Settings")
        print()

    else:
        print("Audio Has been Set Up -> Loading Audio Settings")
        print()


    settings = loadSettings('audioSettings.json')

    print(f"Setup Complete -> Loop Mode: {settings['loopMode']}")

    endFlag = False

    while not endFlag:
        print("\n--------Loop Starting--------\n")

        #   run function that checks if loop should
        endFlag = getEndConditions(settings)

        loopOnce(settings)

    #   loop has terminated
    print("\n\nSample Loop Completed!")


#   single sampling run ->
#   mySet = Audio settings, loaded in start
def loopOnce(mySet):
    print("In Loop Once...")
    getData(mySet['smplPath'])
    detected = processData(mySet['smplPath'], mySet['reference'])

    print("Running Updates")
    updateLocal(mySet, detected)
    updateServer(detected)
    print("\n>-------Loop COMPLETE-------<\n")
