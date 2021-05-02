from flask import Flask, render_template
import machine_learning as ml
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction")
def prediction():
    ml.show("Juan")
    return render_template("prediction.html")