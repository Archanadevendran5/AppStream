import json
from src.commonutil.Config import *

jsonFile = pathToWS + "/DataRequirements/JSONFiles/AppStreamDetails.json"
jsonFilePath = os.path.expanduser(jsonFile)

with open(jsonFilePath, 'r+') as file:
    credentialImport = json.loads(file.read())

ACCOUNTID = credentialImport['accountID']
USERNAME = credentialImport['username']
PASSWORD = credentialImport['password']
MIDWAYLINK = credentialImport['midwayLink']
IMAGEBUILDERLINK = credentialImport['ImageBuilderLink']
FLEETLINK = credentialImport['FleetsLink']
ITERATION = credentialImport['iteration']
MIDWAYLOGIN = credentialImport['midwayLogin']
MIDWAYDOMAIN = credentialImport['midwayDomain']
MIDWAYFIELD0 = credentialImport['midwayField0']
MIDWAYFIELD1 = credentialImport['midwayField1']
