from flask import Flask, render_template , request
import joblib
import numpy as np

app = Flask(__name__)

#load the modeles and scaler
LR_model = joblib.load("best_lr.joblib")
RF_model = joblib.load("best_rf.joblib")
# scaler = pickle.load(open('scaler.plk' , 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict' , methods=['POST'])
def predict():
    #from_data = [float(x) for x in request.form.values() if x not in ['logistic' , 'RF']]
    model_selection = request.form.get('model_selection')

    #read input in the same order as trainin
    features = np.array([[
        float(request.form["Pregnancies"]),
        float(request.form["Glucose"]),
        float(request.form["BloodPressure"]),
        float(request.form["SkinThickness"]),
        float(request.form["Insulin"]),
        float(request.form["BMI"]),
        float(request.form["DiabetesPedigreeFunction"]),
        float(request.form["Age"])
    ]])

    #model selection
    if model_selection == 'logistic':
        prediction = LR_model.predict(features)
        model_name = "Logistic regression"

    elif model_selection == 'RF':
        prediction = RF_model.predict(features)
        model_name = "Random Forest"

    else:
        return render_template("index.htm" , prediction_text="please select a model,")     

    result = "High Risk" if prediction[0] == 1 else "low Risk"
    return render_template('index.html' , prediction_text=f'result ({model_name}) : {result}') 
if __name__ == "__main__" : 
    app.run(debug=True)

