import requests
import creds
import pandas as pd


base_url = "https://api.twelvedata.com/"

class real_time_price:
    def rtp(self, ticker):
        
        ticker = ticker.upper()
        rtp_url = f"{base_url}price?symbol={ticker}&apikey={creds.api_key}"
        rtp_data = requests.get(rtp_url).json()
        return rtp_data
        

class real_quotes:
    def test_quotes(self, ticker):
        
        ticker = ticker.upper()
        quote_url = f"{base_url}quote?symbol={ticker}&apikey={creds.api_key}"
        quote_data = requests.get(quote_url).json()
        return quote_data



class time_series:
    def ts(self, ticker):
        
        ticker = ticker.upper()
        ts_url = f"{base_url}time_series?symbol={ticker}&interval=1day&apikey={creds.api_key}"
        ts_data = requests.get(ts_url).json()
        data2 = pd.DataFrame(ts_data["values"])
        return data2
