import requests
import json

_CoinDeskAPI = "https://api.coindesk.com/v1/bpi/currentprice.json"


def ChangeTZ(string):
    string = string[:string.index('UTC')] + "EST"

    hour = string[string.index(':') - 2:string.index(':')]
    hour = str((int(hour) - 4) % 24).zfill(2)
    return (string[:string.index(':') - 2] + hour + string[string.index(':'):])


def main():
    r = requests.get(_CoinDeskAPI)
    btcJson = r.json()

    updatedTime = ChangeTZ(btcJson['time']['updated'])

    btcPrice = "$" + btcJson['bpi']['USD']['rate'][:-2]
    userPrice = str(float(btcJson['bpi']['USD']['rate'][:-2].replace(',',''))*0.02048329)
    

    infoString = "As of " + updatedTime + ", the price of Bitcoin is: " + btcPrice + "\n"
    infoString += "This turns your 0.02048329 BTC into $" + (userPrice[:userPrice.index('.') + 3]) + "\n"

    return infoString