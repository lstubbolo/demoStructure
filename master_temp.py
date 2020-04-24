from OCR_Controller import menu_OCR

from SettingsFunctions import *


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

    print("In Controller from Audio, going back to Main Menu")


def EXIT():
    print("Have a nice day!")

    exit(0)


# main
if __name__ == "__main__":

    loadSettings()

    #   launch GUI
    #launch gui

    menuString = "\nMAIN MENU\n1)\tSettings\n2)\tOCR\n3)\tAudio\n4)\tEXIT\n"
    options = {1: Settings, 2: OCR, 3: Audio, 4: EXIT}
    print("In the master File")

    userInput = -1


    while userInput != 4:
        print(menuString)

        userInput = int(input("Enter 1-4: "))

        print(f"You Entered: {userInput}\n")
        options[userInput]()

        print("PROCESS DONE, HIT STOP SYMBOL")
        while(True):
            print("killme")
