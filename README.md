# 🏠 House Price Prediction with XGBoost

## 📌 Project Overview
This project predicts house prices using machine learning techniques and the XGBoost algorithm.

The goal was to improve prediction accuracy through feature engineering, model comparison, and boosting methods.

---

## 📊 Dataset
- Source: Ames Housing Dataset
- Problem Type: Regression
- Target Variable: `SalePrice`

---

## 🔍 Project Workflow
- Data cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Log transformation
- Train/Test split
- Random Forest baseline model
- XGBoost implementation
- Feature importance analysis
- Streamlit deployment

---

## ⚙️ Features Used
```text
OverallQual
GrLivArea
TotalBsmtSF
Age
LotArea_log
GarageArea
GarageCars
TotRmsAbvGrd
FullBath
```
---

## 🤖 Models Used
### Random Forest Regressor
MAE: 18724

### XGBoost Regressor
MAE: 18150

XGBoost achieved better performance and produced more realistic feature importance patterns.

---

## 📈 Feature Importance Insights
Key observations:

- OverallQual remained the most important feature.
- GarageCars and FullBath became significantly more important in XGBoost.
- XGBoost captured more realistic relationships between house quality and pricing.

This suggests that boosting models can detect more subtle feature interactions compared to Random Forest.

---

## 🚀 Streamlit Web App
Live App:

https://house-price-app-app-82fv4yt2hyg7wiudzwkotx.streamlit.app/

The app allows users to enter house features and receive predicted house prices in real time.

---

## 🧠 Business Value
This project demonstrates how machine learning can help:

- Estimate property prices
- Support real estate decision-making
- Analyze key pricing factors
- Build deployable prediction systems

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Matplotlib
- Seaborn

---

## ▶️ How to Run
### 1. Clone the repository
  git clone <repo-link>

### 2. Install dependencies
  pip install -r requirements.txt

### 3. Run Streamlit app
  streamlit run app.py

  ---
  
## 👨‍💻 Author
Hossein Fathi
