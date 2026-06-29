import streamlit as st

st.set_page_config(
    page_title="AttritionIQ",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

import landing, dashboard, predict, bulk_upload
import style

style.load_css()

PAGES = {
    "Home": landing,
    "Dashboard": dashboard,
    "Predict": predict,
    "Bulk Upload": bulk_upload,
}

with st.sidebar:
    st.markdown("""
        <div style='padding:0.5rem 0 1.5rem;'>
            <span style='font-size:20px;font-weight:800;color:#fff;letter-spacing:1px;'>
                ⬡ <span style='color:#FFD84D;'>ATTRITION</span>IQ
            </span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size:10px;color:#555;text-transform:uppercase;letter-spacing:2px;margin-bottom:0.3rem;'>Main</p>", unsafe_allow_html=True)
    page = st.radio(
        label="Navigation",
        options=list(PAGES.keys()),
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='font-size:10px;color:#444;border-top:1px solid #2a2a2a;padding-top:1rem;line-height:1.7;'>
            IBM HR Analytics Dataset<br>
            Logistic Regression Model<br>
            Data Science Internship · 2026
        </div>
    """, unsafe_allow_html=True)

PAGES[page].show()
