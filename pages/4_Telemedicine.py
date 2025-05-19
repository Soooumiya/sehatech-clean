import streamlit as st
import json

# --- Page setup ---
st.set_page_config(page_title="SehaTech - Doctors", layout="wide")

# --- Use selected language from session state ---
lang = st.session_state.get("lang", "en")

# --- Load multilingual doctor data ---
with open("doctors_translated_multilang.json", "r") as f:
    doctors = json.load(f)

# --- UI Translations ---
ui = {
    "title": {
        "en": "🩺 SehaTech - Find Your Doctor",
        "fr": "🩺 SehaTech - Trouvez votre médecin",
        "ar": "🩺 سيهاتك - ابحث عن طبيبك",
        "amz": "🩺 ⵙⴻⵀⴰⵜⴻⴽ - ⴰⵎⵙⵙⴰⵍⴰⴽ ⵜⴰⵙⵎⴰⵏⵜ"
    },
    "subtitle": {
        "en": "Filter doctors by specialty, language, and contact method.",
        "fr": "Filtrez les médecins par spécialité, langue et méthode de contact.",
        "ar": "فرز الأطباء حسب التخصص واللغة وطريقة الاتصال.",
        "amz": "ⴰⴼⵓⵙ ⵏ ⴰⵎⵙⵙⴰⵍⵉⵏ ⴰⵎⵓⴽⴰⵎⵓⵔ, ⵜⵉⵣⵉⵏⵜ ⴷ ⵓⵙⵙⴰⵏ ⵏ ⵓⴽⴰⵢ"
    },
    "filters": {
        "specialty": {
            "en": "🩺 Specialty",
            "fr": "🩺 Spécialité",
            "ar": "🩺 التخصص",
            "amz": "🩺 ⵜⵙⵉⵏⵜ"
        },
        "language": {
            "en": "🌐 Language",
            "fr": "🌐 Langue",
            "ar": "🌐 اللغة",
            "amz": "🌐 ⵜⵉⵣⵉⵏⵜ"
        },
        "contact": {
            "en": "📞 Contact Method",
            "fr": "📞 Méthode de contact",
            "ar": "📞 وسيلة الاتصال",
            "amz": "📞 ⴰⵣⵡⵓⵍ ⵏ ⵓⴽⴰⵢ"
        }
    },
    "pagination": {
        "en": "✅ Showing",
        "fr": "✅ Affichage de",
        "ar": "✅ عرض",
        "amz": "✅ ⴰⵎⵍⵍⵉ ⵏ"
    },
    "no_results": {
        "en": "No doctors match your filters.",
        "fr": "Aucun médecin ne correspond à vos filtres.",
        "ar": "لا يوجد أطباء يطابقون الفلاتر.",
        "amz": "ⴰⵎⵙⵙⴰⵍ ⴰⵎⴰ ⵓⵔ ⵜⴰⴼⵓⵙⵜ."
    },
    "contact_buttons": {
        "Video Call": {
            "en": "🎥 Video",
            "fr": "🎥 Vidéo",
            "ar": "🎥 فيديو",
            "amz": "🎥 ⵜⴰⵎⵎⵓⵔⵜ"
        },
        "WhatsApp": {
            "en": "💬 WhatsApp",
            "fr": "💬 WhatsApp",
            "ar": "💬 واتساب",
            "amz": "💬 ⵡⴰⵜⵙⴰⴱ"
        },
        "Email": {
            "en": "✉️ Email",
            "fr": "✉️ Courriel",
            "ar": "✉️ البريد الإلكتروني",
            "amz": "✉️ ⴰⵙⵉⵏⴰⵡ"
        },
        "Message": {
            "en": "📲 SMS",
            "fr": "📲 Message",
            "ar": "📲 رسالة",
            "amz": "📲 ⵜⴰⵙⵉⵏⵜ"
        }
    }
}

# --- CSS ---
st.markdown("""
    <style>
        .header { color: #0f766e; font-size: 2.5rem; font-weight: bold; text-align: center; }
        .subheader { color: #6b7280; text-align: center; font-size: 1rem; margin-bottom: 2rem; }
        .card { background: #ffffff; border-radius: 16px; padding: 1rem; margin-bottom: 1.5rem; border: 1px solid #e5e7eb; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
        .doc-img { width: 100%; height: 180px; object-fit: cover; border-radius: 12px; }
        .doc-name { font-weight: bold; font-size: 1.2rem; color: #065f46; margin-top: 0.5rem; }
        .doc-specialty { color: #089981; font-size: 0.95rem; }
        .status { font-size: 0.85rem; color: #059669; margin-bottom: 0.5rem; }
        .btn { padding: 6px 12px; text-decoration: none; border-radius: 999px; font-size: 0.8rem; margin: 4px 4px 0 0; display: inline-block; color: white; font-weight: 500; }
        .btn.video { background-color: #0d9488; }
        .btn.whatsapp { background-color: #25D366; }
        .btn.email { background-color: #2563eb; }
        .btn.sms { background-color: #6b7280; }
        .btn:hover { opacity: 0.9; }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown(f"<div class='header'>{ui['title'][lang]}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subheader'>{ui['subtitle'][lang]}</div>", unsafe_allow_html=True)

# --- Filters ---
specialties = sorted(set(doc["specialty"][lang] for doc in doctors))
languages = sorted(set(l for doc in doctors for l in doc["languages"][lang]))
contacts = sorted(set(c for doc in doctors for c in doc["contacts"][lang]))

col1, col2, col3 = st.columns(3)
with col1:
    selected_spec = st.selectbox(ui["filters"]["specialty"][lang], specialties)
with col2:
    selected_lang = st.selectbox(ui["filters"]["language"][lang], languages)
with col3:
    selected_contact = st.selectbox(ui["filters"]["contact"][lang], contacts)

# --- Filter logic ---
def match(doc):
    return (
        selected_spec == doc["specialty"][lang] and
        selected_lang in doc["languages"][lang] and
        selected_contact in doc["contacts"][lang]
    )

filtered = [doc for doc in doctors if match(doc)]

# --- Pagination ---
page_size = 9
total = len(filtered)
page = st.number_input("Page", 1, max(1, (total - 1) // page_size + 1), 1)
start_idx = (page - 1) * page_size
end_idx = start_idx + page_size
paged_docs = filtered[start_idx:end_idx]

st.markdown(f"### {ui['pagination'][lang]} {len(paged_docs)} / {total}")

# --- Display Cards ---
cols = st.columns(3)

for idx, doc in enumerate(paged_docs):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="card">
            <img src="{doc['image']}" class="doc-img" alt="{doc['name']}">
            <div class="doc-name">{doc['name']}</div>
            <div class="doc-specialty">🩺 {doc['specialty'][lang]}</div>
            <div class="status">🟢 {doc['status']}</div>
            <div>📞 {doc['phone']}</div>
            <div>🌍 {', '.join(doc['languages'][lang])}</div>
            <div style="margin-top: 0.6rem;">
        """, unsafe_allow_html=True)

        buttons = []
        for contact in doc["contacts"]["en"]:  # use English keys to link
            if contact == "Video Call":
                buttons.append(f"<a class='btn video' href='https://meet.jit.si/{doc['name'].replace(' ', '')}' target='_blank'>{ui['contact_buttons'][contact][lang]}</a>")
            elif contact == "WhatsApp":
                buttons.append(f"<a class='btn whatsapp' href='https://wa.me/{doc['phone'].replace('+', '')}' target='_blank'>{ui['contact_buttons'][contact][lang]}</a>")
            elif contact == "Email":
                buttons.append(f"<a class='btn email' href='mailto:{doc['email']}' target='_blank'>{ui['contact_buttons'][contact][lang]}</a>")
            elif contact == "Message":
                buttons.append(f"<a class='btn sms' href='sms:{doc['phone']}' target='_blank'>{ui['contact_buttons'][contact][lang]}</a>")

        st.markdown("".join(buttons), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

if not filtered:
    st.warning(ui["no_results"][lang])
