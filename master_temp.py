#   This is the main controller file. This is a temporary stand-in for what will be in the GUI

import OCR_Controller
import Audio_Controller
from Settings_Functions import *
from Audio_Functions import playReference, recordAudio, clearAudio
from FireBase_Functions import setupFirebase

def Settings():
    print(f"\nSETTINGS ->\tThis function has access to settings json files")

    # launch settings screen

    print("In Controller from Settings, going back to Main Menu")

def OCR():
    print("\nYou entered OCR!")
    OCR_Controller.start()
    print("In Controller from OCR, going back to Main Menu")

def Audio():
    print("\nYou entered Audio!")
    Audio_Controller.start()
    print("In Controller from Audio, going back to Main Menu")


#   exits the program -> erase main settings file
def EXIT():

    '''print(f"removing mainSettings File")
    path = getFullPath('mainSettings.json')
    os.remove(path)
    print(f"\tmainSettings.json deleted")
    '''



    print("Done Exit Process\nHave A Nice Day!")
    exit('\nExiting Program...')

#   init function for the entire project
#   This function will automatically terminate with error
#   if the settings file read/write system isn't working
def init_Main():
    #   load main settings file
    mainSet = loadSettings('mainSettings.json')

    #   overwrite error flag in mainSettings
    print("Writing Main Settings Error Flag to False")
    changeSetting(mainSet, 'error', 'False')
    mainSet = loadSettings('mainSettings.json')

    print(f"\tSettings Load Error: {mainSet['error']}")
    print()

    #   check that flag was overwritten successfully
    if not mainSet['error'] == 'False':
        print("Failed to Load / Generate Main Settings")
        exit("Main Settings Failure")

    #   Check if firebase should be connected then do it
    if mainSet['FB_Enabled'] == 'True':
        setupFirebase()


# main
if __name__ == "__main__":

    #   make sure settings system is working, exit if there are issues
    init_Main()

    menuString = "\nMAIN MENU\n1)\tSettings\n2)\tOCR\n3)\tAudio\n4)\tEXIT\n5)\t(re)Rec Reference\n6)\tPlay Reference\n7)\tClear Recordings\n"
    options = {1: Settings, 2: OCR, 3: Audio, 4: EXIT, 5: recordAudio, 6: playReference, 7: clearAudio}

    userInput = -1


    while userInput != 4:
        print(menuString)

        print("changing to test github")
        userInput = int(input(f"Enter 1-{len(options)}: "))
        options[userInput]()

        print("\nBack in Main Menu")
