import time
import json
import requests
import copy

def getOldJson():
    with open("Stocks.json", "r") as f:
        return json.load(f)

def getNewJson(oldjson):
    newjson = copy.copy(oldjson)
    for i in oldjson:
        newjson[i] = oldjson[i] + 1 #Replce with API code
    return newjson

def updateJson(newjson):
    with open("Stocks.json", "w") as f:
        json.dump(newjson, f)

def main():
    oldjson = getOldJson()
    newjson = getNewJson(oldjson)
    print(f"Old: {oldjson}")
    print(f"New: {newjson}")
    for i in oldjson:
        if int(newjson[i]) > int(oldjson[i]):
            print(f"Buy {i}")
        else:
            print(f"Don't Buy {i}")
    updateJson(newjson)
    pass

if __name__ == "__main__":
    main()
