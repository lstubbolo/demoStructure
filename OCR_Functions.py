#   All OCR-related functions go in here
from Settings_Functions import *

try:
    import picamera
except ModuleNotFoundError:
    print('picamera not found - camera functions will not work')


#   Generates Cropped Images from a Source Image
def cropSource(cropImgs):
    print("Cropping Source Image...")
    print("\t**NOT IMPLEMENTED-> CROP SOURCE IMAGE")
    print("\tcontents of arguments")
    for entry in cropImgs:
        print(f"\t\t{entry}")
    print()


#   Performs OCR on each of the Cropped Images
def doOCR(image, PSM, lang):
    print("Performing OCR")
    print("\t**IMPLEMENTED BUT NOT INTEGRATED -> David's Code")
    print(f"\tpath: {image}, PSM: {PSM}, lang: {lang}")


#   Cropping Setup Function
def cropSetup():
    print("Cropping Setup Function")
    print("\t**IN DEVELOPMENT BY BRYAN")

    print("\tManually Setting OCR Setup Flag to True in Main Settings")
    changeSetting(loadSettings('mainSettings.json'), 'OCR_Setup', True)

