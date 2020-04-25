import subprocess
import os
from datetime import datetime, timedelta
import json

#   runs the bash script located at the specified local path
def runBashScript(path):
    directory = os.path.dirname(__file__)
    filePath = os.path.join(directory, path)
    subprocess.call(filePath)

#   runs the bash script located at the specified local path
def runBashScriptArgs(path, args):
    directory = os.path.dirname(__file__)
    filePath = os.path.join(directory, path)
    subprocess.call([filePath, args])


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


#   checks loop ending conditions common to both kinds of loop
def check_LoopMode(mySet):
    if mySet['loopMode'] == 'infinite':
        return False

    if mySet['loopMode'] == 'single':
        return True

    #   returns true if enough time has passed
    if mySet['loopMode'] == 'duration':
        return checkTime(mySet['loopEnd'])

    else:
        return False

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

