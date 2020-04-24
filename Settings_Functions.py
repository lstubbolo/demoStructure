import os
import json
import subprocess

#   This set of function handles saving / loading settings


#   returns a settings object derived from
def loadSettings(fileName):

    #   name of main
    main_Settings = "mainSettings.json"

    #   gets the directory of the file
    directory = os.path.dirname(__file__)

    #   set path to json file-> append file name to directory
    filePath = os.path.join(directory, fileName)

    #   check if main settings file exists, if not, create it
    if fileName == main_Settings and not (os.path.exists(filePath)):
        print("NO SETTINGS FILE DETECTED")

        print("creating new file with default entry")

        #creating a default settings object in memory
        mainSettings = {
            'fireBaseURL': 'empty',
            'fireBaseInput': 'empty',
            'OCR_Setup': 'False',
            'Audio_Setup': 'False',
            'OCR_Active': 'False',
            'Audio_Active': 'False'
        }

        # use open() to create a file

        with open(filePath, 'w') as myFile:
            myFile.write(json.dumps(mainSettings))

    #   load
    else:
        with open(filePath, 'r') as myFile:
            settingsObj = json.loads(myFile.read())

        print(f"{fileName} settings loaded")

        return settingsObj


#   runs the bash script located at the specified local path
def runBashScript(path):
    directory = os.path.dirname(__file__)
    filePath = os.path.join(directory, path)
    subprocess.call(filePath)



