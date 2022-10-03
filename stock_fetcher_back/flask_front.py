from flask import Flask, redirect, url_for, render_template, request
from stock_fetcher import real_time_price
from stock_fetcher import real_quotes
from stock_fetcher import time_series



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
        

@app.route("/rtp",methods=["POST", "GET"])
def rtp():
    if request.method == "POST":
        ticker = request.form["rtp"]
        return redirect(url_for("display_rtp", usr=ticker))
    else:
        return render_template("rtp.html")

@app.route("/quotes",methods=["POST", "GET"])
def quotes():
    if request.method == "POST":
        ticker = request.form["quotes"]
        return redirect(url_for("display_quotes", usr=ticker))
    else:
        return render_template("quotes.html")

@app.route("/ts",methods=["POST", "GET"])
def ts():
    if request.method == "POST":
        ticker = request.form["ts"]
        return redirect(url_for("display_ts", usr=ticker))
    else:
        return render_template("ts.html")



@app.route("/<usr>_real_time_price")
def display_rtp(usr):
    data = real_time_price().rtp(usr)
    return f"<center><h1>{usr}</h1><h2>{data}</h2></center>"

@app.route("/<usr>_real_quotes")
def display_quotes(usr):
    data = real_quotes().test_quotes(usr)
    return render_template("display_quotes.html",data=data,usr=usr)


@app.route("/<usr>_time_series")
def display_ts(usr):
    data = time_series().ts(usr)
    return render_template("display_ts.html",data=data,usr=usr)
    




# remember debug=True when working on this 
if __name__ == "__main__":
    app.run()