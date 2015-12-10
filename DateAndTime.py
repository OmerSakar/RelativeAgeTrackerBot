import time


def getDateAndTime():
    result = time.time()
    return result


def checkIfHourPassed(old):
    return time.time() - old > 3600
