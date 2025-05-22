import streamlit as st
import hashlib
import json
import os

# --- MUST BE FIRST ---
st.set_page_config(page_title="Login – SehaTech", layout="centered")

# --- HIDE SIDEBAR ---
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- TRANSLATIONS ---
lang = st.session_state.get("lang", "en")
translations = {
    "en": {
        "title": "🔐 Login to SehaTech",
        "username": "Username",
        "password": "Password",
        "login": "Login",
        "signup": "Sign Up",
        "welcome": "Welcome back!",
        "new_user": "Create a new account",
        "user_exists": "User already exists!",
        "user_created": "Account created successfully!",
        "login_failed": "Incorrect username or password.",
        "empty_fields": "Please fill in all fields."
    },
    "fr": {
        "title": "🔐 Connexion à SehaTech",
        "username": "Nom d'utilisateur",
        "password": "Mot de passe",
        "login": "Connexion",
        "signup": "S'inscrire",
        "welcome": "Bon retour !",
        "new_user": "Créer un nouveau compte",
        "user_exists": "L'utilisateur existe déjà !",
        "user_created": "Compte créé avec succès !",
        "login_failed": "Nom d'utilisateur ou mot de passe incorrect.",
        "empty_fields": "Veuillez remplir tous les champs."
    },
    "ar": {
        "title": "🔐 تسجيل الدخول إلى سيهاتك",
        "username": "اسم المستخدم",
        "password": "كلمة المرور",
        "login": "تسجيل الدخول",
        "signup": "إنشاء حساب",
        "welcome": "مرحبًا بعودتك!",
        "new_user": "إنشاء حساب جديد",
        "user_exists": "المستخدم موجود بالفعل!",
        "user_created": "تم إنشاء الحساب بنجاح!",
        "login_failed": "اسم المستخدم أو كلمة المرور غير صحيحة.",
        "empty_fields": "يرجى ملء جميع الحقول."
    },
    "amz": {
        "title": "🔐 ⵜⵉⵏⵏⴰⵥⴰ ⴷ SehaTech",
        "username": "ⵉⵙⵎ ⵏ ⵓⵙⴻⵍⵍⵉ",
        "password": "ⴰⴷⴰⵙ ⵏ ⴰⵙⵙⵓ",
        "login": "ⴰⵏⵏⴰⵥ",
        "signup": "ⵙⵉⵏⵉ ⴰⵔⴰⵎ",
        "welcome": "ⴰⵎⵣⴰⵡ ⴰⵏⵙⵓⴽ!",
        "new_user": "ⴰⵎⵙⴰⵏ ⴰⵏⴰⵎⴰⵍ",
        "user_exists": "ⵓⵙⴻⵍⵍⵉ ⵉⴳ ⵓⵙⵏⵏⵉⵎ!",
        "user_created": "ⴰⵎⵙⴰⵏ ⵉⵙⵎⴰⵍ!",
        "login_failed": "ⵉⵙⵎ ⵓ ⴰⴷⴰⵙ ⵏ ⴰⵙⵙⵓ ⵓⵙⵏⵏⵉⵎ.",
        "empty_fields": "ⴰⴷⵔ ⴰⵎⵎⵓⵔ ⵏ ⵉⵏⵏⵓⵙⴰⵏ."
    }
}
t = translations[lang]

# --- TITLES ---
st.title(t["title"])
mode = st.radio("", [t["login"], t["signup"]], horizontal=True)

# --- INPUTS ---
username = st.text_input(t["username"])
password = st.text_input(t["password"], type="password")

# --- DATA FILES ---
USERS_FILE = "users.json"
PROFILES_FILE = "user_profiles.json"

# --- HELPERS ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(data):
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- BUTTON ACTION ---
if st.button(mode):
    if not username or not password:
        st.warning(t["empty_fields"])
    else:
        users = load_users()
        hashed_pw = hash_password(password)

        if mode == t["login"]:
            if username in users and users[username] == hashed_pw:
                st.success(f"{t['welcome']} {username} 👋")
                st.session_state["user"] = username

                # Load profile if exists
                if os.path.exists(PROFILES_FILE):
                    with open(PROFILES_FILE, "r") as f:
                        profiles = json.load(f)
                    if username in profiles:
                        st.session_state["user_profile"] = profiles[username]

                st.switch_page("pages/1_User_Info.py")
            else:
                st.error(t["login_failed"])

        elif mode == t["signup"]:
            if username in users:
                st.error(t["user_exists"])
            else:
                users[username] = hashed_pw
                save_users(users)
                st.success(t["user_created"])
