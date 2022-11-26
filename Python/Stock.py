import time
import json

def getStocks():
    with open("../Stocks.json", "r") as f:
        return json.load(f)

def getChange(stock):

    pass

def Buy(change):
    if change > 0:
        return True
    else:
        return False

def main():
    while(True):
        try:
            stocks = getStocks()
            for i in stocks:
                change = getChange(i)
                if Buy(change):
                    print(f"Buy Stock {i}")
                else:
                    print(f"Sell Stock {i}")
        
            time.sleep(7*24*60*60) #Wait 1 week
        except:
            print("Failure")

if __name__ == "__main__":
    main()
