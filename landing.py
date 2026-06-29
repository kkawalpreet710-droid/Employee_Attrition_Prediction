import streamlit as st

def show():
    st.markdown("""
    <div style='text-align:center;padding:3rem 1rem 2rem;'>
        <div style='display:inline-block;background:#FFD84D;color:#1a1a1a;
            font-size:11px;font-weight:700;padding:5px 16px;border-radius:20px;
            letter-spacing:2px;text-transform:uppercase;margin-bottom:1.5rem;'>
            AI-Powered HR Intelligence
        </div>
        <h1 style='font-size:3.5rem;font-weight:900;line-height:1.05;
            letter-spacing:-2px;text-transform:uppercase;color:#1a1a1a;
            margin-bottom:1rem;'>
            PREDICT WHO LEAVES<br>
            <span style='background:#FFD84D;color:#1a1a1a;
                padding:0 0.15em;border-radius:4px;'>BEFORE</span>
            THEY RESIGN
        </h1>
        <p style='font-size:1.1rem;color:#444;max-width:500px;
            margin:0 auto 2rem;line-height:1.6;'>
            Turn your HR data into actionable retention insights.
            Know which employees are at risk — weeks before they hand in their notice.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    metrics = [
        ("1,470", "Employees Analysed", "#fff"),
        ("16.1%", "Attrition Rate", "#f87171"),
        ("59%", "Model Recall", "#FFD84D"),
        ("3", "Models Compared", "#4ade80"),
    ]
    for col, (val, label, color) in zip([c1, c2, c3, c4], metrics):
        with col:
            st.markdown(f"""
            <div style='background:#1a1a1a;border:1px solid #2a2a2a;border-radius:12px;
                padding:1.2rem;text-align:center;'>
                <div style='font-size:28px;font-weight:800;color:{color};'>{val}</div>
                <div style='font-size:11px;color:#aaaaaa;text-transform:uppercase;
                    letter-spacing:1px;margin-top:6px;'>{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style='background:#FFD84D;border-radius:20px;padding:3rem 2.5rem;
        margin-bottom:1.5rem;'>
        <div style='font-size:10px;font-weight:700;letter-spacing:2px;
            text-transform:uppercase;color:#8a7200;margin-bottom:0.5rem;'>
            What you get
        </div>
        <div style='display:flex;justify-content:space-between;
            align-items:center;flex-wrap:wrap;gap:2rem;'>
            <h2 style='font-size:2rem;font-weight:900;text-transform:uppercase;
                color:#1a1a1a;line-height:1.1;margin:0;'>
                SEE THE RISK.<br>ACT BEFORE<br>IT'S TOO LATE.
            </h2>
            <div style='font-size:13px;color:#333;max-width:320px;line-height:1.8;'>
                Our Logistic Regression model — trained on IBM HR data — identifies
                the employees most likely to leave based on 10+ behavioural and
                structural factors. Use the sidebar to explore.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    f1, f2, f3, f4 = st.columns(4)
    features = [
        ("📊", "Live Dashboard", "Attrition rates by department, role, and salary — all in one view."),
        ("🔮", "Single Prediction", "Enter one employee's details and get an instant risk score."),
        ("📁", "Bulk Upload", "Upload your full HR CSV and download risk scores for everyone."),
        ("💡", "Top Risk Factors", "See which features drive attrition most in your organisation."),
    ]
    for col, (icon, title, desc) in zip([f1, f2, f3, f4], features):
        with col:
            st.markdown(f"""
            <div style='background:#1a1a1a;border:1px solid #2a2a2a;border-radius:14px;
                padding:1.4rem;height:170px;'>
                <div style='font-size:24px;margin-bottom:0.6rem;'>{icon}</div>
                <div style='font-size:12px;font-weight:700;color:#ffffff;
                    text-transform:uppercase;letter-spacing:0.5px;
                    margin-bottom:0.4rem;'>{title}</div>
                <div style='font-size:11px;color:#aaaaaa;line-height:1.5;'>{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style='background:#1a1a1a;border-radius:16px;padding:2rem 2.5rem;'>
        <div style='font-size:10px;color:#FFD84D;text-transform:uppercase;
            letter-spacing:2px;margin-bottom:0.5rem;font-weight:700;'>How it works</div>
        <h3 style='font-size:1.4rem;font-weight:900;text-transform:uppercase;
            color:#ffffff;margin-bottom:1.5rem;'>THREE STEPS. ZERO GUESSWORK.</h3>
    </div>
    """, unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3)
    steps = [
        ("01", "Upload your HR data", "Drop in your employee CSV or use the sample IBM dataset to explore instantly."),
        ("02", "Model predicts attrition", "Logistic Regression scores each employee's risk based on 10+ key factors."),
        ("03", "HR takes targeted action", "Download results and prioritise who needs a retention conversation first."),
    ]
    for col, (num, title, desc) in zip([s1, s2, s3], steps):
        with col:
            st.markdown(f"""
            <div style='background:#1a1a1a;border-top:2px solid #FFD84D;
                border-radius:0 0 12px 12px;padding:1.2rem;'>
                <div style='font-size:11px;color:#FFD84D;font-weight:700;
                    margin-bottom:0.4rem;'>{num}</div>
                <div style='font-size:13px;font-weight:700;color:#ffffff;
                    text-transform:uppercase;margin-bottom:0.4rem;'>{title}</div>
                <div style='font-size:11px;color:#aaaaaa;line-height:1.5;'>{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;padding:2rem;'>
        <h2 style='font-size:2.5rem;font-weight:900;text-transform:uppercase;
            color:#1a1a1a;margin-bottom:0.5rem;'>STOP LOSING GREAT PEOPLE.</h2>
        <p style='color:#444;'>Use the sidebar to open the Dashboard or start predicting.</p>
    </div>
    """, unsafe_allow_html=True)
