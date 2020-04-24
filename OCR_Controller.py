import time
from PiResponses import respInter


#   get data function -> for OCR this means taking a picture and cropping
def getData():
    print("\tGetting Data (Taking Picture, Cropping)")
    time.sleep(.25)
    print("\tDone Getting Data. Returning to sampleRun")
    print()


#   process data function -> for OCR this means running OCR scripts
def processData():
    print("\tProcessing Data (Running OCR on set of cropped images)")
    time.sleep(.5)
    print("\tDone Processing Data. Returning to sampleRun")
    print()


#   Update Local function -> display most recent results, save to file?
def updateLocal():
    print("\tUpdating GUI, storage with data from this run")
    time.sleep(.25)
    print("\tDone updating local. Returning to sampleRun")
    print()


#   Update Server function -> Push results to Firebase
def updateServer():
    print("\tUpdating Firebase with data from this run")
    print("\tAvoid deadlock here!")
    time.sleep(.25)
    print("\tDone updating Firebase. Returning to sampleRun")
    print()


#   menu -> Called by Controller -> User can either change settings or start run
def menu_OCR():
    print("OCR MENU:-> No Settings implemented yet")

    print("Going Automatically Going to Start")

    start()


#   ensures values are initialed
def setup():
    print("OCR Setup:\tLoading preferences from json")

    #   TODO check mainSettings.OCR_Setup

    print("\n**If No cropping area set run cropping setup")
    time.sleep(.25)

    print("Done OCR Setup ")

    return True


#   sub controller function -> runs everything needed for OCR runs
def start():
    print("OCR Start function")
    print("running setup")
    setupSuccess = setup()

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
        sampleRun()
        print("Done Sampling - waiting")
        time.sleep(1)
        print("Done Waiting - loop over")

    print("\n\nSample Loop Completed!")


#   single sampling run ->
'''
#   Take picture, save to file
#   Crop Pictures, save to file
#   Extract Strings from Crop, save to file
#   Update Local Display
#   UpdateFirebase
'''
def sampleRun():
    print("In sample Run")
    getData()
    processData()
    updateLocal()
    updateServer()


