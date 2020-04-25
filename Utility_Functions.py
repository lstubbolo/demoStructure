import subprocess
import os
from datetime import datetime, timedelta
import json

#   runs the bash script located at the specified local path
def runBashScript(path):
    directory = os.path.dirname(__file__)
    filePath = os.path.join(directory, path)
    subprocess.call(filePath)


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

