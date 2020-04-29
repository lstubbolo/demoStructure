import subprocess
import os
from datetime import datetime, timedelta
import json

#   This is the least secure code I think i have ever written
#   attempts to run the bash script based on the name provided
#   args are optional, but
def runBashScript(scriptName, args = ()):
    directory = os.path.dirname(__file__)
    filePath = os.path.join(directory, scriptName)
    try:
        subprocess.call([filePath, args])
    except PermissionError:
        print(f"'{scriptName}' has not been set to executable!")
        print(f"while in this directory run sudo chmod +x {scriptName}")


#   removes all files in root directory of the specified type(if allowable)
def wipeAll(type):
    allowable = ('.wav', '.json', '.png', '.jpeg')
    #   check if you are allowed to remove this type of file

    if not allowable.__contains__(type):
        print(f"You can't remove '{type}' files")
        exit(f'Stupd MF Tried to delete {type} files')
    else:
        print(f"Removing all files ending with '{type}'")

        directory = os.path.dirname(__file__)
        allFiles = os.listdir(directory)
        allWav = [f for f in allFiles if f.endswith(type)]

        for file in allWav:
            path_to_file = os.path.join(directory, file)
            os.remove(path_to_file)

        print(f"\tAll {type} files Removed")
        print()


#   datetime stuff

#   gets a json string from a datetime object
def getTimeStr(timeObj):
    timeStr = json.dumps(timeObj, default=datetime.__str__)
    return timeStr


#   gets a json formatted time string, returns if current time is greater
def checkTime(input):
    endTime = datetime.strptime(json.loads(input), '%Y-%m-%d %H:%M:%S')
    current = datetime.now().replace(microsecond=0)
    return current > endTime

