#   contains lists of button functions to be added to menu buttons
from CoordList import coordList
from Image_Functions import *


#   functions for the buttons on the main menu

def take_Src():
    print('taking source image')
    takeSource()


def empty():
    print("this function is empty")


mainMenuFns = {
    "takeSrc": take_Src,
    "empty": empty
}


#   functions needed for buttons on the imgTest screen

def show_Img():
    print("showing image")
    myList = coordList()
    img = 'source.jpg'
    showImage(myList, img)


def add_Crop():
    print("adding crop")
    myList = coordList()
    img = 'source.jpg'
    addCrop(myList, img)


def crop_Source():
    print("cropping soruce")
    myList = coordList()
    img = 'source.jpg'
    cropSource(myList, img)


imgTestFns = {
    'showImg': show_Img,
    'addCrop': add_Crop,
    'cropSrc': crop_Source

}
