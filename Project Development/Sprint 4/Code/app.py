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
        import pickle
        import numpy as np
        model = pickle.load(open(r"./heart_disease.sav", "rb"))
        scaled = pickle.load(open(r"./scaler.sav", "rb"))
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
        user_input = np.array(user_input)
        user_input = user_input.reshape(1,-1)
        user_input = scaled.fit_transform(user_input)
        prediction = model.predict(user_input)
         # token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
        # API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        # mltoken = token_response.json()["access_token"]
        # header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
        # payload_scoring = {"input_data": [{"fields": ["Age","Sex","Chest pain type","BP","Cholesterol","FBS over 120","EKG results","Max HR","Exercise angina","ST depression","Slope of ST","Number of vessels fluro","Thallium"], "values": [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]}]}
        # response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/2c94f5e4-04ea-43dd-9d5a-c0365c95b676/predictions?version=2022-11-10', json=payload_scoring,
        # headers={'Authorization': 'Bearer ' + mltoken})
        # response_scoring = response_scoring.json()   
        # print(response_scoring)  
        # # Get prediction
        # prediction = response_scoring["predictions"][0]["values"][0][0]
        if prediction=='Presence':
            output = "Sorry "+name+", you are at high risk of having a heart disease. Please consult a doctor as soon as possible"
            image = "../static/high-risk.jpg"
        elif prediction=='Absence':
            output = "Hi "+name+", you are at low risk of having a heart disease. If you are still not convinced please consult a doctor"
            image = "../static/low-risk.jpg"
        else:
            output = "Hey "+name+", there was some error processing your details. Please try again later."
            image = "../static/error.png"
            
        return render_template("result.html", output = output, result=image)
                
    return render_template("predictor.html")

# Running the app
if __name__ == '__main__':
    app.run(debug = True)
