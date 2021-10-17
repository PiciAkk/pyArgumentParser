import sys
import json

argumentsDict = {}
arguments = sys.argv[1:]
for i in range(0, len(arguments), 2):
    argumentsDict.update({arguments[i]: arguments[i+1]})

print(json.dumps(argumentsDict))
