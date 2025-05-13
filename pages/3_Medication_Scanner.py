import streamlit as st
from PIL import Image

# Multilingual static content
LANG = st.session_state.get("language", "en")

WARNINGS = {
    "en": "⚠️ This page cannot be automatically translated due to medical image and text processing.",
    "fr": "⚠️ Cette page ne peut pas être traduite automatiquement à cause du traitement d'image et de texte médical.",
    "ar": "⚠️ لا يمكن ترجمة هذه الصفحة تلقائيًا بسبب معالجة الصور والنصوص الطبية.",
    "amz": "⚠️ ⵜⵉⵎⵓⵍⵍⴰⵢⵜ ⵜⴰⵎⴰⵣⵉⵖⵜ ⴰⵎⵎⵓⵔ ⴷ ⴰⵙⵙⵓⵎⵜ ⵏ ⵜⵉⴷⵉⵙⵉⵏ."
}

LABELS = {
    "en": {
        "title": "💊 Medication Scanner",
        "name": "Enter medication name (optional)",
        "upload": "Upload or take a photo of medication",
        "analyze": "Analyze",
        "results": "Medication Information"
    },
    "fr": {
        "title": "💊 Scanner de Médicament",
        "name": "Entrez le nom du médicament (optionnel)",
        "upload": "Téléchargez ou prenez une photo du médicament",
        "analyze": "Analyser",
        "results": "Informations sur le médicament"
    },
    "ar": {
        "title": "💊 ماسح الأدوية",
        "name": "أدخل اسم الدواء (اختياري)",
        "upload": "قم برفع أو التقاط صورة للدواء",
        "analyze": "تحليل",
        "results": "معلومات الدواء"
    },
    "amz": {
        "title": "💊 ⵙⴽⴰⵏⴻⵔ ⵏ ⵜⵓⵙⵙⵓⵎⵜ",
        "name": "ⵓⵙⵏⵉ ⵏ ⵜⵓⵙⵙⵓⵎⵜ (ⴰⵎⵎⵓⵔ)",
        "upload": "ⵜⵉⵍⵍⵉ ⴰⴼⵓⵙ ⴰⴷ ⵓⵙⵙⵓⵎ ⵜⵓⵙⵙⵓⵎⵜ",
        "analyze": "ⴰⵙⵍⴻⵍ",
        "results": "ⵜⵓⵙⵙⵓⵎⵜ: ⵜⴰⵎⵙⵙⵉⵏⵜ"
    }
}

T = LABELS.get(LANG, LABELS["en"])
W = WARNINGS.get(LANG, WARNINGS["en"])

# Medication simulation database
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

# Page layout
st.markdown(f"## {T['title']}")
st.warning(W)

# Input
name_input = st.text_input(f"🔤 {T['name']}")
image_file = st.file_uploader(f"📤 {T['upload']}", type=["jpg", "jpeg", "png"])

# Button
if st.button(T["analyze"]):
    found = None
    if name_input:
        found = simulate_med_info(name_input)
    elif image_file:
        st.image(image_file, caption="🧾 Uploaded image", use_column_width=True)
        if "doliprane" in image_file.name.lower():
            found = simulate_med_info("doliprane")

    if found:
        st.success(f"{T['results']}: {found['name']}")
        st.markdown(f"**💊 Dosage**: {found['dosage']}")
        st.markdown(f"**✅ Used For**: {found['used_for']}")
        st.markdown(f"**🚫 Not For**: {found['not_for']}")
        st.markdown(f"**📝 Notes**: {found['notes']}")
    else:
        st.error("❌ Medication not recognized. Try typing the name or using a clearer photo.")
