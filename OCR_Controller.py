import time
from PiResponses import respond, check_LoopMode
from OCR_Functions import *
from FireBase_Functions import postFirebase

testVar = {'hello', 'world'}

#   get data function -> for OCR this means taking a picture and cropping
def getData(src, cropImgs):
    print("Getting Data for OCR...")
    takeSource(src)
    cropped = cropSource(cropImgs)
    print()


#   process data function -> for OCR this means running OCR scripts
def processData(imgs, PSM, lang):
    print("Processing Data for OCR...")
    crop_text = {}
    for entry in imgs:
        crop_text[entry] = (doOCR(imgs[entry], PSM[entry], lang[entry]))
    print()
    return crop_text

#   called during loop - > updates local values
#   any function calls that need to happen depending loop data should happen here
def updateLocal(mySet, ocr_out):

    print("Updating Local Stuff")

    mySet = changeSetting(mySet, 'cropTxt', ocr_out)

    print("\t**NOT IMPLEMENTED-> UPDATE SCREEN")
    print()

    return mySet

#   called during loop -> Push results to Firebase
def updateServer(fb_url, ocrData):
    print(f"Updating Server")

    fb_message = {'ocrText': ocrData}

    postFirebase(fb_url, fb_message)

    print("\tFirebase Update Complete")
    print()


#   checks internal end conditions for the sampling loop
def getEndConditions(mySet):
    print("Checking Audio End Conditions")

    #   checks for loop end due to loopMode Settings (in Utility Functions)
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
def init_OCR():
    print("In init_OCR: Checking OCR Initialization")

    mainSet = loadSettings('mainSettings.json')
    flag = mainSet['OCR_Setup']
    print(f"Main Settings OCR Setup Flag: {flag}")

    #   flag must be evaluated as string!
    return flag == "True"


#   sub controller function -> runs everything needed for Audio runs
def start():
    print("OCR Start function")

    #   checks that device setup was completed
    setupSuccess = init_OCR()

    if not setupSuccess:
        print("\tOCR Not Set Up! -> Running CropSetup")
        cropSetup()
        print("\tdone\n")

    print("Loading OCR Settings")
    mySet = loadSettings('OCRSettings.json')

    print(f"Setup Complete -> Loop Mode: {mySet['loopMode']}")

    endFlag = False

    global testVar
    testVar['hello'] = 'Bryan'

    runLoop(endFlag, mySet)


def runLoop(endFlag, mySet):
        print("\n--------Loop Starting--------\n")

        print()
        #   run function that checks if loop should
        endFlag = getEndConditions(mySet)

        loopOnce(mySet)


#   single sampling run ->
#   mySet = pcr settings, loaded in start
def loopOnce(mySet):
    print("In Loop Once...")
    #   Take picture, save to file
    #   Crop Pictures, save to file
    getData(mySet['srcImg'], mySet['cropImgs'])

    #   Extract Strings from Crop, save to file
    cropText = processData(mySet['cropImgs'], mySet['cropPSM'], mySet['cropLang'])

    print("Running Updates")
    updateLocal(mySet, cropText)
    updateServer(mySet['fb_url'], cropText)
    print("\n>-------Loop COMPLETE-------<\n")


