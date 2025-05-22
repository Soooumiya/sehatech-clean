import streamlit as st
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Profile – SehaTech", layout="centered")

# --- HIDE SIDEBAR NAVIGATION ---
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- BLOCK UNAUTHORIZED USERS ---
if "user" not in st.session_state:
    st.error("❌ You must log in first.")
    st.stop()

username = st.session_state["user"]
lang = st.session_state.get("lang", "en")

# --- TRANSLATIONS ---
languages = {
    "en": {
        "title": "👤 Your Health Profile",
        "next": "Next ➡️",
        "name": "Full Name",
        "age": "Age",
        "gender": "Gender",
        "weight": "Weight (kg)",
        "height": "Height (cm)",
        "allergies": "Allergies (comma separated)",
        "conditions": "Known Health Conditions (or write 'None')",
        "fix_errors": "❌ Please fix the following:",
        "saved": "✅ Profile saved!",
        "gender_options": ["Male", "Female"],
        "logout": "🚪 Logout",
        "errors": {
            "name": "Name is required.",
            "age": "Please enter a valid age above 0.",
            "gender": "Gender selection is required.",
            "weight": "Please enter a valid weight.",
            "height": "Please enter a valid height.",
            "allergies": "Please enter allergies or write 'None'.",
            "conditions": "Please specify conditions or write 'None'."
        }
    },
    "fr": {
        "title": "👤 Votre Profil de Santé",
        "next": "Suivant ➡️",
        "name": "Nom Complet",
        "age": "Âge",
        "gender": "Sexe",
        "weight": "Poids (kg)",
        "height": "Taille (cm)",
        "allergies": "Allergies (séparées par des virgules)",
        "conditions": "Problèmes de santé connus (ou tapez 'Aucun')",
        "fix_errors": "❌ Veuillez corriger les éléments suivants :",
        "saved": "✅ Profil enregistré !",
        "gender_options": ["Homme", "Femme"],
        "logout": "🚪 Se déconnecter",
        "errors": {
            "name": "Le nom est requis.",
            "age": "Veuillez entrer un âge valide supérieur à 0.",
            "gender": "La sélection du sexe est requise.",
            "weight": "Veuillez entrer un poids valide.",
            "height": "Veuillez entrer une taille valide.",
            "allergies": "Veuillez indiquer les allergies ou tapez 'Aucun'.",
            "conditions": "Veuillez indiquer les problèmes ou tapez 'Aucun'."
        }
    },
    "ar": {
        "title": "👤 ملفك الصحي",
        "next": "التالي ➡️",
        "name": "الاسم الكامل",
        "age": "العمر",
        "gender": "الجنس",
        "weight": "الوزن (كجم)",
        "height": "الطول (سم)",
        "allergies": "الحساسية (مفصولة بفواصل)",
        "conditions": "الحالات الصحية المعروفة (أو اكتب 'لا يوجد')",
        "fix_errors": "❌ يرجى تصحيح ما يلي:",
        "saved": "✅ تم حفظ الملف!",
        "gender_options": ["ذكر", "أنثى"],
        "logout": "🚪 تسجيل الخروج",
        "errors": {
            "name": "الاسم مطلوب.",
            "age": "يرجى إدخال عمر صحيح أكبر من 0.",
            "gender": "يرجى تحديد الجنس.",
            "weight": "يرجى إدخال وزن صحيح.",
            "height": "يرجى إدخال طول صحيح.",
            "allergies": "يرجى تحديد الحساسية أو كتابة 'لا يوجد'.",
            "conditions": "يرجى تحديد الحالات أو كتابة 'لا يوجد'."
        }
    },
    "amz": {
        "title": "👤 ⵜⵉⴼⵓⵙⵜ ⵏ ⵓⵙⴻⵍⵍⵉⵏ",
        "next": "ⴰⴼⴻⵙ ➡️",
        "name": "ⴰⵎⵙⵉⴹ ⴰⴷⴷⵓⵔ",
        "age": "ⵙⵉⵙ",
        "gender": "ⵙⵉⴳ",
        "weight": "ⵉⴷⵉⵙⵉ (kg)",
        "height": "ⴰⵖⵔⴰⵡ (cm)",
        "allergies": "ⴰⵣⵍⴰⵡ (ⵉⵙⴻⵍⵍⵉⵏ ⴱ ⵜⵓⴱⵍⵉⵢⵉⵏ)",
        "conditions": "ⵉⵙⴻⵎⴷⴷⵉⵏ ⵏ ⵓⵙⴻⵍⵍⵉⵏ (ⵓⵙⴰⴽ 'ⵓⵙⵉⵏⴰⵡ')",
        "fix_errors": "❌ ⴰⴷⵔ ⴰⵎⵓⵍⴰⵍ ⵉⵙⴷⴰⵍ ⵏⴰ:",
        "saved": "✅ ⵉⵎⵙⵙⴰⵏ ⵏ ⵜⵉⴼⵓⵙⵜ!",
        "gender_options": ["ⴰⵎⴰⵣ", "ⵜⴰⵎⴰⵣⵜ"],
        "logout": "🚪 ⴰⵙⴼⵓⵙ",
        "errors": {
            "name": "ⴰⵎⵙⵉⴹ ⵉⴳ ⵏⵓⵎⵎⵓⵔ.",
            "age": "ⴰⴷⵔ ⴰⵙⴷⴰⵍ ⵉⵙⵉⵙ ⴷ ⵎⴰ ⵏ 0.",
            "gender": "ⵙⵉⴳ ⵉⴳ ⵏⵓⵎⵎⵓⵔ.",
            "weight": "ⴰⴷⵔ ⴰⵙⴷⴰⵍ ⵉⴷⵉⵙⵉ.",
            "height": "ⴰⴷⵔ ⴰⵙⴷⴰⵍ ⴰⵖⵔⴰⵡ.",
            "allergies": "ⴰⴷⵔ ⵉⵙⴰⵏ ⵉⵙⴻⵎⴷⴷⵉⵏ ⵓ ⴰⴼⵓⵙ 'ⵓⵙⵉⵏⴰⵡ'.",
            "conditions": "ⴰⴷⵔ ⵉⵙⴻⵎⴷⴷⵉⵏ ⵓ ⴰⴼⵓⵙ 'ⵓⵙⵉⵏⴰⵡ'."
        }
    }
}
l = languages[lang]

# --- Load profile if it exists ---
profile_path = "user_profiles.json"
profile_data = {}
if os.path.exists(profile_path):
    with open(profile_path, "r") as f:
        profiles = json.load(f)
        profile_data = profiles.get(username, {})

# --- FORM ---
st.title(l["title"])
with st.form("profile_form"):
    name = st.text_input(l["name"], value=profile_data.get("name", ""))
    age = st.number_input(l["age"], min_value=0, max_value=120, value=profile_data.get("age", 0))

    gender_value = profile_data.get("gender", "")
    gender_options = l["gender_options"]
    try:
        gender_index = gender_options.index(gender_value)
    except ValueError:
        gender_index = 0
    gender = st.selectbox(l["gender"], gender_options, index=gender_index)

    weight = st.number_input(l["weight"], min_value=0.0, max_value=300.0, value=profile_data.get("weight", 0.0))
    height = st.number_input(l["height"], min_value=0.0, max_value=250.0, value=profile_data.get("height", 0.0))
    allergies = st.text_area(l["allergies"], value=profile_data.get("allergies", ""))
    conditions = st.text_area(l["conditions"], value=profile_data.get("conditions", ""))

    submit = st.form_submit_button(l["next"])

# --- FORM PROCESSING ---
if submit:
    errors = []
    e = l["errors"]
    if not name.strip(): errors.append(e["name"])
    if age <= 0: errors.append(e["age"])
    if not gender: errors.append(e["gender"])
    if weight <= 0: errors.append(e["weight"])
    if height <= 0: errors.append(e["height"])
    if not allergies.strip(): errors.append(e["allergies"])
    if not conditions.strip(): errors.append(e["conditions"])

    if errors:
        st.error(l["fix_errors"])
        for err in errors:
            st.write(f"🔴 {err}")
    else:
        profile = {
            "name": name,
            "age": age,
            "gender": gender,
            "weight": weight,
            "height": height,
            "allergies": allergies,
            "conditions": conditions
        }

        # Save to file
        profiles[username] = profile
        with open(profile_path, "w") as f:
            json.dump(profiles, f, indent=4)

        # Save to session
        st.session_state["user_profile"] = profile
        st.success(l["saved"])
        st.switch_page("pages/2_Dashboard.py")

# --- LOGOUT BUTTON ---
st.markdown("---")
if st.button(l["logout"]):
    st.session_state.clear()
    st.switch_page("app.py")
