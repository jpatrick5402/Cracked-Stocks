import datetime
import time
import json
import requests
import copy
import os


def getOldJson():
    with open("./Stocks.json", "r") as f:
        return json.load(f)

def getNewJson(oldjson, KEY):
    newjson = copy.copy(oldjson)
    for i in oldjson:
        URL = f"https://api.twelvedata.com/price?symbol={i}&apikey={KEY}"

        price = requests.get(URL).json()["price"]

        newjson[i] = float(price)
    return newjson

def updateJson(newjson):
    with open("./Stocks.json", "w") as f:
        json.dump(newjson, f)

def Calculate(oldjson,newjson):
    pass

def main():

    while(True):
        try:
            KEY = os.environ["FKEY"]
        except:
            KEY = input("Enter your API KEY: ")
        oldjson = getOldJson()
        newjson = getNewJson(oldjson, KEY)
        print(datetime.datetime.now())
        print(f"Old: {oldjson}")
        print(f"New: {newjson}")
        for i in oldjson:
            if newjson[i] > oldjson[i] + 2:
                print(f"Buy {i}")
            else:
                print(f"Don't Buy {i}")
        updateJson(newjson)
        time.sleep(7*24*60*60)
    
    return 0

if __name__ == "__main__":
    main()
