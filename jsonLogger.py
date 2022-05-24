import json
from datetime import datetime

def replaceLogs(detect):
    with open('jsonLogs/detectionlogs.json') as logFile:
        data = json.load(logFile)
        for item in data['lastDetectedLog']:
            item["DetectionPositions"] = item["DetectionPositions"].replace(str(item["DetectionPositions"]), str(detect))
            item["LastDetectedTime"] = item["LastDetectedTime"].replace(str(item["LastDetectedTime"]), str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            item["timesDetected"] = item["timesDetected"] + 1

    with open('jsonLogs/detectionlogs.json', 'w') as f:
        json.dump(data, f)