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

    def quote_open(self, ticker):
        ticker = ticker.upper()
        quote_url = f"{base_url}quote?symbol={ticker}&apikey={creds.api_key}"
        quote_data = requests.get(quote_url).json()
        return "Open : %s" %  quote_data.get('open')
    
    def quote_high(self, ticker):
        ticker = ticker.upper()
        quote_url = f"{base_url}quote?symbol={ticker}&apikey={creds.api_key}"
        quote_data = requests.get(quote_url).json()
        return "High : %s" %  quote_data.get('high')

    def quote_low(self, ticker):
        ticker = ticker.upper()
        quote_url = f"{base_url}quote?symbol={ticker}&apikey={creds.api_key}"
        quote_data = requests.get(quote_url).json()
        return "Low : %s" %  quote_data.get('low')
    
    def quote_close(self, ticker):
        ticker = ticker.upper()
        quote_url = f"{base_url}quote?symbol={ticker}&apikey={creds.api_key}"
        quote_data = requests.get(quote_url).json()
        return "Close : %s" %  quote_data.get('close')

    def quote_volume(self, ticker):
        ticker = ticker.upper()
        quote_url = f"{base_url}quote?symbol={ticker}&apikey={creds.api_key}"
        quote_data = requests.get(quote_url).json()
        return "Volume : %s" %  quote_data.get('volume')
    
    def quote_pre_close(self, ticker):
        ticker = ticker.upper()
        quote_url = f"{base_url}quote?symbol={ticker}&apikey={creds.api_key}"
        quote_data = requests.get(quote_url).json()
        return "Previous close : %s" %  quote_data.get('previous_close')
    
    def quote_avg_vol(self, ticker):
        ticker = ticker.upper()
        quote_url = f"{base_url}quote?symbol={ticker}&apikey={creds.api_key}"
        quote_data = requests.get(quote_url).json()
        return "Average volume : %s" %  quote_data.get('average_volume')
    
    def quote_fifty_two_high(self, ticker):
        ticker = ticker.upper()
        quote_url = f"{base_url}quote?symbol={ticker}&apikey={creds.api_key}"
        quote_data = requests.get(quote_url).json()
        return "Fifty-two week : %s" %  quote_data.get('fifty_two_week')

class time_series:
    def ts(self, ticker):
        
        ticker = ticker.upper()
        ts_url = f"{base_url}time_series?symbol={ticker}&interval=1day&apikey={creds.api_key}"
        ts_data = requests.get(ts_url).json()
        data2 = pd.DataFrame(ts_data["values"])
        return data2
