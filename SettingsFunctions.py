#   This set of function handles saving / loading settings



#   returns a settings object
def loadSettings():

    #   name of settingsFile
    fileName = "mainSettings.json"

    #   gets the directory of the file
    directory = os.path.dirname(__file__)

    #   set path to json file-> append file name to directory
    filePath = os.path.join(directory, fileName)

    #   check if file doesn't exist, if not, make one at default value
    if not (os.path.exists(filePath)):
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
        mainSettings = {}
        with open(filePath, 'r') as myFile:
            mainSettings = json.loads(myFile.read())

        print("Settings Loaded")

        return mainSettings
