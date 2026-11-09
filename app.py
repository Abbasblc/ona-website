"""Omani Nursing Association - website prototype preview (Streamlit).

Visitors enter an access code, then see the full bilingual (English/Arabic) prototype.
Set the code in Streamlit Cloud: App settings > Secrets:
    ACCESS_CODE = "your-code"
"""
import hmac
import os
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Omani Nursing Association | Website preview",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SITE = Path(__file__).parent / "site" / "index.html"


def access_code() -> str:
    try:
        return str(st.secrets["ACCESS_CODE"])
    except Exception:
        return os.environ.get("ACCESS_CODE", "")


@st.cache_data(show_spinner=False)
def load_site() -> str:
    return SITE.read_text(encoding="utf-8")


# Shared styling: hide Streamlit chrome, Omani heritage colours
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300;400;600&family=Reem+Kufi:wght@600&display=swap');
#MainMenu, header[data-testid="stHeader"], footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {display:none !important;}
html, body, [data-testid="stAppViewContainer"] {background:#FAF5EC;}
* {font-family:'Readex Pro', sans-serif;}
</style>
""",
    unsafe_allow_html=True,
)

if "ok" not in st.session_state:
    st.session_state.ok = False

code = access_code()

if not st.session_state.ok:
    st.markdown(
        """
<style>
.block-container {max-width:580px; padding-top:8vh;}
.gate {background:#FFFDF9; border:1px solid #E4D4BC; border-radius:18px; padding:30px 30px 10px;
       box-shadow:0 18px 40px -26px rgba(12,59,68,.55); position:relative; overflow:hidden; text-align:center;}
.gate:before {content:""; position:absolute; inset:0 0 auto 0; height:5px;
              background:linear-gradient(90deg,#0E6A6F,#1A9E86,#9C4F2E,#C8202A);}
.gate h1 {font-family:'Reem Kufi', sans-serif; color:#0C3B44; font-size:1.7rem; margin:.2rem 0 .1rem;}
.gate .ar {direction:rtl; font-family:'Reem Kufi', sans-serif; color:#0E6A6F; font-size:1.35rem; margin:0 0 .8rem;}
.gate p {color:#5B5148; margin:.2rem 0;}
.stButton > button, .stFormSubmitButton > button {background:#C8202A; color:#fff; border:0; border-radius:999px;
       padding:.55rem 1.6rem; font-weight:600; width:100%;}
.stButton > button:hover, .stFormSubmitButton > button:hover {background:#A3161F; color:#fff;}
.foot {text-align:center; color:#8A7D6E; font-size:.82rem; margin-top:1.4rem;}
</style>
<div class="gate">
  <h1>Omani Nursing Association</h1>
  <div class="ar">الجمعية العمانية للتمريض</div>
  <p>Website prototype · for review by the ONA board</p>
  <p dir="rtl">نموذج أولي للموقع · للمراجعة من مجلس إدارة الجمعية</p>
</div>
""",
        unsafe_allow_html=True,
    )
    if not code:
        st.error("Access code is not set. Add ACCESS_CODE in the app's Secrets. / لم يُضبط رمز الدخول بعد.")
        st.stop()
    with st.form("gate", clear_on_submit=False):
        entered = st.text_input(
            "Access code / رمز الدخول", type="password", placeholder="Enter the code you received / أدخل الرمز"
        )
        submitted = st.form_submit_button("Open the website / فتح الموقع")
    if submitted:
        if hmac.compare_digest(entered.strip(), code):
            st.session_state.ok = True
            st.rerun()
        else:
            st.error("Incorrect code. Please try again. / الرمز غير صحيح، حاول مرة أخرى.")
    st.markdown(
        '<div class="foot">© 2026 Omani Nursing Association · Powered by Knowledge Horizon</div>',
        unsafe_allow_html=True,
    )
    st.stop()

# ---------- the website, full screen ----------
st.markdown(
    """
<style>
.block-container {padding:0 !important; max-width:100% !important;}
[data-testid="stAppViewContainer"] > .main, section.main {padding:0 !important;}
[data-testid="stVerticalBlock"] {gap:0 !important;}
iframe {width:100% !important; height:100vh !important; border:0 !important; display:block;}
</style>
""",
    unsafe_allow_html=True,
)
components.html(load_site(), height=900, scrolling=True)
