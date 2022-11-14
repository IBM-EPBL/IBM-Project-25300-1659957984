from flask import Flask, request, render_template, redirect
import joblib
import requests

# Declare a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        if request.form.get("predict")=="predict":
            return redirect("/predict")
        if request.form.get("dashboard")=="dashboard":
            return redirect("/dashboard")        
    return render_template("website.html")    

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        # Get values through input bars
        name = request.form.get("name")
        age =   request.form.get('age')
        sex =   request.form.get('sex')
        cp =   request.form.get('cp')
        trestbps =   request.form.get('trestbps')
        chol =   request.form.get('chol')
        fbs =   request.form.get('fbs')
        restecg =   request.form.get('restecg')
        thalach =   request.form.get('thalach')
        exang =   request.form.get('exang')
        oldpeak =   request.form.get('oldpeak')
        slope =   request.form.get('slope')
        ca =   request.form.get('ca')
        thal =   request.form.get('thal')
        
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

        print(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal)
    return render_template("predictor.html")

# Running the app
if __name__ == '__main__':
    app.run(debug = True)
