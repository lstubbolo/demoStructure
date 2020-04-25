from DEFAULTS import *
from Utility_Functions import *
#   This set of function handles saving / loading settings


#   returns the absolute path to the local path provided
def getFullPath(fileName):
    #   gets the directory of the file
    directory = os.path.dirname(__file__)

    #   set path to json file-> append file name to directory
    filePath = os.path.join(directory, fileName)

    return filePath


#   changes setting in object, saves it to file, returns the modified version
def changeSetting(obj, key, value):
    obj[key] = value

    #   every settings object has an attribute called self
    #   which is the local path to where it is saved
    path = getFullPath(obj['self'])

    #   save to file
    with open(path, 'w') as myFile:
        myFile.write(json.dumps(obj))

    return obj


#   returns a settings object from a filename
def loadSettings(fileName):

    filePath = getFullPath(fileName)

    #   check if main settings file exists, if not, create it
    if not(os.path.exists(filePath)):
        print(f"No settings file detected for {fileName}")
        print("generating settings file ...")

        genSettings(fileName, filePath)

        print ("done")

    #   load
    else:
        with open(filePath, 'r') as myFile:
            settingsObj = json.loads(myFile.read())

        print(f"{fileName} settings loaded")

        return settingsObj


#   generates settings file automatically from data in DEFAULTS
#   saves file and returns settings dict
def genSettings(name, path):
    settingsObj = LIST_ALL[name]

    #   check if something was loaded
    if(settingsObj):
        #   write object to file
        with open(path, 'w') as myFile:
            myFile.write(json.dumps(settingsObj))

    else:
        print(f"\n\nError -> settings file{name} unable to be generated.")
        print("TERMINATING")
        exit("ERROR")

    return settingsObj


#   sets the end time attribute of the provided settings object
#   based upon the provided offset(hours)
#   returns the modified settings object
def setEndtime(obj, offset):
    endObj = datetime.now().replace(microsecond=0) + timedelta(hours=offset)
    endStr = getTimeStr(endObj)

    return changeSetting(obj, 'loopEnd', endStr)

