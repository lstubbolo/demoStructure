import os
import cv2

from CoordObj import coordObj

SCREEN_DIMS = {'width': 799, 'height': 479}


#   CRASHES ON MAC DO NOT RUN
#   returns the absolute path to the local path provided
def getFullPath(fileName):
    #   gets the directory of the file
    directory = os.path.dirname(__file__)

    #   set path to json file-> append file name to directory
    filePath = os.path.join(directory, fileName)

    return filePath


#   shows the source image with the bounding areas for cropping
def showImage(cropObjs, imgPath=getFullPath('source.jpg')):
    if not os.path.exists(imgPath):
        print("No Source Image, Fool! Run takeSource!")
        return

    else:
        #   load image from path, create a named window
        image = cv2.imread(imgPath)
        windowName = "Source Image"
        cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)

        #   set window size, move window
        cv2.resizeWindow(windowName, SCREEN_DIMS['width'], SCREEN_DIMS['height'])
        # cv2.moveWindow(windowName, 0, -50)

        #   add mouse listener function
        cv2.setMouseCallback(windowName, closeEvent)

        #   add rectangles to the window
        for obj in cropObjs.myList[1:]:
            cv2.rectangle(image, obj.topL, obj.botR, (0, 255, 0), 3)

        cv2.imshow(windowName, image)
        cv2.waitKey(0)


#   Use this event listener if you want to close after one click only
def closeEvent(event, x, y, flags, param):
    print("\tClosing Image")
    cv2.destroyAllWindows()


#   attempts to display the image at the provided path
def addCrop(cropObjs, imgPath=getFullPath('source.jpg')):
    if not os.path.exists(imgPath):
        print("No Source Image, Fool! Run takeSource!")
        return

    else:
        #   load image from path, create a named window of the correct size

        image = cv2.imread(imgPath)

        windowName = "Source Image"
        cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(windowName, SCREEN_DIMS['width'], SCREEN_DIMS['height'])

        #   parameters to pass to the listener w/ important stuff added in
        param = [image, windowName, cropObjs]

        #   add mouse listener function,
        cv2.setMouseCallback(windowName, clickHandler, param)

        #   add rectangles to the window
        for obj in cropObjs.myList[1:]:
            cv2.rectangle(image, obj.topL, obj.botR, (0, 255, 0), 6)

        cv2.imshow(windowName, image)
        cv2.waitKey(0)


#   click handler for addCrop
#   first and second click append coords to param and draw to image
#   third click saves new coord obj and closes window
def clickHandler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        image = param[0]
        windowName = param[1]

        #   adjust x/y for touchcreen inaccuracy
        #   *always returns slightly down and to the right
        coord = (x - 5, y - 5)

        #   using number of parameters to make decisions
        #   starts with two params, for the first two
        if (len(param) < 5):
            #   add coords to list
            param.append(coord)

            # draw a circle
            cv2.circle(image, coord, 15, (216, 230, 0), 5)
            cv2.imshow(windowName, image)
            cv2.waitKey(1)

            # Draw the rectangle after the second click
            if (len(param) == 5):
                cv2.rectangle(image, param[3], param[4], (0, 255, 0), 6)
                cv2.imshow(windowName, image)
                cv2.waitKey(1)
                param.append(0)

        #   on third click add the object and close the window
        else:
            cropObjs = param[2]
            #   create a new coord Obj and add to list
            name = "crop" + str(cropObjs.getSize())
            cropObjs.addObject(coordObj(name, param[3], param[4]))

            print("closing window ")
            cv2.destroyAllWindows()


#   generates cropped images based on source image and crop objects
#   returns a list of file paths for use with ocr
def cropSource(cropObjs, imgPath=getFullPath('source.jpg')):
    if not os.path.exists(imgPath):
        print("No Source Image, Fool! Run takeSource!")
        return

    else:
        #   load image from path
        image = cv2.imread(imgPath)

        #   iterate through cropped objects, skipping the first(default) object
        for obj in cropObjs.myList[1:]:
            name = obj.name + '.jpg'

            print(name)

            topL = obj.topL
            botR = obj.botR
            print(name, topL, botR)
            print('x:', topL[0], '->', botR[0])
            print('y:', topL[1], '->', botR[1])

            #   crop the image: y: bot-> top,   x: L->R
            crop_img = image[topL[1]:botR[1], topL[0]:botR[0]]
            cv2.imwrite(getFullPath(name), crop_img)
