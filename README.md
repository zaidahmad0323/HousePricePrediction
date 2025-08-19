
# 🏠 House Price Prediction Web App

This is a Machine Learning-based web application that predicts house prices based on user input such as location, number of bedrooms (BHK), number of bathrooms, and area (in square feet). The app uses a trained ML model and is built with Flask on the backend and HTML/CSS/JavaScript on the frontend.

---

## 📌 Features

- Predict house prices in real-time
- Location, BHK, bathroom, and area-based predictions
- Trained on real housing data
- Used 3 models: Linear Regression, Lasso Regression, and Decision Tree Regressor
- Used `cross_val_score` for model evaluation
- Used `GridSearchCV` for hyperparameter tuning
- Simple frontend using HTML, CSS, and JavaScript

---

## 🧠 Machine Learning

### ✅ Models Used:
- **Linear Regression**
- **Lasso Regression**
- **Decision Tree Regressor**

### 📊 Evaluation Methods:
- **Cross-validation** with `cross_val_score`
- **Hyperparameter tuning** with `GridSearchCV`

All models were tested and the best one was selected based on accuracy and performance.

---

## 💻 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **ML Libraries**: scikit-learn, Pandas, NumPy
- **Visualization**: Matplotlib

---

## 📂 Project Structure

```
HousePricePrediction/
├── model/
│   └── regressions/         # Saved ML model files
├── server/
│   ├── app.py               # Flask server
│   ├── bangalore_house_price_prediction.pickle
│   ├── data_columns.json
│   ├── static/              # CSS and JS
│   │   ├── app.css
│   │   └── app.js
│   └── templates/
│       └── app.html
├── Procfile
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

1. **Clone the repo**

```bash
git clone https://github.com/zaidahmad0323/HousePricePrediction.git
cd HousePricePrediction
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Flask app**

```bash
cd server
python app.py
```

4. **Open your browser**

```
http://127.0.0.1:5000
```

---

## 🛠️ Future Improvements

- Improve frontend UI with Bootstrap
- Add more features like garage, year built, etc.
- Deploy to Heroku or Render for public use
- Add more advanced ML models

---

## 🙋‍♂️ About Me

**Zaid Ahmad**  
Aspiring AI Engineer | Python & ML Enthusiast  
📧 zaidahmad0323@gmail.com  
🌐 [LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📜 License

This project is licensed under the MIT License.
