import streamlit as st
import base64
import os

# ✅ MUST be the first Streamlit call
st.set_page_config(page_title="🚨 Emergency", layout="centered")

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
        st.error("❌ Missing siren.mp3 in /emergency folder.")

play_siren(SIREN_PATH)

# --- Custom Styles ---
st.markdown("""
    <style>
    body {
        background-color: #fff5f5;
    }

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
st.markdown('<div class="animated-msg">🚑 Please wait... ambulance is on the way.</div>', unsafe_allow_html=True)

# --- Ambulance GIF ---
if os.path.exists(GIF_PATH):
    st.image(GIF_PATH, use_container_width=True)
else:
    st.error("❌ Missing ambulance.gif in /emergency folder.")

# --- Phone Call Button (mobile native dialer) ---
st.markdown("""
    <div class="phone-button-container">
        <a href="tel:15">
            <button class="phone-button">📞 Call 15</button>
        </a>
    </div>
""", unsafe_allow_html=True)
