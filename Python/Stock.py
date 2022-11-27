import time
import json
import requests
import copy
import os

KEY = os.environ["FKEY"]

def getOldJson():
    with open("./Stocks.json", "r") as f:
        return json.load(f)

def getNewJson(oldjson):
    newjson = copy.copy(oldjson)
    for i in oldjson:
        URL = f"https://api.twelvedata.com/price?symbol={i}&apikey={KEY}"

        price = requests.get(URL).json()["price"]

        newjson[i] = float(price)
    return newjson

def updateJson(newjson):
    with open("./Stocks.json", "w") as f:
        json.dump(newjson, f)

def main():
    oldjson = getOldJson()
    newjson = getNewJson(oldjson)
    print(f"Old: {oldjson}")
    print(f"New: {newjson}")
    for i in oldjson:
        if newjson[i] > oldjson[i]:
            print(f"Buy {i}")
        else:
            print(f"Don't Buy {i}")
    updateJson(newjson)
    pass

if __name__ == "__main__":
    main()
