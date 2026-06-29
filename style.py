import streamlit as st

def load_css():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #F5F0E8; }
    [data-testid="stMain"] { background-color: #F5F0E8; }
    .main .block-container { background-color: #F5F0E8; padding-top: 2rem; }

    [data-testid="stSidebar"] {
        background-color: #1a1a1a !important;
        border-right: 2px solid #FFD84D !important;
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] div { color: #cccccc !important; }
    [data-testid="stSidebar"] .stRadio label {
        color: #cccccc !important; font-size: 13px !important;
    }
    .stRadio > div { gap: 4px; }

    p, li { color: #1a1a1a; }
    div[style*="color:#555"] { color: #aaaaaa !important; }
    div[style*="color:#666"] { color: #aaaaaa !important; }
    div[style*="color:#444"] { color: #aaaaaa !important; }
    h1, h2, h3, h4 { color: #1a1a1a !important; }
    label { color: #1a1a1a !important; }

    .stButton > button {
        background: #FFD84D !important; color: #1a1a1a !important;
        border: none !important; border-radius: 10px !important;
        font-weight: 800 !important; font-size: 14px !important;
        padding: 0.7rem 2rem !important;
    }
    .stButton > button:hover { background: #f5cc30 !important; }
    .stSlider > div > div { background: #FFD84D !important; }
    .stSelectbox > div > div {
        background: #fff !important; border: 1px solid #ddd !important;
        color: #1a1a1a !important; border-radius: 8px !important;
    }
    [data-testid="stFileUploader"] {
        background: #fff !important; border: 2px dashed #ccc !important;
        border-radius: 12px !important; color: #1a1a1a !important;
    }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    [data-testid="collapsedControl"] { display: none !important; }
    section[data-testid="stSidebar"] > div { min-width: 200px !important; }
    </style>
    """, unsafe_allow_html=True)
