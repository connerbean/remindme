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

    infoString = "As of " + updatedTime + ", the price of Bitcoin is: " + btcPrice
    return infoString