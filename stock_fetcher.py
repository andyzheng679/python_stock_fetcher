import requests

api_key = ""
base_url = "https://api.twelvedata.com/time_series?"
ticker = input("Enter ticker symbol you want to view:" )
request_url = f"{base_url}symbol={ticker}&interval=1day&apikey={api_key}"
data = requests.get(request_url).json()
print(data["values"][0])            # prints most current data
