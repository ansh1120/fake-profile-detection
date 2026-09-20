# Fake Profile Detection

A machine learning based web application for detecting potentially fake social media profiles.

## 📌 Project Overview

Fake Profile Detection is an academic project developed using Python and Flask. The application analyzes profile-related information and uses a trained machine learning model to predict whether a profile is likely to be fake or genuine.

The project also provides a web-based interface where users can interact with the profile detection system.

## 🚀 Features

- User-friendly web interface
- Fake profile prediction using Machine Learning
- Profile checking functionality
- Trained ML model integration
- Dataset-based prediction
- Flask-based web application
- Result display through web pages

## 🛠️ Technologies Used

- Python
- Flask
- Machine Learning
- Pandas
- NumPy
- Scikit-learn
- HTML
- CSS
- SQLite
- Git & GitHub

## 🤖 Machine Learning

The application uses a trained machine learning model stored in:

`fake_profile_model.pkl`

The project uses profile-related attributes from the dataset to generate predictions.

## 📂 Project Structure

```text
fake-profile-detection/
│
├── app.py
├── model.py
├── dataset.csv
├── fake_profile_model.pkl
├── requirements.txt
├── .gitignore
│
├── static/
│   └── bg.jpg
│
└── templates/
    ├── about.html
    ├── check_profile.html
    ├── contact.html
    ├── dashboard.html
    ├── login.html
    ├── result.html
    └── statistics.html
