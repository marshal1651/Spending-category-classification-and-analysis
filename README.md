Customer Spending Analysis & Prediction

📌 Project Overview

This project focuses on analyzing customer spending patterns using real-world structured data. The workflow includes:

Data cleaning and merging

Exploratory analysis and dashboard building

Feature engineering and preprocessing

Applying multiple Machine Learning models for spending category prediction

Model evaluation and comparison



---

🗂️ Dataset

Size: ~90,000 rows (after cleaning & merging)

Features: Customer demographics, transaction details, product categories, etc.

Target: Spending_Category (Low, Medium, High)



---

🔧 Steps Performed

1. Data Cleaning & Preparation

Removed null values and duplicates

Standardized column names and formats

Merged multiple datasets into a single structured file


2. Exploratory Data Analysis (EDA)

Built a Power BI Dashboard for customer insights

Visualized: spending trends, product preferences, demographics, seasonal effects


3. Feature Engineering

Created new target column: Spending_Category

Encoded categorical features

Applied feature scaling


4. Model Building

Applied and compared multiple classification algorithms:

Logistic Regression

Decision Tree

Random Forest

K-Nearest Neighbors (KNN)

Support Vector Machine (SVM)

Naive Bayes


5. Hyperparameter Tuning

Performed tuning for Decision Tree and Random Forest


6. Model Evaluation

Evaluated on Accuracy, Precision, Recall, F1-score

Compared results in tabular & graphical form



---

📊 Results

Random Forest performed the best among all models

Achieved highest accuracy and balanced performance across categories



---

📌 Tech Stack

Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)

Power BI (Dashboard creation & visualization)



---

📂 Project Structure

├── data/                 # Raw and cleaned datasets  
├── notebooks/            # Jupyter notebooks / scripts  
├── dashboard/            # Power BI files  
├── models/               # Saved model files (if applicable)  
├── README.md             # Project documentation


---

🚀 Future Improvements

Try advanced ML models (XGBoost, LightGBM)

Deploy model as a web app using Streamlit/Flask

Automate dashboard refresh with live data



---

👤 Author

Armaan Siddiqui 
gwarmaan1651@gmail.com

🔗 [LinkedIn Profile: //www.linkedin.com/in/armaansiddiqui/]


---
