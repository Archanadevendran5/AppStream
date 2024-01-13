import os

pathToWS = os.getcwd().split("src")[0]
jsonDir = "/DataRequirements/JSONFiles/"
logDir = "/DataRequirements/LogFiles/"

JsonDirectory = pathToWS + jsonDir
JsonDirectory_Path = os.path.expanduser(JsonDirectory)
if not os.path.exists(JsonDirectory_Path):
    os.makedirs(JsonDirectory_Path)

LogDirectory = pathToWS + logDir
LogDirectory_Path = os.path.expanduser(LogDirectory)
if not os.path.exists(LogDirectory_Path):
    os.makedirs(LogDirectory_Path)
