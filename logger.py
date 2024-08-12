import csv
import os

config = {
    "path": "./logs",
    "fieldsname": ["User", "Data", "Time"]
}

# Ensure the directory exists
if not os.path.exists(config['path']):
    os.makedirs(config['path'])

async def addLogfile(user):
    with open(f"{config['path']}/{user.id}.csv", 'w') as logFile:
        processing = csv.DictWriter(logFile, delimiter=";", lineterminator="\r", fieldnames=config['fieldsname'])
        processing.writeheader()
        logFile.close()

async def logMsg(query, user):
    if user is None:
        return  # Early return if user is None
    if not os.path.exists(f"{config['path']}/{user.id}.csv"):
        await addLogfile(user)
    
    data = {"User": user.username, "Data": query.text, "Time": query.date}
    with open(f"{config['path']}/{user.id}.csv", 'a', newline='') as logFile:
        processing = csv.DictWriter(logFile, delimiter=";", lineterminator="\r", fieldnames=config['fieldsname'])
        processing.writerow(data)
        logFile.close()

async def logCall(query, user):
    if user is None:
        return  # Early return if user is None
    if not os.path.exists(f"{config['path']}/{user.id}.csv"):
        await addLogfile(user)
    
    data = {"User": user.username, "Data": query.data, "Time": query.message.date}
    with open(f"{config['path']}/{user.id}.csv", 'a', newline='') as logFile:
        processing = csv.DictWriter(logFile, delimiter=";", lineterminator="\r", fieldnames=config['fieldsname'])
        processing.writerow(data)
        logFile.close()

async def write(query, user):
    try:
        if hasattr(query, 'data'):  # Check if query has 'data' attribute
            await logCall(query, user)
        else:
            await logMsg(query, user)
    except:
        await logMsg(query, user)
