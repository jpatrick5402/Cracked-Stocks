import datetime, time, json, copy, os
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestBarRequest

def getOldJson():
    with open("./Stocks.json", "r") as f:
        return json.load(f)

def getNewJson(oldjson, KEY, PKEY):
    newjson = copy.copy(oldjson)
    client = StockHistoricalDataClient(KEY, PKEY)
    for i in oldjson:
            requests = StockLatestBarRequest(symbol_or_symbols=i)
            data = client.get_stock_latest_bar(request_params=requests)
            newjson[i] = data[i].dict()["close"]
    return newjson

def updateJson(newjson):
    with open("./Stocks.json", "w") as f:
        json.dump(newjson, f)

def calculate(oldjson,newjson,stock):
    old = oldjson[stock]
    new = newjson[stock]
    precent_for_change = .05
    if new > old + (precent_for_change * old):
        return 1
    elif new < old - (precent_for_change * old):
        return 0
    else:
        return 2

def invest(result, stock): 
    if result == "BUY":
        pass
    elif result == "SELL":
        pass
    elif result == "HOLD":
        pass

def main():

    while(True):
        try:
            KEY = os.environ["API_KEY"]
            PKEY = os.environ["PRIVATE_KEY"]
        except:
            KEY = input("Enter your API KEY: ")
            PKEY = input("Enter your Private API KEY: ")

        oldjson = getOldJson()
        newjson = getNewJson(oldjson, KEY, PKEY)
        print(datetime.datetime.now())
        print(f"Old: {oldjson}")
        print(f"New: {newjson}")
        for i in oldjson:
            answer = calculate(oldjson,newjson,i)
            if answer == 1:
                print(f"Buy {i}")
            elif answer == 0:
                print(f"Don't Buy {i}")
            elif answer == 2:
                print(f"Hold {i}")

        updateJson(newjson)
        time.sleep(7*24*60*60)
    
    return 0

if __name__ == "__main__":
    main()
