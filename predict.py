import streamlit as st
from model import score_employee, get_risk_level, get_drivers, get_recommendation

def show():
    st.markdown("""
    <div style='margin-bottom:1.5rem;'>
        <h1 style='font-size:1.6rem;font-weight:800;color:#fff;margin:0;'>
            Single Employee Prediction
        </h1>
        <p style='font-size:11px;color:#555;margin-top:4px;'>
            Enter employee details to get an instant attrition risk score
        </p>
    </div>
    """, unsafe_allow_html=True)

    form_col, result_col = st.columns([3, 2])

    with form_col:
        st.markdown("""<div style='background:#1a1a1a;border:1px solid #2a2a2a;
            border-radius:12px;padding:1.5rem;'>""", unsafe_allow_html=True)

        st.markdown("<p style='font-size:10px;color:#FFD84D;text-transform:uppercase;letter-spacing:2px;border-bottom:1px solid #2a2a2a;padding-bottom:8px;'>Personal Info</p>", unsafe_allow_html=True)
        p1, p2 = st.columns(2)
        with p1:
            age = st.slider("Age", 18, 60, 32)
            marital = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
        with p2:
            gender = st.selectbox("Gender", ["Male", "Female"])
            education = st.selectbox("Education", ["Below College", "College", "Bachelor", "Master", "Doctor"], index=2)

        st.markdown("<p style='font-size:10px;color:#FFD84D;text-transform:uppercase;letter-spacing:2px;border-bottom:1px solid #2a2a2a;padding-bottom:8px;margin-top:1rem;'>Job Details</p>", unsafe_allow_html=True)
        j1, j2 = st.columns(2)
        with j1:
            dept = st.selectbox("Department", ["Research and Development", "Sales", "Human Resources"])
            job_level = st.selectbox("Job Level", ["1 — Entry", "2 — Junior", "3 — Mid", "4 — Senior", "5 — Director"], index=1)
            overtime = st.selectbox("Overtime", ["Yes", "No"])
        with j2:
            role = st.selectbox("Job Role", [
                "Sales Representative", "Laboratory Technician",
                "Human Resources", "Research Scientist",
                "Sales Executive", "Manager",
                "Manufacturing Director", "Research Director"
            ])
            travel = st.selectbox("Business Travel", ["Travel_Frequently", "Travel_Rarely", "Non-Travel"])
            income = st.slider("Monthly Income (₹)", 1000, 20000, 3500, step=100)

        st.markdown("<p style='font-size:10px;color:#FFD84D;text-transform:uppercase;letter-spacing:2px;border-bottom:1px solid #2a2a2a;padding-bottom:8px;margin-top:1rem;'>Tenure</p>", unsafe_allow_html=True)
        t1, t2 = st.columns(2)
        with t1:
            years = st.slider("Years at Company", 0, 40, 2)
            years_mgr = st.slider("Years with Manager", 0, 17, 1)
        with t2:
            years_role = st.slider("Years in Current Role", 0, 18, 1)
            wlb = st.selectbox("Work-Life Balance", [1, 2, 3, 4],
                               format_func=lambda x: f"{x} — {'Bad' if x==1 else 'Good' if x==2 else 'Better' if x==3 else 'Best'}",
                               index=2)

        predict_clicked = st.button("→ Predict Attrition Risk", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with result_col:
        score = score_employee(overtime, travel, role, marital,
                               years, years_role, years_mgr,
                               income, wlb, dept)
        risk_level = get_risk_level(score)
        drivers = get_drivers(overtime, travel, role, income,
                              years, years_role, years_mgr, marital, wlb)
        rec = get_recommendation(risk_level)

        ring_color = '#f87171' if risk_level == 'HIGH' else '#fbbf24' if risk_level == 'MEDIUM' else '#4ade80'
        badge_bg = '#3d1515' if risk_level == 'HIGH' else '#3d2e10' if risk_level == 'MEDIUM' else '#0f2e1a'
        circumference = 314
        offset = circumference - int((score / 100) * circumference)

        st.markdown(f"""
        <div style='background:#1a1a1a;border:1px solid #2a2a2a;
            border-radius:12px;padding:1.5rem;'>
            <div style='font-size:10px;color:#555;text-transform:uppercase;
                letter-spacing:1.5px;margin-bottom:1.2rem;'>Risk Assessment</div>

            <div style='text-align:center;margin-bottom:1.2rem;'>
                <svg width='130' height='130' viewBox='0 0 120 120'>
                    <circle cx='60' cy='60' r='50' fill='none'
                        stroke='#222' stroke-width='10'/>
                    <circle cx='60' cy='60' r='50' fill='none'
                        stroke='{ring_color}' stroke-width='10'
                        stroke-dasharray='314'
                        stroke-dashoffset='{offset}'
                        stroke-linecap='round'
                        transform='rotate(-90 60 60)'/>
                </svg>
                <div style='margin-top:-70px;margin-bottom:55px;'>
                    <div style='font-size:30px;font-weight:800;color:#fff;'>{score}%</div>
                    <div style='font-size:10px;color:#666;'>risk score</div>
                </div>
                <span style='background:{badge_bg};color:{ring_color};
                    font-size:11px;font-weight:700;padding:5px 18px;
                    border-radius:20px;'>{risk_level} RISK</span>
            </div>

            <div style='font-size:10px;color:#555;text-transform:uppercase;
                letter-spacing:1px;margin:1.2rem 0 0.8rem;'>Key risk drivers</div>
        """, unsafe_allow_html=True)

        impact_styles = {
            'HIGH': ('background:#3d1515;color:#f87171;', 'HIGH'),
            'MEDIUM': ('background:#3d2e10;color:#fbbf24;', 'MED'),
            'LOW': ('background:#1a2a1a;color:#4ade80;', 'LOW'),
        }

        if drivers:
            for name, level, desc in drivers:
                style, label = impact_styles[level]
                st.markdown(f"""
                <div style='display:flex;justify-content:space-between;
                    align-items:flex-start;padding:7px 0;
                    border-bottom:1px solid #222;'>
                    <div>
                        <div style='font-size:11px;color:#bbb;'>{name}</div>
                        <div style='font-size:10px;color:#444;margin-top:2px;'>{desc}</div>
                    </div>
                    <span style='{style}font-size:9px;font-weight:700;
                        padding:2px 8px;border-radius:20px;flex-shrink:0;
                        margin-left:8px;'>{label}</span>
                </div>""", unsafe_allow_html=True)
        else:
            st.markdown("<p style='font-size:11px;color:#444;'>No significant risk factors detected.</p>", unsafe_allow_html=True)

        st.markdown(f"""
            <div style='background:#111;border:1px solid #2a2a2a;
                border-radius:8px;padding:1rem;margin-top:1rem;'>
                <div style='font-size:10px;color:#FFD84D;text-transform:uppercase;
                    letter-spacing:1px;margin-bottom:6px;'>Recommendation</div>
                <div style='font-size:11px;color:#888;line-height:1.6;'>{rec}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
