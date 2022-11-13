from flask import Flask, request, render_template, redirect
import joblib
import requests

# Declare a Flask app
app = Flask(__name__)

# Main function here

@app.route('/', methods=['GET', 'POST'])
def main():
    # If a form is submitted
    if request.method == "POST":
        if request.form.get("predict")=="predict":
            return redirect("/predict")
        if request.form.get("dashboard")=="dashboard":
            return redirect("/dashboard")        
    return render_template("website.html")    

# Running the app
if __name__ == '__main__':
    app.run(debug = True)
