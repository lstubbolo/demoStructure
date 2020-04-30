from PiResponses import respond, check_LoopMode
from Audio_Functions import *
from FireBase_Functions import postFirebase

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
    #if(detected):
    if(True):
        print("Updating Local Stuff")
        print(f"\tSetting Audio Setting 'detected' to {detected}")
        mySet = changeSetting(mySet, 'detected', detected)

        print("\t**NOT IMPLEMENTED-> UPDATE SCREEN")
        print()
    else:
        print(f"\tLocal Update Skipped Because detected: {detected}")

    return mySet


#   called during loop -> Push results to Firebase
def updateServer(fb_url, detected):
    print(f"Updating Server")
    # if(detected):
    if (True):
        fb_message = {'audioDetected': detected}

        postFirebase(fb_url, fb_message)

        print("\tFirebase Update Complete")
        print()

    else:
        print(f"\tFirebase Update Skipped Because detected: {detected}")

#   checks internal end conditions for the sampling loop
def getEndConditions(mySet):
    print("Checking OCR End Conditions")

    #   checks for loop end due to loopMode mySet (in Utility Functions)
    if check_LoopMode(mySet):
        print("\tLoop Ended Due to Internal Trigger")
        print()
        return True

    #   Checks for loop end from to external input
    if respond("check", "audio") == "Stop":
        print("\tLoop Ended Due to External Trigger")
        print()
        return True


    print("\tLoop Continuing")
    return False

#   checks that main mySet[Audio_Setup] flag is true
def init_Audio():
    print("In init_Audio: Checking Audio Initialization")

    mainSet = loadSettings('mainSettings.json')
    flag = mainSet['Audio_Setup']
    print(f"Main Settings Audio Setup Flag: {flag}")

    #   flag must be evaluated as string!
    return flag == "True"


#   sub controller function -> runs everything needed for Audio runs
def start():
    print("Audio Start function")

    #   checks that device setup was completed
    setupSuccess = init_Audio()

    if not setupSuccess:
        print("\tAudio Not Set Up! -> Running recordRef\n")
        recordRef()
        print("\tdone\n")

    print("Loading Audio Settings")
    mySet = loadSettings('audioSettings.json')

    print(f"Setup Complete -> Loop Mode: {mySet['loopMode']}")

    endFlag = False

    while not endFlag:
        print("\n--------Loop Starting--------\n")

        #   run function that checks if loop should
        endFlag = getEndConditions(mySet)

        #   runs exatly one loop
        loopOnce(mySet)

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
    updateServer(mySet['fb_url'], detected)
    print("\n>-------Loop COMPLETE-------<\n")
