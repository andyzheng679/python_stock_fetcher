import requests
import creds


base_url = "https://api.twelvedata.com/"

class input_check:
    def checker(start):
        try:
            user_input = int(start)
            if int(start) == 1:
                real_time_price.rtp_display(start)
            if int(start) == 2:
                quotes.quote_display(start)
            if int(start) == 3:
                time_series.ts_display(start)
        except ValueError:
            print("Invalid Entry, Try Again")

class real_time_price:
    def rtp_display(start):
        ticker_symbol = input("Enter ticker symbol you want to view: ").upper()
        rtp_url = f"{base_url}price?symbol={ticker_symbol}&apikey={creds.api_key}"
        rtp_data = requests.get(rtp_url).json()

        try:
            if rtp_data['code'] == 400:
                print("Invalid Symbol")
        except KeyError:
            print(ticker_symbol)
            print(rtp_data)
            
class quotes:
    def quote_display(start):
        ticker_symbol = input("Enter ticker symbol you want to view: ").upper()
        quote_url = f"{base_url}quote?symbol={ticker_symbol}&apikey={creds.api_key}"
        quote_data = requests.get(quote_url).json()
        
        try:
            if quote_data['code'] == 400:
                print("Invalid Symbol")
        except KeyError:
            print(ticker_symbol)
            print(quote_data)

class time_series:
    def ts_display(start):
        ticker_symbol = input("Enter ticker symbol you want to view:" ).upper()
        ts_url = f"{base_url}time_series?symbol={ticker_symbol}&interval=1day&apikey={creds.api_key}"
        ts_data = requests.get(ts_url).json()
        
        try:
            if ts_data['code'] == 400:
                print("Invalid Symbol")
        except KeyError:
            print(ts_data["values"])



while True:
    start = input("Enter 1 to view Real-Time Data,\nEnter 2 to view Quotes,\nEnter 3 to view Time Series: ")
    
    
    try:
        if int(start) >= 4:
            print("Invalid Entry, Try Again")
            continue
        elif int(start) == 0:
            break
        else:
            input_check.checker(start)
    except ValueError:
        input_check.checker(start)
        continue

        
