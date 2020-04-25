from OCR_Controller import menu_OCR
import Audio_Controller
from Settings_Functions import *

def Settings():
    print(f"\nSETTINGS ->\tThis function has access to settings json files")

    # launch settings screen

    print("In Controller from Settings, going back to Main Menu")

def OCR():
    print("You entered OCR!")
    menu_OCR()
    print("In Controller from OCR, going back to Main Menu")

def Audio():
    print("You entered Audio!")
    Audio_Controller.start()
    print("In Controller from Audio, going back to Main Menu")


#   exits the program -> erase main settings file
def EXIT():

    '''print(f"removing mainSettings File")
    path = getFullPath('mainSettings.json')
    os.remove(path)
    print(f"\tmainSettings.json deleted")
    '''

    print(f"Removing All Settings and Loop-Generated Files (for testing)\n")
    wipeAll('.json')

    #   delete all old audio files -> take this out eventually
    wipeAll('.wav')

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


# main
if __name__ == "__main__":

    #   make sure settings system is working, exit if there are issues
    init_Main()

    menuString = "\nMAIN MENU\n1)\tSettings\n2)\tOCR\n3)\tAudio\n4)\tEXIT\n"
    options = {1: Settings, 2: OCR, 3: Audio, 4: EXIT}
    print("In the master File")

    userInput = -1


    while userInput != 4:
        print(menuString)

        userInput = int(input("Enter 1-4: "))

        options[userInput]()
        print("\nBack in Main Menu")

