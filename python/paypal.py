#termianl  cd ~/Desktop/Paypal
# export FLASK_APP=beatmaker.py (which py u wanna use)
#flask run (run)
# export FLASK_ENV=development(debug mode on)
#flask run (run)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    headline = "HI"
    return render_template("index.html", headline= headline)

#exchange
@app.route("/exchange", methods=["POST"])
def exchange():
    item = request.form.get("item")
    headline = "exchange"
    return render_template("exchange.html", headline = headline, item=item)
