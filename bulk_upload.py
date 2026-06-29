import streamlit as st
import pandas as pd
import io
from model import score_employee, get_risk_level

SAMPLE_DATA = [
    {'EmployeeID':'EMP-001','Department':'Sales','JobRole':'Sales Representative','MonthlyIncome':3200,'OverTime':'Yes','BusinessTravel':'Travel_Frequently','YearsAtCompany':1,'YearsInCurrentRole':1,'YearsWithCurrManager':0,'MaritalStatus':'Single','WorkLifeBalance':1},
    {'EmployeeID':'EMP-002','Department':'Research and Development','JobRole':'Laboratory Technician','MonthlyIncome':2900,'OverTime':'Yes','BusinessTravel':'Travel_Rarely','YearsAtCompany':2,'YearsInCurrentRole':1,'YearsWithCurrManager':1,'MaritalStatus':'Single','WorkLifeBalance':2},
    {'EmployeeID':'EMP-003','Department':'Human Resources','JobRole':'Human Resources','MonthlyIncome':4100,'OverTime':'No','BusinessTravel':'Travel_Rarely','YearsAtCompany':3,'YearsInCurrentRole':2,'YearsWithCurrManager':2,'MaritalStatus':'Married','WorkLifeBalance':3},
    {'EmployeeID':'EMP-004','Department':'Sales','JobRole':'Sales Executive','MonthlyIncome':5500,'OverTime':'Yes','BusinessTravel':'Travel_Frequently','YearsAtCompany':4,'YearsInCurrentRole':2,'YearsWithCurrManager':1,'MaritalStatus':'Single','WorkLifeBalance':2},
    {'EmployeeID':'EMP-005','Department':'Research and Development','JobRole':'Research Scientist','MonthlyIncome':6800,'OverTime':'No','BusinessTravel':'Travel_Rarely','YearsAtCompany':6,'YearsInCurrentRole':4,'YearsWithCurrManager':3,'MaritalStatus':'Married','WorkLifeBalance':3},
    {'EmployeeID':'EMP-006','Department':'Research and Development','JobRole':'Manager','MonthlyIncome':15000,'OverTime':'No','BusinessTravel':'Non-Travel','YearsAtCompany':14,'YearsInCurrentRole':7,'YearsWithCurrManager':8,'MaritalStatus':'Married','WorkLifeBalance':4},
    {'EmployeeID':'EMP-007','Department':'Sales','JobRole':'Sales Representative','MonthlyIncome':3000,'OverTime':'Yes','BusinessTravel':'Travel_Frequently','YearsAtCompany':1,'YearsInCurrentRole':0,'YearsWithCurrManager':0,'MaritalStatus':'Single','WorkLifeBalance':1},
    {'EmployeeID':'EMP-008','Department':'Research and Development','JobRole':'Research Director','MonthlyIncome':18000,'OverTime':'No','BusinessTravel':'Travel_Rarely','YearsAtCompany':20,'YearsInCurrentRole':10,'YearsWithCurrManager':9,'MaritalStatus':'Married','WorkLifeBalance':4},
    {'EmployeeID':'EMP-009','Department':'Human Resources','JobRole':'Human Resources','MonthlyIncome':3800,'OverTime':'Yes','BusinessTravel':'Travel_Rarely','YearsAtCompany':2,'YearsInCurrentRole':1,'YearsWithCurrManager':1,'MaritalStatus':'Divorced','WorkLifeBalance':2},
    {'EmployeeID':'EMP-010','Department':'Research and Development','JobRole':'Laboratory Technician','MonthlyIncome':4200,'OverTime':'No','BusinessTravel':'Non-Travel','YearsAtCompany':5,'YearsInCurrentRole':3,'YearsWithCurrManager':4,'MaritalStatus':'Married','WorkLifeBalance':3},
    {'EmployeeID':'EMP-011','Department':'Sales','JobRole':'Sales Executive','MonthlyIncome':7200,'OverTime':'No','BusinessTravel':'Travel_Rarely','YearsAtCompany':8,'YearsInCurrentRole':5,'YearsWithCurrManager':6,'MaritalStatus':'Married','WorkLifeBalance':3},
    {'EmployeeID':'EMP-012','Department':'Research and Development','JobRole':'Manufacturing Director','MonthlyIncome':12000,'OverTime':'No','BusinessTravel':'Travel_Rarely','YearsAtCompany':12,'YearsInCurrentRole':6,'YearsWithCurrManager':7,'MaritalStatus':'Married','WorkLifeBalance':4},
]

def process_df(df):
    results = []
    for _, row in df.iterrows():
        score = score_employee(
            overtime=str(row.get('OverTime', 'No')),
            travel=str(row.get('BusinessTravel', 'Non-Travel')),
            role=str(row.get('JobRole', '')),
            marital=str(row.get('MaritalStatus', 'Single')),
            years=int(row.get('YearsAtCompany', 0)),
            years_role=int(row.get('YearsInCurrentRole', 0)),
            years_mgr=int(row.get('YearsWithCurrManager', 0)),
            income=int(row.get('MonthlyIncome', 5000)),
            wlb=int(row.get('WorkLifeBalance', 3)),
            dept=str(row.get('Department', ''))
        )
        results.append({
            'Employee ID': row.get('EmployeeID', row.get('EmployeeNumber', 'N/A')),
            'Department': row.get('Department', ''),
            'Job Role': row.get('JobRole', ''),
            'Income': f"₹{int(row.get('MonthlyIncome', 0)):,}",
            'Overtime': row.get('OverTime', 'No'),
            'Years': int(row.get('YearsAtCompany', 0)),
            'Risk Score': score,
            'Risk Level': get_risk_level(score),
        })
    return pd.DataFrame(results).sort_values('Risk Score', ascending=False)


def show():
    st.markdown("""
    <div style='margin-bottom:1.5rem;'>
        <h1 style='font-size:1.6rem;font-weight:800;color:#fff;margin:0;'>
            Bulk Employee Prediction
        </h1>
        <p style='font-size:11px;color:#555;margin-top:4px;'>
            Upload your HR CSV — get attrition risk scores for every employee instantly
        </p>
    </div>
    """, unsafe_allow_html=True)

    if 'bulk_results' not in st.session_state:
        st.session_state.bulk_results = None

    if st.session_state.bulk_results is None:
        st.markdown("""
        <div style='border:2px dashed #2a2a2a;border-radius:16px;
            padding:3rem 2rem;text-align:center;background:#1a1a1a;
            margin-bottom:1rem;'>
            <div style='font-size:40px;margin-bottom:1rem;'>📁</div>
            <div style='font-size:15px;font-weight:700;color:#fff;
                margin-bottom:6px;'>Drop your CSV file here</div>
            <div style='font-size:12px;color:#555;margin-bottom:1.5rem;'>
                Supports IBM HR Analytics format · Max 10,000 rows</div>
        </div>
        """, unsafe_allow_html=True)

        uploaded = st.file_uploader("Choose a CSV file", type=['csv'],
                                    label_visibility="collapsed")

        c1, c2 = st.columns(2)
        with c1:
            if uploaded:
                if st.button("→ Process Uploaded File", use_container_width=True):
                    df = pd.read_csv(uploaded)
                    st.session_state.bulk_results = process_df(df)
                    st.rerun()
        with c2:
            if st.button("Use Sample Data (12 employees)", use_container_width=True):
                df = pd.DataFrame(SAMPLE_DATA)
                st.session_state.bulk_results = process_df(df)
                st.rerun()

        st.markdown("""
        <div style='background:#1a1a1a;border:1px solid #2a2a2a;border-radius:10px;
            padding:1rem 1.2rem;margin-top:1rem;'>
            <div style='font-size:10px;color:#FFD84D;text-transform:uppercase;
                letter-spacing:1px;margin-bottom:8px;'>Expected CSV columns</div>
            <div style='font-size:11px;color:#555;line-height:1.8;'>
                Department · JobRole · OverTime · BusinessTravel · MonthlyIncome ·
                YearsAtCompany · YearsInCurrentRole · YearsWithCurrManager ·
                MaritalStatus · WorkLifeBalance
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        results = st.session_state.bulk_results
        high = len(results[results['Risk Level'] == 'HIGH'])
        med  = len(results[results['Risk Level'] == 'MEDIUM'])
        low  = len(results[results['Risk Level'] == 'LOW'])

        st.markdown(f"""
        <div style='background:#1a1a1a;border:1px solid #2a2a2a;border-radius:10px;
            padding:0.8rem 1.2rem;display:flex;align-items:center;gap:12px;
            margin-bottom:1rem;font-size:12px;'>
            <div style='width:8px;height:8px;border-radius:50%;
                background:#4ade80;flex-shrink:0;'></div>
            <div style='color:#888;'>
                Processed <span style='color:#fff;font-weight:600;'>{len(results)}</span> employees ·
                <span style='color:#f87171;font-weight:600;'>{high} high risk</span> ·
                <span style='color:#fbbf24;font-weight:600;'>{med} medium risk</span> ·
                <span style='color:#4ade80;font-weight:600;'>{low} low risk</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        for col, label, val, color in [
            (m1, "Total Processed", len(results), "#fff"),
            (m2, "High Risk", high, "#f87171"),
            (m3, "Medium Risk", med, "#fbbf24"),
            (m4, "Low Risk", low, "#4ade80"),
        ]:
            with col:
                st.markdown(f"""
                <div style='background:#1a1a1a;border:1px solid #2a2a2a;
                    border-radius:12px;padding:1rem 1.2rem;margin-bottom:1rem;'>
                    <div style='font-size:10px;color:#555;text-transform:uppercase;
                        letter-spacing:1px;margin-bottom:6px;'>{label}</div>
                    <div style='font-size:24px;font-weight:800;color:{color};'>{val}</div>
                </div>""", unsafe_allow_html=True)

        st.markdown("""<div style='background:#1a1a1a;border:1px solid #2a2a2a;
            border-radius:12px;padding:1.2rem 1.4rem;'>
            <div style='font-size:11px;font-weight:700;text-transform:uppercase;
                letter-spacing:1px;color:#fff;margin-bottom:1rem;'>
                Prediction Results</div>
        """, unsafe_allow_html=True)

        filter_opt = st.radio("Filter by risk level",
                              ["All", "HIGH", "MEDIUM", "LOW"],
                              horizontal=True,
                              label_visibility="collapsed")

        filtered = results if filter_opt == "All" else results[results['Risk Level'] == filter_opt]

        def style_risk(val):
            if val == 'HIGH':   return 'background:#3d1515;color:#f87171;border-radius:4px;padding:2px 8px;'
            if val == 'MEDIUM': return 'background:#3d2e10;color:#fbbf24;border-radius:4px;padding:2px 8px;'
            return 'background:#0f2e1a;color:#4ade80;border-radius:4px;padding:2px 8px;'

        st.dataframe(
            filtered.style.applymap(style_risk, subset=['Risk Level']),
            use_container_width=True,
            hide_index=True,
            height=400
        )
        st.markdown("</div>", unsafe_allow_html=True)

        csv_out = results.to_csv(index=False)
        c1, c2 = st.columns([1, 4])
        with c1:
            st.download_button(
                label="⬇ Download Results CSV",
                data=csv_out,
                file_name="attrition_predictions.csv",
                mime="text/csv",
                use_container_width=True
            )
        with c2:
            if st.button("↺ Upload another file", use_container_width=False):
                st.session_state.bulk_results = None
                st.rerun()
