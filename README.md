# Diabetes Risk Prediction App

A machine learning-powered web application that predicts the likelihood of diabetes based on user health information. The application provides a simple, interactive interface for entering medical parameters and receiving an instant prediction.

## 📌 Overview
This project was done as a part of my final year Bachelor's degree project 

The **Diabetes Risk Prediction App** leverages a trained machine learning model to estimate whether a user is at risk of diabetes using clinical features such as glucose level, BMI, age, blood pressure, and insulin level. This project demonstrates the complete machine learning workflow, from data preprocessing and model training to deployment in a user-friendly web application.

> **Disclaimer:** This application is intended for educational purposes only and should **not** be used as a substitute for professional medical diagnosis or treatment.

---

## 🚀 Features

- **Predicts diabetes risk** using a trained machine learning model
- **Clean and responsive** user interface
- **Real-time** prediction results
- **Input validation** for accurate data entry
- **Easy-to-use** web application
- **Lightweight and fast** performance

---

## 📂 Project Structure

```text
Diabetes-Risk-Prediction-App/
│
├── static/               # CSS, JavaScript, Images
├── templates/            # HTML Templates
├── model/                # Trained ML Model
├── app.py                # Flask Application
├── requirements.txt      # Python Dependencies
├── README.md
└── dataset.csv           # Dataset (PIMA INDIANS)

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📊 Input Parameters

The model accepts the following medical information:

- **Number of Pregnancies**
- **Glucose Level**
- **Blood Pressure**
- **Skin Thickness**
- **Insulin Level**
- **Body Mass Index (BMI)**
- **Diabetes Pedigree Function**
- **Age**

---

## 🧠 Machine Learning Workflow

1. **Data Collection**
2. **Data Cleaning and Preprocessing**
3. **Feature Selection**
4. **Model Training**
5. **Model Evaluation**
6. **Model Serialization**
7. **Flask Integration**
8. **Web Deployment**

---

## 📈 Output

The application predicts whether the user is:

- **Low Risk of Diabetes**
- **High Risk of Diabetes**

The prediction is generated instantly after submitting the required information.

---


## 🔮 Future Improvements

- User authentication
- Prediction confidence score
- Medical history storage
- Data visualization dashboard
- Cloud deployment
- Explainable AI (feature importance)
- Support for additional health indicators

---

## 👨‍💻 Author

**Yekta Ahmadifar**

GitHub Repository:

https://github.com/Yekta-Ahmadifar/Diabetes-Risk-Prediction-App
