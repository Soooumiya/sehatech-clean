import streamlit as st
import random

# --- Get selected language ---
lang = st.session_state.get("lang", "en")

# --- Language dictionary ---
translations = {
    "en": {
        "welcome": "Welcome",
        "tagline": "Your smart health hub — everything in one place.",
        "summary": "📋 My Health Summary",
        "age": "🎂 Age",
        "weight": "⚖️ Weight",
        "height": "📏 Height",
        "conditions": "🧬 Conditions",
        "allergies": "🌿 Allergies",
        "tip_title": "🩺 Health Tip",
        "tips": [
            "💧 Stay hydrated. Drink 6–8 glasses of water a day.",
            "🚶‍♂️ Walk at least 30 minutes daily to stay active.",
            "🥗 Eat more whole foods and fiber.",
            "🧘 Manage stress with relaxation or breathing.",
            "🕒 Take your meds on time – build a routine.",
            "🛌 Sleep 7–8 hours for better focus and recovery.",
            "🧴 Use sunscreen daily, even on cloudy days.",
            "📆 Schedule regular checkups for prevention."
        ],
        "features": {
            "scan": ["Scan Medication", "Use your camera to scan pills or prescriptions."],
            "symptom": ["Symptom Checker", "Describe symptoms to receive suggestions."],
            "telemed": ["Telemedicine", "Connect with certified doctors instantly."],
            "nearby": ["Nearby Services", "Find hospitals and pharmacies near you."],
            "records": ["Health Records", "Coming soon: All your medical history in one place."],
            "mental": ["Mental Health", "Coming soon: Emotional support and mental well-being."],
            "emergency": ["Emergency Help", "Call emergency services in one tap."]
        }
    },
    "fr": {
        "welcome": "Bienvenue",
        "tagline": "Votre centre de santé intelligent — tout en un seul endroit.",
        "summary": "📋 Mon résumé de santé",
        "age": "🎂 Âge",
        "weight": "⚖️ Poids",
        "height": "📏 Taille",
        "conditions": "🧬 Problèmes de santé",
        "allergies": "🌿 Allergies",
        "tip_title": "🩺 Conseil santé",
        "tips": [
            "💧 Buvez 6 à 8 verres d’eau par jour.",
            "🚶‍♂️ Marchez 30 minutes par jour.",
            "🥗 Mangez plus de fibres et d'aliments complets.",
            "🧘 Gérez le stress avec la relaxation.",
            "🕒 Prenez vos médicaments à l’heure.",
            "🛌 Dormez 7 à 8 heures chaque nuit.",
            "🧴 Utilisez de la crème solaire tous les jours.",
            "📆 Faites des bilans de santé réguliers."
        ],
        "features": {
            "scan": ["Scanner un médicament", "Utilisez l’appareil photo pour scanner des médicaments."],
            "symptom": ["Vérificateur de symptômes", "Décrivez vos symptômes pour obtenir des suggestions."],
            "telemed": ["Téléconsultation", "Contactez un médecin certifié."],
            "nearby": ["Services à proximité", "Trouvez un hôpital ou une pharmacie proche."],
            "records": ["Dossiers médicaux", "Bientôt : votre historique médical complet."],
            "mental": ["Santé mentale", "Bientôt : soutien émotionnel et bien-être."],
            "emergency": ["Aide d'urgence", "Appelez les urgences rapidement."]
        }
    },
    "ar": {
        "welcome": "مرحبًا",
        "tagline": "مركزك الصحي الذكي — كل شيء في مكان واحد.",
        "summary": "📋 ملخص حالتي الصحية",
        "age": "🎂 العمر",
        "weight": "⚖️ الوزن",
        "height": "📏 الطول",
        "conditions": "🧬 الحالات",
        "allergies": "🌿 الحساسية",
        "tip_title": "🩺 نصيحة صحية",
        "tips": [
            "💧 اشرب 6 إلى 8 أكواب من الماء يوميًا.",
            "🚶‍♂️ امشِ لمدة 30 دقيقة يوميًا.",
            "🥗 تناول أطعمة كاملة وغنية بالألياف.",
            "🧘 قلل التوتر من خلال التأمل أو التنفس العميق.",
            "🕒 تناول الأدوية في مواعيدها.",
            "🛌 نم 7–8 ساعات يوميًا.",
            "🧴 استخدم واقي الشمس يوميًا.",
            "📆 قم بفحوصات طبية دورية."
        ],
        "features": {
            "scan": ["مسح الدواء", "استخدم الكاميرا لمسح الأدوية أو الوصفات."],
            "symptom": ["فحص الأعراض", "صف أعراضك للحصول على اقتراحات."],
            "telemed": ["الرعاية عن بُعد", "تواصل مع طبيب معتمد فورًا."],
            "nearby": ["خدمات قريبة", "ابحث عن مستشفيات وصيدليات قريبة."],
            "records": ["السجلات الصحية", "قريبًا: كل تاريخك الطبي في مكان واحد."],
            "mental": ["الصحة النفسية", "قريبًا: دعم عاطفي ورفاهية نفسية."],
            "emergency": ["مساعدة طارئة", "اتصل بالطوارئ بضغطة واحدة."]
        }
    },
    "amz": {
        "welcome": "ⴰⵏⴼⵓⵙ",
        "tagline": "ⴰⴳⵔⴰⴷ ⵏ ⵜⴰⵎⴰⵣⵉⵖⵜ — ⴰⴷⴷⵔⴰⴷ ⵏ ⵓⵙⴻⵍⵍⵉⵏ.",
        "summary": "📋 ⵜⴰⵙⵓⵏⵜ ⵏ ⵓⵙⴻⵍⵍⵉⵏ",
        "age": "🎂 ⵙⵉⵙ",
        "weight": "⚖️ ⵉⴷⵉⵙⵉ",
        "height": "📏 ⴰⵖⵔⴰⵡ",
        "conditions": "🧬 ⵉⵙⴻⵎⴷⴷⵉⵏ",
        "allergies": "🌿 ⴰⵣⵍⴰⵡ",
        "tip_title": "🩺 ⵜⵉⵙⴳⵉ ⵏ ⵓⵙⴻⵍⵍⵉⵏ",
        "tips": [
            "💧 ⵉⵙ ⵉⵙⴰⵎ ⵏ ⴰⴷⵔ ⴰⴽⴰⵔ ⴷ 6-8 ⴰⴳⵔⴰⵣ ⵏ ⵎⴰⵡⵉ.",
            "🚶‍♂️ ⴰⵎⵙⵙ ⵏ 30 ⵜⴰⵙⴳⵉⵏ ⵓⵎⵙⴷⵉ.",
            "🥗 ⴰⴷⵔ ⵉⵙⵉ ⵏ ⵉⴷⴷⵉⵙⴻⵏ ⴷ ⵉⵏⵏⵓⵙⵉⵏ.",
            "🧘 ⴰⴷⵔ ⵉⴳⵔ ⴰⵎⵎⵓⵔ ⵓ ⵏⵏⵓⵙⵉ.",
            "🕒 ⴰⴷⵔ ⵓⵙⴻⵎⴷⴷⵉⵏ ⵏ ⵜⴰⵏⵎⴰⵙⵜ.",
            "🛌 ⵉⵙ ⴰⵎⵙⵙ ⴷ 7–8 ⵜⴰⵙⴳⵉⵏ.",
            "🧴 ⴰⴷⵔ ⵓⴳⵔⴰⵣ ⵏ ⵓⵎⴰⵢ ⵉⴳⴳⴰ.",
            "📆 ⵉⵙ ⴰⴷⵔ ⵜⴰⵎⵓⵔⵜ ⴷ ⴰⴳⴳⵓⴹ ⴷ ⵜⵉⵙⴳⵉⵏ."
        ],
        "features": {
            "scan": ["ⴰⵙⵎⵎⵓⵙ ⵏ ⵉⵙⴻⵎⴷⴷⵉⵏ", "ⴰⴷⵔ ⵜⵉⵏⴳⵉ ⴷ ⵓⴽⴽⵓⵙ ⵏ ⵜⵉⵙⴻⵎⴷⴷⵉⵏ."],
            "symptom": ["ⴼⵙⵙ ⵏ ⵉⵙⵙⵓⵎⴰⵏ", "ⴰⴷⵔ ⵉⵙⵙⵓⵎⴰⵏ ⵓ ⵜⵙⵙⴰⵏⵜ ⴷ ⴰⵎⴰⵣⵉⵖⵜ."],
            "telemed": ["ⴰⵎⴻⵏⵙⴰ ⴷ ⵜⵙⴰⵏⵜ", "ⴰⴷⵔ ⴰⴷⴷⵓⵔ ⴷ ⴰⵎⵎⵓⵔ ⵏ ⴰⵎⴻⵏⵙⴰ."],
            "nearby": ["ⵉⵏⵏⴰⵡⵉⵏ ⵏ ⵜⵙⴰⵏⵜ", "ⴰⴷⵔ ⵎⴰⵙⴷⵉ ⵓ ⵎⵉⴽⴽⵓⴷⵉⵏ ⵓⴳⵓⴹⵉⵏ."],
            "records": ["ⴰⴳⴳⵓⴹ ⵏ ⵜⵙⴰⵏⵜ", "ⵓⵣⴰⵔ: ⴰⴷⴷⵔⴰⴷ ⵏ ⵙⴻⵀⴰⵜⴻⴽ."],
            "mental": ["ⵙⴻⵀⴰⵜⴻⵎ ⵏ ⵎⴰⵣⵉⵖⵜ", "ⵓⵣⴰⵔ: ⵓⵎⵎⵓⵔ ⵓ ⴰⵎⵎⵓⵔ ⴷ ⴰⴼⵓⵙ."],
            "emergency": ["ⴰⴱⵓⵍ ⵓⴷⵔⴰⴽ", "ⴰⴷⵔ ⵓⵙⵏⵉⴼ ⵉⵙ ⴷ ⵏⵓⵙⴰⵏ."]
        }
    }
}

# --- Page Setup ---
st.set_page_config(page_title="Dashboard", layout="wide")
t = translations[lang]

# --- Get user profile ---
user = st.session_state.get("user_profile", {
    "name": "User", "age": "", "weight": "", "height": "", "conditions": "", "allergies": ""
})

# --- Header ---
st.markdown(f"""
    <div style="background: linear-gradient(to right, #10b981, #059669); padding: 2rem; border-radius: 16px; color: white;">
        <h1 style="margin: 0;">{t['welcome']}, {user['name']} 👋</h1>
        <p style="margin: 0.3rem 0 0;">{t['tagline']}</p>
    </div>
""", unsafe_allow_html=True)

# --- Summary ---
with st.expander(t["summary"], expanded=True):
    col1, col2, col3 = st.columns(3)
    col1.metric(t["age"], user.get("age", "—"))
    col2.metric(t["weight"], f"{user.get('weight', '—')} kg")
    col3.metric(t["height"], f"{user.get('height', '—')} cm")
    col4, col5 = st.columns(2)
    col4.info(f"{t['conditions']}: {user.get('conditions', '—') or 'None'}")
    col5.warning(f"{t['allergies']}: {user.get('allergies', '—') or 'None'}")

# --- Tip ---
st.info(f"**{t['tip_title']}**\n\n{random.choice(t['tips'])}")

# --- Feature Cards ---
features = {
    "scan": ["fas fa-camera", "3_Medication_Scanner"],
    "symptom": ["fas fa-stethoscope", "3_Symptom_Checker"],
    "telemed": ["fas fa-video", "4_Telemedicine"],
    "nearby": ["fas fa-map-marker-alt", "5_Nearby_Services"],
    "records": ["fas fa-file-medical", None],
    "mental": ["fas fa-brain", None],
    "emergency": ["fas fa-ambulance", None]
}

st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        .feature-card {
            background: #fff;
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            text-align: center;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            cursor: pointer;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.1);
        }
        .feature-icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
            color: #10b981;
        }
        .feature-title {
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 0.3rem;
            color: #065f46;
        }
        .feature-desc {
            font-size: 0.85rem;
            color: #64748b;
        }
    </style>
""", unsafe_allow_html=True)

# --- Feature Grid ---
st.markdown('<div class="feature-grid">', unsafe_allow_html=True)
for key, (icon, page) in features.items():
    title, desc = t["features"][key]
    btn_key = f"btn_{key}"
    st.markdown(f"""
        <div class="feature-card" onclick="document.getElementById('{btn_key}').click()">
            <div class="feature-icon"><i class="{icon}"></i></div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{desc}</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("", key=btn_key):
        if page:
            st.switch_page(f"pages/{page}.py")
        elif key == "emergency":
            st.warning("📞 Please call your local emergency number.")
        else:
            st.info("🚧 This feature is coming soon.")
st.markdown('</div>', unsafe_allow_html=True)
