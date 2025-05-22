import streamlit as st
from PIL import Image
import os

# --- Language setup ---
LANG = st.session_state.get("lang", "en")

# --- Translations ---
LABELS = {
    "en": {
        "title": "💊 Medication Scanner",
        "name": "Enter medication name (optional)",
        "upload": "Upload or take a photo of medication",
        "upload_note": "(JPG, JPEG, PNG – Max 200MB)",
        "upload_tip": "📎 Use the button below to choose a file or drag it here.",
        "analyze": "🔍 Analyze",
        "results": "Medication Info",
        "none": "No known medication detected.",
        "logout": "🚪 Logout",
        "field_dosage": "💊 Dosage",
        "field_used_for": "✅ Used For",
        "field_not_for": "🚫 Not For",
        "field_notes": "📝 Notes"
    },
    "fr": {
        "title": "💊 Scanner de Médicament",
        "name": "Entrez le nom du médicament (optionnel)",
        "upload": "Téléchargez ou prenez une photo du médicament",
        "upload_note": "(JPG, JPEG, PNG – 200 Mo max)",
        "upload_tip": "📎 Utilisez le bouton ci-dessous ou faites glisser le fichier ici.",
        "analyze": "🔍 Analyser",
        "results": "Infos Médicament",
        "none": "Aucun médicament reconnu.",
        "logout": "🚪 Se déconnecter",
        "field_dosage": "💊 Posologie",
        "field_used_for": "✅ Utilisé pour",
        "field_not_for": "🚫 Ne convient pas à",
        "field_notes": "📝 Remarques"
    },
    "ar": {
        "title": "💊 ماسح الأدوية",
        "name": "أدخل اسم الدواء (اختياري)",
        "upload": "قم برفع أو التقاط صورة للدواء",
        "upload_note": "(JPG، JPEG، PNG – الحد الأقصى 200 ميجا بايت)",
        "upload_tip": "📎 استخدم الزر أدناه لاختيار ملف أو اسحبه هنا.",
        "analyze": "🔍 تحليل",
        "results": "معلومات الدواء",
        "none": "لم يتم التعرف على دواء معروف.",
        "logout": "🚪 تسجيل الخروج",
        "field_dosage": "💊 الجرعة",
        "field_used_for": "✅ يُستخدم لعلاج",
        "field_not_for": "🚫 غير مناسب لـ",
        "field_notes": "📝 ملاحظات"
    },
    "amz": {
        "title": "💊 ⵙⴽⴰⵏⴻⵔ ⵏ ⵜⵓⵙⵙⵓⵎⵜ",
        "name": "ⵓⵙⵏⵉ ⵏ ⵜⵓⵙⵙⵓⵎⵜ (ⴰⵎⵎⵓⵔ)",
        "upload": "ⵜⵉⵍⵍⵉ ⴰⴼⵓⵙ ⴰⴷ ⵓⵙⵙⵓⵎ ⵜⵓⵙⵙⵓⵎⵜ",
        "upload_note": "(JPG, JPEG, PNG – ⴰⵎⴷⴷⵓⵔ 200MB)",
        "upload_tip": "📎 ⴰⴼⵓⵙ ⵓⴷⵔ ⵉⵍⵍⵉ ⴰⴼⵓⵙ ⴰⴷ ⵜⵓⵙⵎⵜ ⴷ ⴰⵣⵓⵍ ⵏ ⵜⵉⵖⵉ.",
        "analyze": "🔍 ⴰⵙⵍⴻⵍ",
        "results": "ⵜⵓⵙⵙⵓⵎⵜ",
        "none": "ⵓⵙⵎⵎⵓⴹ ⵏ ⵜⵓⵙⵙⵓⵎⵜ ⵓⵙⵙⵓⵎ ⵓⴳⴰⵔ.",
        "logout": "🚪 ⴰⵙⴼⵓⵙ",
        "field_dosage": "💊 ⵜⵙⵉⵏⵜ",
        "field_used_for": "✅ ⴰⵣⵓⵍ ⵏ ⵜⴰⵎⵓⵙⵜ",
        "field_not_for": "🚫 ⵓⴷⵍ ⴷ ⵓⵎⵎⵓⵔ ⵏ ⴰⵙⴷⵔⴰⵏ",
        "field_notes": "📝 ⵉⵏⴻⵏⵜⵓⵙⵉⵏ"
    }
}

T = LABELS.get(LANG, LABELS["en"])

# --- Simulated multilingual medication info ---
def simulate_med_info(name, lang):
    name = name.lower().strip()

    amox = ["amoxicillin", "amoxicilline", "أموكسيسيلين", "ⴰⵎⵓⴽⵙⵉⵍⵉⵏ"]
    dolo = ["doliprane", "دوليبران", "ⴷⵓⵍⵉⴱⵔⴰⵏ", "paracetamol", "باراسيتامول"]

    if name in amox:
        return {
            "name": {
                "en": "Amoxicillin", "fr": "Amoxicilline", "ar": "أموكسيسيلين", "amz": "ⴰⵎⵓⴽⵙⵉⵍⵉⵏ"
            },
            "dosage": {
                "en": "500 mg every 8 hours or 875 mg every 12 hours.",
                "fr": "500 mg toutes les 8h ou 875 mg toutes les 12h.",
                "ar": "500 ملغ كل 8 ساعات أو 875 ملغ كل 12 ساعة.",
                "amz": "500 ⵎⵍⴳ ⴷ ⴽⵍ 8 ⵙⴰⵄⴰⵙ ⴰⵏⵏ 875 ⵎⵍⴳ ⴷ ⴽⵍ 12 ⵙⴰⵄⴰⵙ."
            },
            "used_for": {
                "en": "Respiratory infections, urinary tract infections, strep throat.",
                "fr": "Infections respiratoires, urinaires, angines.",
                "ar": "التهابات الجهاز التنفسي، المسالك البولية، والتهاب الحلق.",
                "amz": "ⵉⵏⴼⵉⴽⵉⵙⵉⵏ ⵏ ⵜⴰⵙⴱⴰⵙⵜ ⴰⵏⵜⴰⵎⵓⵙⵜ ⴰⴷ ⵜⵉⵙⵙⵓⵎⵜ."
            },
            "not_for": {
                "en": "People allergic to penicillin.",
                "fr": "Personnes allergiques à la pénicilline.",
                "ar": "الأشخاص الذين يعانون من حساسية تجاه البنسلين.",
                "amz": "ⴰⵎⵎⵓⵔ ⵏ ⵜⴰⵍⵍⴰⵍⵉⵏ ⵏ ⴱⵉⵏⵙⵉⵍⵉⵏ."
            },
            "notes": {
                "en": "Complete the full course even if symptoms improve.",
                "fr": "Terminez le traitement même si les symptômes s'améliorent.",
                "ar": "أكمل الدورة العلاجية حتى لو تحسنت الأعراض.",
                "amz": "ⴰⵎⴷⵔⴰⴹ ⴰⴳⵔⴰⴹ ⴰⵎⴰⵣⵉⵖ ⴳ ⵜⴰⵏⴰⵍⴰ."
            }
        }

    elif name in dolo:
        return {
            "name": {
                "en": "Doliprane (Paracetamol)", "fr": "Doliprane (Paracétamol)",
                "ar": "دوليبران (باراسيتامول)", "amz": "ⴷⵓⵍⵉⴱⵔⴰⵏ (ⴱⴰⵔⴰⵙⵉⵜⴰⵎⵓⵍ)"
            },
            "dosage": {
                "en": "500 mg to 1g every 4–6 hours. Max 4g/day.",
                "fr": "500 mg à 1g toutes les 4–6 heures. Max 4g/jour.",
                "ar": "500 ملغ إلى 1غ كل 4 إلى 6 ساعات. الحد الأقصى 4غ/اليوم.",
                "amz": "500 ⵎⵍⴳ ⵏ 1ⴳ ⴷ ⴽⵍ 4 ⴰⵏⵏ 6 ⵙⴰⵄⴰⵙ."
            },
            "used_for": {
                "en": "Fever, mild to moderate pain, headaches.",
                "fr": "Fièvre, douleurs légères à modérées, maux de tête.",
                "ar": "الحمى، الألم الخفيف إلى المتوسط، والصداع.",
                "amz": "ⵜⵉⵎⵓⵍⵍⴰⵢⵜ, ⴰⵎⵎⵓⵔ, ⵓⵣⵣⵉⵍ ⵏ ⵜⴰⴳⵍⴰⴷⵜ."
            },
            "not_for": {
                "en": "Liver disease, alcohol use, allergic reactions.",
                "fr": "Maladie du foie, alcool, réactions allergiques.",
                "ar": "مرض الكبد، الكحول، تفاعلات تحسسية.",
                "amz": "ⵜⵓⵙⵙⵓⵎⵜ ⵏ ⵓⵣⵣⵡⴰⵏ, ⴰⵍⴽⵓⵍ, ⵜⵉⵎⵓⵍⵍⴰⵢⵜ."
            },
            "notes": {
                "en": "Do not combine with other paracetamol products.",
                "fr": "Ne pas associer à d'autres produits contenant du paracétamol.",
                "ar": "لا تجمعه مع منتجات أخرى تحتوي على الباراسيتامول.",
                "amz": "ⵉⵎⵎⵓⵔ ⵏ ⵓⵣⵣⵡⴰⵏ ⴷ ⵓⴳⴷⵔⴰ ⴱⴰⵔⴰⵙⵉⵜⴰⵎⵓⵍ."
            }
        }

    return None

# --- Page Layout ---
st.set_page_config(page_title=T["title"], layout="centered")
st.markdown(f"## {T['title']}")

# Inputs
name_input = st.text_input(f"🔤 {T['name']}")
st.markdown(f"### 📤 {T['upload']} {T['upload_note']}")
st.markdown(f"<div style='color: gray; font-size: 0.85rem; margin-bottom: 6px;'>{T['upload_tip']}</div>", unsafe_allow_html=True)
image_file = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

# Analyze
if st.button(T["analyze"]):
    result = None
    if name_input:
        result = simulate_med_info(name_input, LANG)
    elif image_file:
        st.image(image_file, caption="🧾 Uploaded Image", use_column_width=True)
        filename_guess = os.path.splitext(image_file.name)[0]
        result = simulate_med_info(filename_guess, LANG)

    if result:
        st.success(f"🧾 {T['results']}: {result['name'][LANG]}")
        st.markdown(f"**{T['field_dosage']}**: {result['dosage'][LANG]}")
        st.markdown(f"**{T['field_used_for']}**: {result['used_for'][LANG]}")
        st.markdown(f"**{T['field_not_for']}**: {result['not_for'][LANG]}")
        st.markdown(f"**{T['field_notes']}**: {result['notes'][LANG]}")
    else:
        st.error(f"❌ {T['none']}")

# Logout
st.markdown("---")
if st.button(T["logout"]):
    st.session_state.clear()
    st.switch_page("app.py")
