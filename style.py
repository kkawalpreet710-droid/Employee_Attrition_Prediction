import streamlit as st

def load_css():
    st.markdown("""
    <style>
    /* ── Global ── */
    [data-testid="stAppViewContainer"] {
        background-color: #111111;
    }
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-right: 1px solid #2a2a2a;
    }
    [data-testid="stSidebar"] .stRadio label {
        color: #888 !important;
        font-size: 13px !important;
        padding: 6px 0;
    }
    [data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] p {
        color: #888;
        font-size: 13px;
    }
    .stRadio > div { gap: 4px; }

    /* ── Metric cards ── */
    .metric-card {
        background: #1a1a1a;
        border: 1px solid #2a2a2a;
        border-radius: 12px;
        padding: 1rem 1.2rem;
    }
    .metric-label {
        font-size: 10px;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 6px;
    }
    .metric-val {
        font-size: 26px;
        font-weight: 800;
        color: #fff;
    }
    .metric-sub { font-size: 11px; margin-top: 3px; }

    /* ── Chart card ── */
    .chart-card {
        background: #1a1a1a;
        border: 1px solid #2a2a2a;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
    }
    .chart-title {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #fff;
        margin-bottom: 3px;
    }
    .chart-sub { font-size: 10px; color: #555; margin-bottom: 1rem; }

    /* ── Risk badges ── */
    .badge-high {
        background: #3d1515; color: #f87171;
        font-size: 10px; font-weight: 700;
        padding: 3px 10px; border-radius: 20px;
        display: inline-block;
    }
    .badge-medium {
        background: #3d2e10; color: #fbbf24;
        font-size: 10px; font-weight: 700;
        padding: 3px 10px; border-radius: 20px;
        display: inline-block;
    }
    .badge-low {
        background: #0f2e1a; color: #4ade80;
        font-size: 10px; font-weight: 700;
        padding: 3px 10px; border-radius: 20px;
        display: inline-block;
    }

    /* ── Yellow CTA button ── */
    .stButton > button {
        background: #FFD84D !important;
        color: #1a1a1a !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 800 !important;
        font-size: 14px !important;
        padding: 0.7rem 2rem !important;
    }
    .stButton > button:hover {
        background: #f5cc30 !important;
    }

    /* ── Headings ── */
    h1, h2, h3 { color: #ffffff !important; }
    p, li { color: #aaaaaa; }

    /* ── Inputs ── */
    .stSlider > div > div { background: #FFD84D !important; }
    .stSelectbox > div > div {
        background: #1a1a1a !important;
        border: 1px solid #2a2a2a !important;
        color: #fff !important;
        border-radius: 8px !important;
    }

    /* ── Upload zone ── */
    .upload-zone {
        border: 2px dashed #2a2a2a;
        border-radius: 16px;
        padding: 3rem 2rem;
        text-align: center;
        background: #1a1a1a;
        margin-bottom: 1rem;
    }

    /* ── Hide Streamlit default chrome ── */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)
