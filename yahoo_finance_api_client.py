import requests
import json
class yahoo_finance_api:

    #set a singleton method
    __instance = None
    #@staticmethod
    def get_instance(self):
        if yahoo_finance_api.__instance == None:
            yahoo_finance_api()
        return yahoo_finance_api.__instance
    
    def __init__(self):
        if yahoo_finance_api.__instance != None:
            print("ERROR")
        else:
            yahoo_finance_api.__instance = self
    #set url and headers tp static
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
    headers = {
        'x-rapidapi-key': "1a5d467378msh93fb379ab511567p1a1a82jsn0f1bb63d2039",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }
    def get_regular_market_previous_close_symbol(self,symbol):

        querystring = {"symbol":symbol,"region":"US"}
        response = requests.request("GET", self.url, headers=self.headers, params=querystring)
        payload = json.loads(response.text)

        
        #(response.text)
        #print(payload["price"])
        #print(payload)
        #add a error handling
        while True:
            try:
                raw_price = payload["price"]['regularMarketPreviousClose']['raw']
                break
            except(RuntimeError, TypeError, NameError):
                print("ERROR, EMPTY PRICE")
                return 0
        return float(raw_price)