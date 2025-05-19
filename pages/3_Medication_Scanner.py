import streamlit as st
from PIL import Image
import os

# --- Get current language (only for translating warning) ---
LANG = st.session_state.get("lang", "en")

# --- Translated Warning Text ---
WARNINGS = {
    "en": "⚠️ This page cannot be automatically translated due to medical image and text processing.",
    "fr": "⚠️ Cette page ne peut pas être traduite automatiquement à cause du traitement d'image et de texte médical.",
    "ar": "⚠️ لا يمكن ترجمة هذه الصفحة تلقائيًا بسبب معالجة الصور والنصوص الطبية.",
    "amz": "⚠️ ⵜⵉⵎⵓⵍⵍⴰⵢⵜ ⵜⴰⵎⴰⵣⵉⵖⵜ ⴰⵎⵎⵓⵔ ⴷ ⴰⵙⵙⵓⵎⵜ ⵏ ⵜⵉⴷⵉⵙⵉⵏ."
}
WARNING_TEXT = WARNINGS.get(LANG, WARNINGS["en"])

# --- Static Labels (English only) ---
TITLE = "💊 Medication Scanner"
NAME_INPUT_LABEL = "Enter medication name (optional)"
UPLOAD_LABEL = "Upload or take a photo of medication"
ANALYZE_LABEL = "Analyze"
RESULTS_LABEL = "Medication Information"

# --- Simulated Drug Info Function (replace with real DB or API later) ---
def simulate_med_info(name):
    name = name.lower()
    if "doliprane" in name:
        return {
            "name": "Doliprane (Paracetamol)",
            "dosage": "500mg to 1g every 4-6 hours. Max 4g/day.",
            "used_for": "Fever, mild to moderate pain, headaches.",
            "not_for": "Liver disease, chronic alcohol use, allergic reactions.",
            "notes": "Do not combine with other paracetamol-containing products."
        }
    else:
        return None

# --- Page Layout ---
st.set_page_config(page_title=TITLE, layout="centered")
st.markdown(f"## {TITLE}")
st.warning(WARNING_TEXT)

# --- Inputs ---
name_input = st.text_input(f"🔤 {NAME_INPUT_LABEL}")
image_file = st.file_uploader(f"📤 {UPLOAD_LABEL}", type=["jpg", "jpeg", "png"])

# --- Button ---
if st.button(ANALYZE_LABEL):
    found = None

    # If user typed a name
    if name_input:
        found = simulate_med_info(name_input)

    # If user uploaded an image
    elif image_file:
        st.image(image_file, caption="🧾 Uploaded image", use_column_width=True)
        # Simulate OCR with filename (replace with real OCR later)
        filename_guess = os.path.splitext(image_file.name)[0]
        if "doliprane" in filename_guess.lower():
            found = simulate_med_info("doliprane")

    # Show result
    if found:
        st.success(f"{RESULTS_LABEL}: {found['name']}")
        st.markdown(f"**💊 Dosage**: {found['dosage']}")
        st.markdown(f"**✅ Used For**: {found['used_for']}")
        st.markdown(f"**🚫 Not For**: {found['not_for']}")
        st.markdown(f"**📝 Notes**: {found['notes']}")
    else:
        st.error("❌ Medication not recognized. Try typing the name or using a clearer photo.")
