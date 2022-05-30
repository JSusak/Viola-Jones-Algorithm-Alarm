import json
from datetime import datetime


def replaceLogs(detect):
    with open("jsonLogs/detectionlogs.json") as logFile:
        data = json.load(logFile)
        for item in data["lastDetectedLog"]:
            item["DetectionPositions"] = item["DetectionPositions"].replace(
                str(item["DetectionPositions"]), str(detect)
            )
            item["LastDetectedTime"] = item["LastDetectedTime"].replace(
                str(item["LastDetectedTime"]),
                str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
            )
            item["timesDetected"] = item["timesDetected"] + 1

    with open("jsonLogs/detectionlogs.json", "w") as f:
        json.dump(data, f)


def readLogs():
    msg = ""
    with open("jsonLogs/detectionlogs.json", "r") as logFile:
        data = json.load(logFile)
        for item in data["lastDetectedLog"]:
            msg += (
                "• Last detected position was at: "
                + str(item["DetectionPositions"])
                + ".\n"
            )
            msg += (
                "• The last date at which a face was detected was at: "
                + str(item["LastDetectedTime"])
                + ".\n"
            )
            msg += (
                "• A face has been detected "
                + str(item["timesDetected"])
                + " times. Not very sneaky :)\n"
            )

    return msg

def getLastDetectedID():
    id = "";
    with open("jsonLogs/detectionlogs.json", "r") as logFile:
            data = json.load(logFile)
            for item in data["lastDetectedLog"]:
                id += (str(item["timesDetected"]))
                
        
    return int(id)
