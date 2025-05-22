import streamlit as st
from PIL import Image
import base64
import os

# ─── 1. PAGE CONFIG ───────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SehaTech – Smart Health Assistant",
    layout="wide",
)

# ─── 2. HIDE STREAMLIT SIDEBAR ────────────────────────────────────────────────
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# ─── 3. TRANSLATIONS ──────────────────────────────────────────────────────────
languages = {
    "en": {
        "label": "🇺🇸 English",
        "tagline": "Your Health. One App.",
        "subtitle": "SehaTech brings smart care, anywhere.",
        "start": "Get Started",
        "choose_lang": "Choose Language",
        "footer": "© 2025 SehaTech. Created with ❤️ by Soumiya"
    },
    "fr": {
        "label": "🇫🇷 Français",
        "tagline": "Votre santé. Une seule application.",
        "subtitle": "SehaTech offre des soins intelligents, partout.",
        "start": "Commencer",
        "choose_lang": "Choisir la langue",
        "footer": "© 2025 SehaTech. Créé avec ❤️ par Soumiya"
    },
    "ar": {
        "label": "🇲🇦 العربية",
        "tagline": "صحتك. تطبيق واحد.",
        "subtitle": "سيهاتك تقدم رعاية ذكية في أي وقت وأي مكان.",
        "start": "ابدأ الآن",
        "choose_lang": "اختر اللغة",
        "footer": "© 2025 SehaTech. تم الإنشاء بمحبة بواسطة Soumiya"
    },
    "amz": {
        "label": "ⵣ Amazigh",
        "tagline": "ⵜⴰⵎⴰⵣⵉⵖⵜ ⵏ ⵓⵙⴻⵍⵍⵉⵏ",
        "subtitle": "ⵙⴻⵀⴰⵜⴻⴽ ⵓⴷⵔⴰⵏ ⵏ ⵓⵣⵔⴰⵡ ⴷ ⵉⴷⵔⴻⵏ ⵏ ⵜⴰⵎⴰⵣⵉⵖⵜ",
        "start": "ⴰⴼⴻⵙ",
        "choose_lang": "ⴰⴼⵓⵙ ⵜⵉⵣⵉⵏⵜ",
        "footer": "© 2025 ⵙⴻⵀⴰⵜⴻⴽ. ⵙⵉⵏⴰⴹ Soumiya"
    }
}

# ─── 4. SESSION DEFAULTS ─────────────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state["lang"] = "en"
lang = st.session_state["lang"]

# ─── 5. LANGUAGE SELECTBOX ────────────────────────────────────────────────────
lang_keys   = list(languages.keys())
lang_labels = [languages[k]["label"] for k in lang_keys]
selected_index = lang_keys.index(lang)
selected_label = st.selectbox(
    f"🌐 {languages['en']['choose_lang']}",
    lang_labels,
    index=selected_index,
    key="lang_selectbox",
    on_change=lambda: st.session_state.update(lang=lang_keys[lang_labels.index(st.session_state["lang_selectbox"])])
)
# update session_state["lang"] based on selection
st.session_state["lang"] = lang_keys[lang_labels.index(selected_label)]
l = languages[st.session_state["lang"]]

# ─── 6. CSS STYLING ───────────────────────────────────────────────────────────
st.markdown("""
    <style>
    .center-box {
        padding-top: 40px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .logo {
        width: 160px;
        animation: float-glow 4s ease-in-out infinite;
        filter: drop-shadow(0 0 6px #10b981aa);
    }
    @keyframes float-glow {
        0% { transform: translateY(0px); filter: drop-shadow(0 0 6px #10b981aa); }
        50% { transform: translateY(-10px); filter: drop-shadow(0 0 16px #10b981cc); }
        100% { transform: translateY(0px); filter: drop-shadow(0 0 6px #10b981aa); }
    }
    .title {
        font-size: 3rem;
        font-weight: 800;
        color: #10b981;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .tagline {
        font-size: 1.4rem;
        font-weight: 500;
        color: #0f766e;
        margin-top: 1rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #6b7280;
        margin-top: 0.5rem;
        margin-bottom: 2rem;
    }
    .typewriter {
        overflow: hidden;
        border-right: 2px solid #10b981;
        white-space: nowrap;
        width: 0;
        animation: typing 4s steps(40, end) forwards, blink 0.75s step-end infinite;
    }
    @keyframes typing { from { width: 0 } to { width: 100% } }
    @keyframes blink { 50% { border-color: transparent } }
    .stButton>button {
        background-color: #10b981;
        color: white;
        padding: 0.9rem 2.5rem;
        font-size: 1.1rem;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        animation: pulse-glow 2s infinite;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }
    @keyframes pulse-glow {
        0% { box-shadow: 0 0 5px #10b981; }
        50% { box-shadow: 0 0 20px #10b981, 0 0 30px #10b981; }
        100% { box-shadow: 0 0 5px #10b981; }
    }
    .footer {
        text-align: center;
        color: gray;
        margin-top: 4rem;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# ─── 7. MAIN UI ───────────────────────────────────────────────────────────────
st.markdown("<div class='center-box'>", unsafe_allow_html=True)

# logo
logo_path = "sehatech_logo.png"
if os.path.exists(logo_path):
    img_b64 = base64.b64encode(open(logo_path, "rb").read()).decode()
    st.markdown(f"<img class='logo' src='data:image/png;base64,{img_b64}'/>", unsafe_allow_html=True)

st.markdown(f"<div class='title'>🏥 SehaTech</div>", unsafe_allow_html=True)
st.markdown(f"<div class='tagline'>{l['tagline']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle typewriter'>{l['subtitle']}</div>", unsafe_allow_html=True)

# Get Started button
if st.button(l["start"]):
    st.switch_page("pages/0_Login.py")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown(f"<div class='footer'>{l['footer']}</div>", unsafe_allow_html=True)
