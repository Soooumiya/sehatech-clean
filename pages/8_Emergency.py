import streamlit as st
import base64
import os

# ✅ Set page config
st.set_page_config(page_title="🚨 Emergency", layout="centered")

# ✅ Get language from session state
lang = st.session_state.get("lang", "en")

# ✅ Translations for this page only
translations = {
    "en": {
        "waiting": "🚑 Please wait... ambulance is on the way.",
        "call": "📞 Call 15",
        "error_gif": "❌ Missing ambulance.gif in /emergency folder.",
        "error_audio": "❌ Missing siren.mp3 in /emergency folder."
    },
    "fr": {
        "waiting": "🚑 Veuillez patienter... l'ambulance arrive.",
        "call": "📞 Appeler le 15",
        "error_gif": "❌ Fichier ambulance.gif manquant dans le dossier /emergency.",
        "error_audio": "❌ Fichier siren.mp3 manquant dans le dossier /emergency."
    },
    "ar": {
        "waiting": "🚑 الرجاء الانتظار... سيارة الإسعاف في الطريق.",
        "call": "📞 اتصل بـ 15",
        "error_gif": "❌ ملف ambulance.gif غير موجود في مجلد /emergency.",
        "error_audio": "❌ ملف siren.mp3 غير موجود في مجلد /emergency."
    },
    "amz": {
        "waiting": "🚑 ⴰⵎⴰⵣⵉⵖ ⴰⵏⴼⵓⵙ... ⵉⵎⴱⵓⵍⴰⵙ ⵙⴻⵎⴰⵏ.",
        "call": "📞 ⵉⵙⵏⵉⴼ 15",
        "error_gif": "❌ ⵉⴳⵔⴰⵣ ambulance.gif ⵓⵙⴽⴽⵓⵙ ⴷ /emergency.",
        "error_audio": "❌ ⵉⴳⵔⴰⵣ siren.mp3 ⵓⵙⴽⴽⵓⵙ ⴷ /emergency."
    }
}

# ✅ Use selected translation
t = translations.get(lang, translations["en"])

# --- File Paths ---
GIF_PATH = "emergency/ambulance.gif"
SIREN_PATH = "emergency/siren.mp3"

# --- Play siren on load ---
def play_siren(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            st.markdown(f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """, unsafe_allow_html=True)
    else:
        st.error(t["error_audio"])

play_siren(SIREN_PATH)

# --- Custom Styles ---
st.markdown("""
    <style>
    .animated-msg {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        color: #dc2626;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.05); }
        100% { opacity: 1; transform: scale(1); }
    }
    .phone-button-container {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
    }
    .phone-button {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background-color: #dc2626;
        color: white;
        font-size: 28px;
        font-weight: bold;
        border: none;
        box-shadow: 0 0 40px rgba(255,0,0,0.7);
        cursor: pointer;
        animation: glow 1.8s infinite;
    }
    @keyframes glow {
        0% { box-shadow: 0 0 10px #dc2626; }
        50% { box-shadow: 0 0 30px #dc2626; }
        100% { box-shadow: 0 0 10px #dc2626; }
    }
    </style>
""", unsafe_allow_html=True)

# --- Animated Message ---
st.markdown(f'<div class="animated-msg">{t["waiting"]}</div>', unsafe_allow_html=True)

# --- Ambulance GIF ---
if os.path.exists(GIF_PATH):
    st.image(GIF_PATH, use_container_width=True)
else:
    st.error(t["error_gif"])

# --- Phone Call Button ---
st.markdown(f"""
    <div class="phone-button-container">
        <a href="tel:15">
            <button class="phone-button">{t["call"]}</button>
        </a>
    </div>
""", unsafe_allow_html=True)
