# 🧑‍💼 Employee Attrition Prediction using Machine Learning

> Predicting which employees are likely to leave a company using HR data — so management can take preventive action before it's too late.

---

## 📌 Project Overview

Employee attrition is costly. Every time an employee leaves, a company spends time and money on rehiring and retraining. This project builds a machine learning pipeline that analyses HR data and predicts which employees are at risk of leaving — giving HR teams the chance to intervene early.

This was completed as **Week 2 of a Data Science Internship**.

---

## 📂 Dataset

- **Source:** IBM HR Analytics Employee Attrition Dataset
- **Size:** 1,470 employees × 35 features
- **Target column:** `Attrition` (Yes/No → 1/0)
- **Class balance:** 83.9% stayed, 16.1% left (imbalanced)

---

## 🗂️ Project Structure

```
employee-attrition-prediction/
│
├── WA_Fn-UseC_-HR-Employee-Attrition.csv   # Dataset
├── employee_attrition.ipynb                 # Main Colab notebook
├── charts/                                  # All visualizations
│   ├── chart1_attrition_by_dept_role.png
│   ├── chart2_income_vs_attrition.png
│   ├── chart3_confusion_matrix.png
│   ├── chart4_feature_importance.png
│   └── chart5_roc_curve.png
└── README.md
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | Data loading and cleaning |
| NumPy | Numerical operations |
| Matplotlib & Seaborn | Data visualization |
| Scikit-learn | Preprocessing, model training, evaluation |
| Google Colab | Development environment |

---

## 🔢 Project Workflow

### Task 1 — Data Loading & Exploration
- Loaded CSV using Pandas
- Identified target column (`Attrition`)
- Found dataset is imbalanced — only 16.1% attrition rate
- Identified 26 numeric and 9 categorical columns

### Task 2 — Data Cleaning & Preprocessing
- Confirmed zero null values across all columns
- Dropped irrelevant columns: `EmployeeNumber`, `Over18`, `StandardHours`, `EmployeeCount`
- Converted `Attrition` from Yes/No to 1/0
- Applied One-Hot Encoding to all categorical columns (`pd.get_dummies`)
- Scaled numeric features using `StandardScaler`

### Task 3 — Exploratory Data Analysis (EDA)
- Attrition rate by Department and Job Role
- Monthly Income distribution by Attrition
- Work-Life Balance vs Attrition
- Years at Company vs Attrition trend

### Task 4 — Model Building & Comparison
- Split data 80/20 using `train_test_split`
- Handled class imbalance using `class_weight='balanced'`
- Trained 3 models: Logistic Regression, Random Forest, Gradient Boosting

### Task 5 — Model Evaluation
- Evaluated using Precision, Recall, F1-Score, AUC-ROC, Confusion Matrix
- Extracted Top 10 Feature Importances from best model

### Task 6 — Visualization
- Created and saved 5 charts covering attrition patterns, income distribution, confusion matrix, feature importance, and ROC curves

### Task 7 — HR Insights & Business Recommendations
- Translated model findings into actionable HR recommendations

---

## 📊 Model Comparison Results

| Model | Accuracy | Recall (Leavers) | AUC-ROC |
|---|---|---|---|
| Logistic Regression | 0.72 | **0.59** ✅ | 0.766 |
| Random Forest | 0.87 | 0.08 ❌ | 0.734 |
| Gradient Boosting | 0.87 | 0.18 ❌ | **0.779** |

---

## 🏆 Best Model: Logistic Regression

Despite having lower overall accuracy, Logistic Regression was selected as the best model because:

- It correctly identified **59% of employees who actually left** — the highest recall among all 3 models
- In HR context, **missing an at-risk employee (False Negative) is more costly** than a false alarm
- It is the most **explainable model** — HR teams can understand which factors drive each prediction
- Random Forest and Gradient Boosting scored 87% accuracy but only caught 8% and 18% of actual leavers respectively — making them unreliable for this use case

---

## 🔍 Top 10 Features Driving Attrition

| Rank | Feature | Importance Score |
|---|---|---|
| 1 | YearsAtCompany | 0.973 |
| 2 | OverTime_Yes | 0.926 |
| 3 | JobRole_Laboratory Technician | 0.903 |
| 4 | MaritalStatus_Single | 0.776 |
| 5 | YearsInCurrentRole | 0.724 |
| 6 | BusinessTravel_Travel_Frequently | 0.710 |
| 7 | Department_Sales | 0.621 |
| 8 | JobRole_Sales Representative | 0.612 |
| 9 | YearsWithCurrManager | 0.560 |
| 10 | JobRole_Human Resources | 0.540 |

---

## 💡 Key Business Insights

1. **Sales Representatives** have the highest attrition rate at **39.8%** — nearly 1 in 2 leave
2. **Overtime** is the 2nd strongest predictor of attrition — a clear sign of burnout
3. Employees who left earned on average **₹2,000/month less** than those who stayed
4. Employees with a **Work-Life Balance rating of 1** leave at 31.2% — more than double those rated 3
5. Attrition peaks in the **first 1–3 years** at the company

---

## 📋 HR Recommendations

**1. Introduce an Overtime Alert System**
Flag employees working consistent overtime for a manager check-in — overtime is the 2nd strongest predictor of exit and is immediately actionable.

**2. Create a Retention Plan for Sales Representatives in Years 1–3**
With a 39.8% exit rate and attrition peaking in early tenure, structured career conversations, mentorship, and clear promotion timelines should be introduced for this group specifically.

---

## ⚠️ Model Limitations

- The model correctly identifies approximately **6 in 10 at-risk employees** — 4 in 10 are still missed
- Trained on a single dataset — results may vary across different companies and industries
- Should be used as a **support tool** for HR decisions, not a definitive predictor
- Does not account for external factors like job market conditions or personal circumstances

---

## 🚀 Future Improvements

- Apply **SMOTE** for oversampling and compare with `class_weight='balanced'`
- Tune hyperparameters using **GridSearchCV**
- Try **XGBoost** which may outperform standard Gradient Boosting
- Build an interactive **HR dashboard** using Streamlit or Power BI

---

## 👨‍💻 Author

**Internship Project — Week 2**
Data Science Intern
Date: June 23–26, 2026
