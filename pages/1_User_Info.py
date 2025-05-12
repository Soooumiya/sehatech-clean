import streamlit as st

# --- Use selected language from session ---
lang = st.session_state.get("lang", "en")

# --- Translations for this page ---
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
        "saved": "✅ Profile saved! Redirecting to Dashboard...",
        "gender_options": ["Male", "Female"],
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
        "saved": "✅ Profil enregistré ! Redirection vers le tableau de bord...",
        "gender_options": ["Homme", "Femme"],
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
        "saved": "✅ تم حفظ الملف! سيتم التوجيه إلى لوحة التحكم...",
        "gender_options": ["ذكر", "أنثى"],
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
        "saved": "✅ ⵉⵎⵙⵙⴰⵏ ⵏ ⵜⵉⴼⵓⵙⵜ! ⴰⵎⴻⵏⵉ ⴰⵏⵓ ⴰⴷ ⵜⴰⵎⵓⵔⵜ...",
        "gender_options": ["ⴰⵎⴰⵣ", "ⵜⴰⵎⴰⵣⵜ"],
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

# Load selected language
l = languages[lang]

st.set_page_config(page_title=l["title"], layout="centered")
st.title(l["title"])

# --- Validation Logic ---
def is_valid(profile):
    errors = []
    e = l["errors"]

    if not profile["name"].strip():
        errors.append(e["name"])
    if profile["age"] <= 0:
        errors.append(e["age"])
    if not profile["gender"]:
        errors.append(e["gender"])
    if profile["weight"] <= 0:
        errors.append(e["weight"])
    if profile["height"] <= 0:
        errors.append(e["height"])
    if not profile["allergies"].strip():
        errors.append(e["allergies"])
    if not profile["conditions"].strip():
        errors.append(e["conditions"])

    return errors

# --- Form UI ---
with st.form("user_info_form"):
    name = st.text_input(l["name"])
    age = st.number_input(l["age"], min_value=0, max_value=120, step=1)
    gender = st.selectbox(l["gender"], l["gender_options"])
    weight = st.number_input(l["weight"], min_value=0.0, max_value=300.0, step=0.5)
    height = st.number_input(l["height"], min_value=0.0, max_value=250.0, step=0.5)
    allergies = st.text_area(l["allergies"])
    conditions = st.text_area(l["conditions"])
    submitted = st.form_submit_button(l["next"])

if submitted:
    profile = {
        "name": name.strip(),
        "age": age,
        "gender": gender,
        "weight": weight,
        "height": height,
        "allergies": allergies.strip(),
        "conditions": conditions.strip()
    }

    errors = is_valid(profile)
    if errors:
        st.error(l["fix_errors"])
        for err in errors:
            st.write(f"🔴 {err}")
    else:
        st.session_state["user_profile"] = profile
        st.success(l["saved"])
        st.switch_page("pages/2_Dashboard.py")
