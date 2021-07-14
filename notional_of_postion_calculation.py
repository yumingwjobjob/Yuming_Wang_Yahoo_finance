import yahoo_finance_api_client
class notion_of_position_calculation:
        def get_notional_of_position(self,quantity, symbol):
            yahoo_finance_api = yahoo_finance_api_client.yahoo_finance_api().get_instance()
            #yahoo_finance_api = yahoo_finance_api_client.yahoo_finance_api()
            raw_price = yahoo_finance_api.get_regular_market_previous_close_symbol(symbol)
            quantity = float(quantity)
            final_price = raw_price * quantity
            final_price = "{:.2f}".format(final_price)
            return final_price
