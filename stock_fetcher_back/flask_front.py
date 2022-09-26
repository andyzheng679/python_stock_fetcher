from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
        

@app.route("/rtp",methods=["POST", "GET"])
def rtp():
    if request.method == "POST":
        ticker = request.form["rtp"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("rtp.html")

@app.route("/quotes",methods=["POST", "GET"])
def quotes():
    if request.method == "POST":
        ticker = request.form["quotes"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("quotes.html")

@app.route("/ts",methods=["POST", "GET"])
def ts():
    if request.method == "POST":
        ticker = request.form["ts"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("ts.html")




@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)