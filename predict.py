import streamlit as st
from model import score_employee, get_risk_level, get_drivers, get_recommendation

def show():
    st.markdown("<h1 style='color:#1a1a1a;'>Single Employee Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#666;'>Enter employee details to get an instant attrition risk score</p>", unsafe_allow_html=True)

    form_col, result_col = st.columns([3, 2])

    with form_col:
        st.markdown("<span style='background:#1a1a1a;color:#FFD84D;font-size:10px;font-weight:700;padding:3px 10px;border-radius:4px;letter-spacing:2px;'>PERSONAL INFO</span>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        p1, p2 = st.columns(2)
        with p1:
            age = st.slider("Age", 18, 60, 32)
            marital = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
        with p2:
            gender = st.selectbox("Gender", ["Male", "Female"])
            education = st.selectbox("Education", ["Below College", "College", "Bachelor", "Master", "Doctor"], index=2)

        st.markdown("<br><span style='background:#1a1a1a;color:#FFD84D;font-size:10px;font-weight:700;padding:3px 10px;border-radius:4px;letter-spacing:2px;'>JOB DETAILS</span>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
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

        st.markdown("<br><span style='background:#1a1a1a;color:#FFD84D;font-size:10px;font-weight:700;padding:3px 10px;border-radius:4px;letter-spacing:2px;'>TENURE</span>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        t1, t2 = st.columns(2)
        with t1:
            years = st.slider("Years at Company", 0, 40, 2)
            years_mgr = st.slider("Years with Manager", 0, 17, 1)
        with t2:
            years_role = st.slider("Years in Current Role", 0, 18, 1)
            wlb = st.selectbox("Work-Life Balance", [1, 2, 3, 4],
                               format_func=lambda x: f"{x} — {'Bad' if x==1 else 'Good' if x==2 else 'Better' if x==3 else 'Best'}",
                               index=2)

        st.button("→ Predict Attrition Risk", use_container_width=True)

    with result_col:
        score = score_employee(overtime, travel, role, marital,
                               years, years_role, years_mgr,
                               income, wlb, dept)
        risk_level = get_risk_level(score)
        drivers = get_drivers(overtime, travel, role, income,
                              years, years_role, years_mgr, marital, wlb)
        rec = get_recommendation(risk_level)

        ring_color = '#f87171' if risk_level == 'HIGH' else '#fbbf24' if risk_level == 'MEDIUM' else '#4ade80'
        badge_bg   = '#3d1515' if risk_level == 'HIGH' else '#3d2e10' if risk_level == 'MEDIUM' else '#0f2e1a'

        # ── Risk score card using native Streamlit ──
        st.markdown("""
        <div style='background:#1a1a1a;border:1px solid #2a2a2a;
            border-radius:16px;padding:1.5rem;'>
            <div style='font-size:10px;color:#aaa;text-transform:uppercase;
                letter-spacing:1.5px;margin-bottom:1rem;'>Risk Assessment</div>
        </div>
        """, unsafe_allow_html=True)

        # Score display using metric
        st.metric(label="Attrition Risk Score", value=f"{score}%")

        # Progress bar
        st.progress(score / 100)

        # Risk level badge
        if risk_level == 'HIGH':
            st.error(f"🔴 HIGH RISK")
        elif risk_level == 'MEDIUM':
            st.warning(f"🟡 MEDIUM RISK")
        else:
            st.success(f"🟢 LOW RISK")

        st.divider()

        # Key drivers
        st.markdown("**Key Risk Drivers**")
        impact_emoji = {'HIGH': '🔴', 'MEDIUM': '🟡', 'LOW': '🟢'}
        if drivers:
            for name, level, desc in drivers:
                st.markdown(f"{impact_emoji[level]} **{name}**")
                st.caption(desc)
        else:
            st.caption("No significant risk factors detected.")

        st.divider()

        # Recommendation
        st.markdown("**💡 Recommendation**")
        st.info(rec)
