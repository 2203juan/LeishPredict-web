from flask import Flask, render_template, request
import machine_learning as ml
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction", methods = ['POST', 'GET'])
def prediction():
    if request.method == 'POST':
        gender = request.form['gender']
        ethnicity = request.form['ethnicity']
        age = request.form['age']
        infection_department = request.form['department']
        #weight = request.form['weight']
        height = request.form['height']

        time = request.form['time']
        active = request.form['active']
        eb_lc_ulcera_area_1 = request.form['eb_lc_ulcera_area_1']
        dosis = request.form['dosis']

        data = [gender , ethnicity, age, infection_department, height,
                time, active, eb_lc_ulcera_area_1, dosis]
        ml.push_data(data)
        return render_template("results.html", data=data)
    else:
        return render_template("prediction.html")