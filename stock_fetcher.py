import requests
import creds

base_url = "https://api.twelvedata.com/"


class input_check:
    def checker(start):
        try:
            user_input = int(start)
            print("yes")
        except ValueError:
            print("Invalid Entry, not an int")

while True:
    start = input("Enter 1 to view Real-Time Data,\nEnter 2 to view Quotes,\nEnter 3 to view Time Series: ")

    try:
        if int(start) >= 4:
            print("Invalid Entry, Try Again")
            continue
        else:
            input_check.checker(start)
    except ValueError:
        input_check.checker(start)
        continue


    break







# Real-Time Price

#ticker_symbol = input("Enter ticker symbol you want to view: ").upper()
#rtp_url = f"{base_url}price?symbol={ticker_symbol}&apikey={creds.api_key}"
#rtp_data = requests.get(rtp_url).json()
#print(ticker_symbol)
#print(rtp_data)

# Quote

#ticker_symbol = input("Enter ticker symbol you want to view: ").upper()
#quote_url = f"{base_url}quote?symbol={ticker_symbol}&apikey={creds.api_key}"
#quote_data = requests.get(quote_url).json()
#print(ticker_symbol)
#print(quote_data)

# Times Series

#ticker_symbol = input("Enter ticker symbol you want to view:" ).upper()
#ts_url = f"{base_url}time_series?symbol={ticker_symbol}&interval=1day&apikey={creds.api_key}"
#ts_data = requests.get(ts_url).json()
#print(ts_data["values"])            
