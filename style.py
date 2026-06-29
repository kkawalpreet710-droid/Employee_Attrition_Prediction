import streamlit as st

def load_css():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #111111; }
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-right: 2px solid #FFD84D !important;
    }
    [data-testid="stSidebar"] * { color: #cccccc !important; }
    [data-testid="stSidebar"] .stRadio label {
        color: #cccccc !important;
        font-size: 13px !important;
    }
    .stRadio > div { gap: 4px; }
    p, li, span, div { color: #cccccc; }
    h1, h2, h3, h4 { color: #ffffff !important; }
    label { color: #cccccc !important; }
    .stButton > button {
        background: #FFD84D !important;
        color: #1a1a1a !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 800 !important;
        font-size: 14px !important;
        padding: 0.7rem 2rem !important;
    }
    .stButton > button:hover { background: #f5cc30 !important; }
    .stSlider > div > div { background: #FFD84D !important; }
    .stSelectbox > div > div {
        background: #1a1a1a !important;
        border: 1px solid #333 !important;
        color: #fff !important;
        border-radius: 8px !important;
    }
    [data-testid="stFileUploader"] {
        background: #1a1a1a !important;
        border: 2px dashed #333 !important;
        border-radius: 12px !important;
        color: #ccc !important;
    }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)
