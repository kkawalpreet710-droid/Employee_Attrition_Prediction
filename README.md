# ⬡ AttritionIQ — Employee Attrition Prediction App

A full-stack HR intelligence web app built with Streamlit.
Predicts which employees are at risk of leaving using a Logistic Regression model trained on IBM HR Analytics data.

---

## Pages

| Page | Description |
|---|---|
| Home | Landing page with project overview and stats |
| Dashboard | Charts — attrition by dept, role, income, feature importance |
| Predict | Single employee risk prediction with live sliders |
| Bulk Upload | Upload CSV → get risk scores for all employees → download results |

---

## Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/attritioniq.git
cd attritioniq

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## Deploy to Streamlit Cloud

1. Push this folder to a GitHub repository
2. Go to share.streamlit.io
3. Click "New app"
4. Select your repo → set Main file path to `app.py`
5. Click Deploy

That's it — your app will be live in under 2 minutes!

---

## Project Structure

```
attritioniq/
├── app.py                  # Main entry point
├── requirements.txt        # Dependencies
├── .streamlit/
│   └── config.toml         # Dark theme config
├── pages/
│   ├── landing.py          # Home page
│   ├── dashboard.py        # Charts dashboard
│   ├── predict.py          # Single prediction
│   └── bulk_upload.py      # CSV bulk prediction
└── utils/
    ├── model.py             # Scoring logic
    └── style.py             # CSS injection
```

---

## Tech Stack

- **Streamlit** — web framework
- **Plotly** — interactive charts
- **Pandas** — data handling
- **Scikit-learn** — model (Logistic Regression)

---

Built during Data Science Internship · Week 2 · June 2026
