import requests
import json
class yahoo_finance_api:
    def get_regular_market_previous_close_symbol(self,symbol):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

        querystring = {"symbol":symbol,"region":"US"}

        headers = {
        'x-rapidapi-key': "1a5d467378msh93fb379ab511567p1a1a82jsn0f1bb63d2039",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        payload = json.loads(response.text)
        #(response.text)
        #print(payload["price"])
        #print(payload)
        raw_price = payload["price"]['regularMarketPreviousClose']['raw']
        return float(raw_price)