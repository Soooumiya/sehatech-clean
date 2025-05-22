
import streamlit as st
import json
import os

# 🌍 Get language from session or fallback to English
# Get language from session and normalize it
lang = st.session_state.get("lang", "en")

# Normalize alternative codes (e.g., from main page)
lang_aliases = {
    "amz": "tz",        # ISO code for Tamazight
    "amazigh": "tz",
    "tamazight": "tz"
}
lang = lang_aliases.get(lang, lang)


# Translations for UI strings
T = {
    "en": {
        "title": "🩺 Symptom Checker",
        "desc": "Select a **category**, then a symptom to get reliable info and advice.\n\n⚠️ This is not a medical diagnosis tool.",
        "choose_cat": "🏥 Choose a category",
        "choose_symptom": "🔍 Choose a symptom",
        "category": "Category",
        "description": "📖 Description",
        "advice": "🩹 Advice",
        "footer": "© 2025 SehaTech | Educational purpose only."
    },
    "fr": {
        "title": "🩺 Vérificateur de Symptômes",
        "desc": "Sélectionnez une **catégorie**, puis un symptôme pour des informations fiables.\n\n⚠️ Cet outil n'est pas un diagnostic médical.",
        "choose_cat": "🏥 Choisissez une catégorie",
        "choose_symptom": "🔍 Choisissez un symptôme",
        "category": "Catégorie",
        "description": "📖 Description",
        "advice": "🩹 Conseil",
        "footer": "© 2025 SehaTech | À but éducatif uniquement."
    },
    "ar": {
        "title": "🩺 فحص الأعراض",
        "desc": "اختر **فئة** ثم عرض للحصول على معلومات موثوقة.\n\n⚠️ هذا ليس تشخيصًا طبيًا.",
        "choose_cat": "🏥 اختر الفئة",
        "choose_symptom": "🔍 اختر العرض",
        "category": "الفئة",
        "description": "📖 الوصف",
        "advice": "🩹 النصيحة",
        "footer": "© 2025 SehaTech | للاستخدام التعليمي فقط."
    },
    "tz": {
        "title": "🩺 ⴼⵙⵙ ⵏ ⵉⵙⵙⵓⵎⴰⵏ",
        "desc": "ⴰⴷⵔ ⵜⴰⴳⵔⴰ ⴰⵏ ⵜⵉⵙⵙⵓⵎⴰⵏ ⵏ ⵏⴻⵎⴰⵍⵉⴷ ⵓⴷ ⵉⵙⵏⴰⵡⵉⵏ.\n\n⚠️ ⴰⵎⵙⵙⵓⵎ ⵙⴰ ⵓⵎⴰⴷⴰⵔ ⵏ ⵜⵉⵏⵏⴰⵡⵉⵏ.",
        "choose_cat": "🏥 ⴰⴷⵔ ⵜⴰⴳⵔⴰ",
        "choose_symptom": "🔍 ⴰⴷⵔ ⵜⵉⵙⵙⵓⵎⴰⵏ",
        "category": "ⵜⴰⴳⵔⴰ",
        "description": "📖 ⴰⵎⵙⵙⵉⵏ",
        "advice": "🩹 ⵓⵙⵙⵓⵎ",
        "footer": "© 2025 SehaTech | ⵉⵙⵙ ⵏ ⵜⵙⵙⴰⵏⵜ ⵜⴰⵎⵙⴰⵏⵜ."
    }
}[lang]

# Load JSON file
file_path = f"data/symptoms_{lang}_30.json"
if not os.path.exists(file_path):
    st.error(f"Translation file missing: {file_path}")
    st.stop()

with open(file_path, "r", encoding="utf-8") as f:
    symptoms_data = json.load(f)

# Setup page
st.set_page_config(page_title=T["title"], layout="centered")
st.markdown(f"<h1 style='text-align:center; color:green'>{T['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center'>{T['desc']}</p>", unsafe_allow_html=True)

# Get categories
categories = sorted(set(s["category"] for s in symptoms_data))
selected_category = st.selectbox(T["choose_cat"], categories)

# Get symptoms by category
filtered = [s for s in symptoms_data if s["category"] == selected_category]
symptoms = sorted([s["name"] for s in filtered])
selected_symptom = st.selectbox(T["choose_symptom"], symptoms)

# Show info
symptom = next((s for s in filtered if s["name"] == selected_symptom), None)
if symptom:
    st.markdown(f"### 🩺 {symptom['name']}")
    st.markdown(f"**{T['category']}:** {symptom['category']}")
    st.markdown(f"**{T['description']}**")
    st.info(symptom["description"])
    st.markdown(f"**{T['advice']}**")
    st.success(symptom["advice"])

st.markdown("---")
st.markdown(f"<p style='text-align:center'>{T['footer']}</p>", unsafe_allow_html=True)
# --- Ensure lang is defined (just in case)
lang = st.session_state.get("lang", "en")

# --- Logout translations
logout_labels = {
    "en": "🚪 Logout",
    "fr": "🚪 Se déconnecter",
    "ar": "🚪 تسجيل الخروج",
    "amz": "🚪 ⴰⵙⴼⵓⵙ"
}
logout_label = logout_labels.get(lang, "🚪 Logout")

# --- Logout Button ---
st.markdown("---")
if st.button(logout_label):
    st.session_state.clear()
    st.switch_page("app.py")
