import time


#   Functions that allow looping functions to check if
#   These responses can originate from Firebse (because the pi is checking)
#   ***??????? or possibly from somewhere else??? Stop writing and code Louis


#   check firebase for recent commands
def checkFirebase():
    print("\tin PiResponses.checkFirebase")
    print("\t\tChecking Firebase for commands")

    #   dummy delay
    time.sleep(.5)

    fbResponse = ("nope", "nope")

    return fbResponse


#   this is the function that interacts with the outside functions
def respInter(action_arg = "nope", obj_arg = "nope", external_Flag = False):
    print("\nin PiResponses.interface")

    #   Action is the thing that has to happen, object is the thing it has to happen to

    #   check if this function was called externally
    #   ->  most calls will be done internally, checking for kill signals from Firebase
    #   ->  external flag comes from user input on the Pi

    #   if this function was called internally to check for firebase commands
    if external_Flag == False:
        (action, obj) = checkFirebase()

    #  Flag should only be true if set by user input
    else:
        (action, obj) = (action_arg, obj_arg)


    #   list comprehension for handling firebase input
    actions = {"nope": noResp, "Stop": stopRun, "Start_Run": startRun, "Run_Once": runOnce}

    #   call the action function with the object to perform the action on as the argument; save status
    status = actions[action](obj)

    print(f"\tResponse was")
    return status


def noResp(obj):
    print(f"\tNo action needed for '{obj}'")

    if obj == "OCR":
        print("OBJ = OCR")

    return "nope"


def stopRun(obj):
    print(f"\nstopping run for {obj}...")
    time.sleep(.5)
    print(f"\tStand-in for handling termination for {obj}")
    return "Stopped"


def startRun(obj):
    print(f"\nstarting run for {obj}")
    time.sleep(.5)
    print(f"\tStand-in for handling Starting for {obj}")
    return "Stopped"


def runOnce(obj):
    print(f"\nrunning once for {obj}")
    time.sleep(.5)
    print(f"\tStand-in for handling Starting for {obj}")
    return "Ran_Once"

