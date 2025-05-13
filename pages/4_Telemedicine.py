import streamlit as st
import json

# --- Page setup ---
st.set_page_config(page_title="SehaTech - Doctors", layout="wide")

# --- Multilingual notice ---
lang = st.session_state.get("lang", "en")

notices = {
    "en": "❗ This page cannot be translated due to the nature of doctor names, contact methods, and clinical data.",
    "fr": "❗ Cette page ne peut pas être traduite en raison des noms des médecins et des données médicales.",
    "ar": "❗ لا يمكن ترجمة هذه الصفحة بسبب أسماء الأطباء والبيانات الطبية.",
    "amz": "❗ ⵜⴰⵙⴳⴰ ⴼⵓⵍⴰ ⵜⴰⵏⵙⵉⴷⵜ ⵉⵙ ⵓⴽⴰⵢ ⴰⴷⵔⴰⴼ ⴰⵏⵙⵙ ⴰⵎⴰⵣⵉⵖ ⵏ ⴰⵎⵎⵓⵔⵏ ⴷ ⵉⵙⴻⴼⴽⴰⵏ ⵏ ⵜⵉⴷⵍⵍⵉⵜ.",
}


st.warning(notices.get(lang, notices["en"]))

# --- Load doctor data ---
with open("doctors_500.json", "r") as f:
    doctors = json.load(f)

# --- Extract filters ---
specialties = sorted(set(doc['specialty'] for doc in doctors))
languages = sorted(set(lang for doc in doctors for lang in doc['languages']))
contacts = ["Video Call", "WhatsApp", "Email", "Message"]

# --- CSS styles ---
st.markdown("""
    <style>
        .header {
            color: #0f766e;
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
        }
        .subheader {
            color: #6b7280;
            text-align: center;
            font-size: 1rem;
            margin-bottom: 2rem;
        }
        .card {
            background: #ffffff;
            border-radius: 16px;
            padding: 1rem;
            margin-bottom: 1.5rem;
            border: 1px solid #e5e7eb;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        .doc-img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 12px;
        }
        .doc-name {
            font-weight: bold;
            font-size: 1.2rem;
            color: #065f46;
            margin-top: 0.5rem;
        }
        .doc-specialty {
            color: #089981;
            font-size: 0.95rem;
        }
        .status {
            font-size: 0.85rem;
            color: #059669;
            margin-bottom: 0.5rem;
        }
        .btn {
            padding: 6px 12px;
            text-decoration: none;
            border-radius: 999px;
            font-size: 0.8rem;
            margin: 4px 4px 0 0;
            display: inline-block;
            color: white;
            font-weight: 500;
        }
        .btn.video { background-color: #0d9488; }
        .btn.whatsapp { background-color: #25D366; }
        .btn.email { background-color: #2563eb; }
        .btn.sms { background-color: #6b7280; }
        .btn:hover { opacity: 0.9; }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<div class='header'>🩺 SehaTech - Find Your Doctor</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Filter doctors by specialty, language, and contact method. 500+ doctors available.</div>", unsafe_allow_html=True)

# --- Filters ---
col1, col2, col3 = st.columns(3)
with col1:
    selected_spec = st.selectbox("🩺 Specialty", specialties)
with col2:
    selected_lang = st.selectbox("🌐 Language", languages)
with col3:
    selected_contact = st.selectbox("📞 Contact Method", contacts)

# --- Filter logic ---
def match(doc):
    return (
        doc["specialty"] == selected_spec and
        selected_lang in doc["languages"] and
        selected_contact in doc["contacts"]
    )

filtered = [doc for doc in doctors if match(doc)]

# --- Pagination ---
page_size = 12
total = len(filtered)
page = st.number_input("Page", 1, max(1, total // page_size + (1 if total % page_size else 0)), 1)
start_idx = (page - 1) * page_size
end_idx = start_idx + page_size
paged_docs = filtered[start_idx:end_idx]

st.markdown(f"### ✅ Showing {len(paged_docs)} of {total} matching doctors")

# --- Display cards ---
cols = st.columns(3)

for idx, doc in enumerate(paged_docs):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="card">
            <img src="{doc['image']}" class="doc-img" alt="{doc['name']}">
            <div class="doc-name">{doc['name']}</div>
            <div class="doc-specialty">🩺 {doc['specialty']}</div>
            <div class="status">🟢 {doc['status']}</div>
            <div>📞 {doc['phone']}</div>
            <div>🌍 {', '.join(doc['languages'])}</div>
            <div style="margin-top: 0.6rem;">
        """, unsafe_allow_html=True)

        buttons = []
        if "Video Call" in doc["contacts"]:
            buttons.append(f"<a class='btn video' href='https://meet.jit.si/{doc['name'].replace(' ', '')}' target='_blank'>🎥 Video</a>")
        if "WhatsApp" in doc["contacts"]:
            buttons.append(f"<a class='btn whatsapp' href='https://wa.me/{doc['phone'].replace('+', '')}' target='_blank'>💬 WhatsApp</a>")
        if "Email" in doc["contacts"]:
            buttons.append(f"<a class='btn email' href='mailto:{doc['email']}' target='_blank'>✉️ Email</a>")
        if "Message" in doc["contacts"]:
            buttons.append(f"<a class='btn sms' href='sms:{doc['phone']}' target='_blank'>📲 SMS</a>")

        st.markdown("".join(buttons), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

if not filtered:
    st.warning("No doctors match your filters. Try changing your selection.")
