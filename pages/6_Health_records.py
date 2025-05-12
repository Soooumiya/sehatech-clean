import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

# --- Page Setup ---
st.set_page_config(page_title="📁 Health Records & Preventive Calendar", layout="wide")
st.title("📁 Personal Health Records")
st.caption("Track your health checks and see when to follow up next.")

# --- Language Setup ---
lang = st.session_state.get("lang", "en")

translations = {
    "en": {
        "upload_title": "📤 Upload Medical Files",
        "upload_instruction": "Drag and drop your medical documents here. Limit 200MB per file • PDF, JPG, JPEG, PNG.",
        "consult_title": "🩺 Record Doctor Visits",
        "consult_instruction": "Track your doctor visits and diagnosis.",
        "save_button": "Save Consultation",
        "error_fill": "❌ Please fill in all the fields before saving.",
        "saved": "✅ Consultation saved.",
        "past_title": "📜 Past Consultations",
        "health_checks": "🧭 Your Personalized Health Checks",
        "next_check": "Next check recommended on: ",
        "no_followup": "No regular follow-up required.",
        "should_schedule": "📌 You should schedule a",
        "summary_title": "📆 Summary Calendar: Your Next Health Checks",
        "file_uploaded": "✅ File uploaded.",
        "visit_date": "Visit Date",
        "doctor_name": "Doctor's Name",
        "specialty": "Specialty",
        "clinic": "Clinic / Hospital",
        "notes": "Doctor's Notes / Diagnosis",
        "status": "Status",
        "done": "Done",
        "not_done": "Not Done",
        "why_is_important": "💡 Why is this important?"
    },
    "fr": {
        "upload_title": "📤 Télécharger les dossiers médicaux",
        "upload_instruction": "Téléchargez vos documents médicaux ici. Limite de 200 Mo par fichier • PDF, JPG, JPEG, PNG.",
        "consult_title": "🩺 Enregistrer les visites médicales",
        "consult_instruction": "Suivez vos visites chez le médecin et le diagnostic.",
        "save_button": "Enregistrer la consultation",
        "error_fill": "❌ Veuillez remplir tous les champs avant d'enregistrer.",
        "saved": "✅ Consultation enregistrée.",
        "past_title": "📜 Consultations précédentes",
        "health_checks": "🧭 Vos bilans de santé personnalisés",
        "next_check": "Prochain contrôle recommandé le : ",
        "no_followup": "Aucun suivi régulier requis.",
        "should_schedule": "📌 Vous devez planifier un examen",
        "summary_title": "📆 Calendrier récapitulatif : Vos prochains bilans",
        "file_uploaded": "✅ Fichier téléchargé.",
        "visit_date": "Date de la visite",
        "doctor_name": "Nom du médecin",
        "specialty": "Spécialité",
        "clinic": "Clinique / Hôpital",
        "notes": "Notes du médecin / Diagnostic",
        "status": "Statut",
        "done": "Fait",
        "not_done": "Non fait",
        "why_is_important": "💡 Pourquoi est-ce important?"
    },
    "ar": {
        "upload_title": "📤 تحميل الملفات الطبية",
        "upload_instruction": "قم بسحب وإفلات مستنداتك الطبية هنا. الحد الأقصى 200 ميجابايت لكل ملف • PDF، JPG، JPEG، PNG.",
        "consult_title": "🩺 تسجيل زيارات الطبيب",
        "consult_instruction": "تتبع زياراتك للطبيب والتشخيص.",
        "save_button": "حفظ الاستشارة",
        "error_fill": "❌ يرجى تعبئة جميع الحقول قبل الحفظ.",
        "saved": "✅ تم حفظ الاستشارة.",
        "past_title": "📜 الاستشارات السابقة",
        "health_checks": "🧭 الفحوصات الوقائية الخاصة بك",
        "next_check": "الموعد التالي الموصى به: ",
        "no_followup": "لا توجد متابعة منتظمة مطلوبة.",
        "should_schedule": "📌 يجب أن تحدد موعدًا لفحص",
        "summary_title": "📆 ملخص المواعيد القادمة للفحوصات",
        "file_uploaded": "✅ تم تحميل الملف.",
        "visit_date": "تاريخ الزيارة",
        "doctor_name": "اسم الطبيب",
        "specialty": "التخصص",
        "clinic": "العيادة / المستشفى",
        "notes": "ملاحظات الطبيب / التشخيص",
        "status": "الحالة",
        "done": "تم",
        "not_done": "لم يتم",
        "why_is_important": "💡 لماذا هذا مهم؟"
    },
    "amz": {
        "upload_title": "📤 ⵉⵖⵔⵉ ⵓⵎⴰⵣⵉⵖ ⵓⵙⴻⴷⴷⵉⵏ",
        "upload_instruction": "ⵓⵎⴰⵣⵉⵖ ⵓⵙⴻⴷⴷⵉⵏ ⵓⵎⴰⵣⵉⵖ ⴰⵏ ⵙⴻⵎⵙⴰⵏ ⵓⵙⴻⴷⴷⵉⵏ. Limit 200MB per file • PDF, JPG, JPEG, PNG.",
        "consult_title": "🩺 ⵉⴷⵉ ⵉⵙⵉⵎⵎⵉⵏ ⵏ ⵉⵙⴻⴷⴷⵉⵏ",
        "consult_instruction": "ⵓⵎⵎⴰⵣⵉⵖ ⵙⴰⵎⵓⵣⵓ ⵏ ⵙⴻⵎⵙⴰⵏ ⴰⵏ ⵉⵙⵉⵎⵎⵉⵏ.",
        "save_button": "ⵙⴻⵎⵙ ⵉⵙⵉⵎⵎⵉⵏ",
        "error_fill": "❌ ⵉⵎⴻⴼ ⵉⴽⴻⵔⴼ ⵓⵙⴻⴷⴷⵉⵏ ⵉⵏ ⵉⴷⵔⴰⵙ ⵓⴽⴰ ⵢⴰⵏⵙⵙ.",
        "saved": "✅ ⵉⵙⵉⵎⵎⵉⵏ ⵙⴻⵎⵙⴰⵏ.",
        "past_title": "📜 ⵓⴷⴰⵔⴰⵡ ⵏ ⵉⵙⵉⵎⵎⵉⵏ",
        "health_checks": "🧭 ⵓⵎⵎⴰⵍⴰ ⵏ ⴽⵕⴰⵙ ⵏ ⴰⵣⵓⵍ",
        "next_check": "ⴰⵎⵙⵙⵓ ⴳ ⵉⵎⵣⵣⴰⵡ ⴰⵙⴻⵎⵎⴰⴷ : ",
        "no_followup": "ⵓⵙⵎⵎⴰⴷ ⴰⵙⵉⵎⵎⵉ ⴰⴷⴰⵔⴰⵡ.",
        "should_schedule": "📌 ⵉⴼⴰⵍ ⴰⵎⵙⵙⵓ ⵏ",
        "summary_title": "📆 ⵙⴻⵎⵙⴰⵏ ⵏ ⵉⵎⵣⵣⴰⵡⵏ : ⵏⵏⵉ ⴰⵎⵙⵙⵓⵏ ⴰⴷⴰⵔⴰⵡ",
        "file_uploaded": "✅ ⵉⵙⵉⵎⵎⵉⵏ ⵙⴻⵎⵙⴰⵏ.",
        "visit_date": "ⵉⵎⵣⵣⴰⵡ ⵏ ⵓⵎⵎⵣⵉ",
        "doctor_name": "ⵓⵎⵎⴰⵣⵉⵖ ⵓⵙⵎⵓⵣⵓ",
        "specialty": "ⵙⵙⴻⵎⴰⵡ",
        "clinic": "ⵉⵙⴻ⵷ ⴰⵏ ⵏⵉⵙⵎⴰⵙ",
        "notes": "ⵎⵓⵣⵓ ⵓⵎⵎⴰⵣⵉⵖ / ⵙⵓⵛⴰⵎ",
        "status": "ⵎⵓⵣⵓ",
        "done": "ⵎⵓⵣⵓ ⵇⴰⵛⴰ",
        "not_done": "ⵇⵓⵙⵎ",
        "why_is_important": "💡 ⵉⵎⴻⴼ ⵉⴽⴻⵔⴼ ⵓⵙⴻⴷⴷⵉⵏ ⵏ"
    }
}

t = translations.get(lang, translations["en"])

# --- Profile ---
profile = st.session_state.get("user_profile", {})
gender = profile.get("gender", "Other")
age = profile.get("age", 30)
weight = profile.get("weight", 70)

# --- Upload Files ---
st.subheader(t["upload_title"])
st.caption(t["upload_instruction"])
if "documents" not in st.session_state:
    st.session_state.documents = []
file = st.file_uploader(t["upload_title"], type=["pdf", "jpg", "jpeg", "png"])
if file:
    st.session_state.documents.append({
        "name": file.name,
        "type": file.type,
        "date": datetime.date.today()
    })
    st.success(t["file_uploaded"])
if st.session_state.documents:
    with st.expander("📁 View Uploaded Files"):
        for doc in st.session_state.documents:
            st.markdown(f"📄 **{doc['name']}** — {doc['type']} on {doc['date']}")

# --- Consultations ---
st.subheader(t["consult_title"])
st.caption(t["consult_instruction"])
if "consultations" not in st.session_state:
    st.session_state.consultations = []

with st.form("consult_form"):
    col1, col2 = st.columns(2)
    with col1:
        visit_date = st.date_input(t["visit_date"], value=datetime.date.today())
        doctor = st.text_input(t["doctor_name"])
    with col2:
        specialty = st.text_input(t["specialty"])
        clinic = st.text_input(t["clinic"])
    notes = st.text_area(t["notes"])

    submitted = st.form_submit_button(t["save_button"])
    if submitted:
        if not doctor.strip() or not specialty.strip() or not clinic.strip() or not notes.strip():
            st.error(t["error_fill"])
        else:
            st.session_state.consultations.append({
                "date": visit_date,
                "doctor": doctor,
                "specialty": specialty,
                "clinic": clinic,
                "notes": notes
            })
            st.success(t["saved"])

if st.session_state.consultations:
    st.subheader(t["past_title"])
    for entry in sorted(st.session_state.consultations, key=lambda x: x["date"], reverse=True):
        st.markdown(f"""
        <div style='background:#f0fdf4;border-left:6px solid #10b981;padding:1rem;border-radius:10px;'>
        📅 **{entry['date']}**<br>
        👨‍⚕️ {entry['doctor']} ({entry['specialty']})<br>
        🏥 {entry['clinic']}<br>
        📝 {entry['notes']}
        </div>
        """, unsafe_allow_html=True)

# --- Preventive Checks Logic ---
def get_checks(age, gender, weight):
    return [c for c in [
        ("Blood Pressure", "🩸", "1m", "Monthly", "Monitors hypertension."),
        ("Cholesterol", "🥚", "5y", "Every 5 years", "Detects heart disease.") if age >= 20 else None,
        ("Diabetes", "🍬", "3y", "Every 3 years", "Prevents complications."),
        ("Dental", "🦷", "6m", "Every 6 months", "Oral cleaning."),
        ("Eye Exam", "👁️", "2y", "Every 2 years", "Vision screen."),
        ("Skin Check", "🌞", "1y", "Yearly", "Spot skin cancer early."),
        ("Mental Health", "🧠", "1y", "Yearly", "Stress and mood check."),
        ("Hearing Test", "👂", "5y", "Every 5 years", "Detects hearing loss.") if age >= 30 else None,
        ("Colonoscopy", "🩺", "10y", "Every 10 years", "Colon cancer screening.") if age >= 45 else None,
        ("Thyroid", "🦋", "3y", "As needed", "Thyroid function."),
        ("Hepatitis", "🧫", "once", "Once", "Prevent viral hepatitis."),
        ("Flu Vaccine", "💉", "1y", "Yearly", "Flu prevention."),
        ("BMI", "⚖️", "1y", "Yearly", "Weight management.") if weight >= 80 else None,
        ("Kidney", "🧪", "3y", "As needed", "Early kidney problems."),
        ("Vitamin D", "🌤️", "1y", "As needed", "Bone and immunity."),
        ("Sleep Health", "🛌", "as_needed", "As needed", "Sleep apnea check."),
        ("Bone Density", "🦴", "5y", "After 50", "Osteoporosis risk.") if gender == "Female" and age >= 50 else None,
        ("Breast Exam", "🎗️", "1y", "Yearly", "Early breast cancer.") if gender == "Female" and age >= 20 else None,
        ("Cervical Pap", "🧬", "3y", "Every 3 years", "Cervical cancer.") if gender == "Female" and age >= 21 else None,
        ("Prostate Exam", "🔬", "1y", "After 50", "Prostate screening.") if gender == "Male" and age >= 50 else None
    ] if c]

def add_interval(date, code):
    return {
        "1m": date + relativedelta(months=1),
        "6m": date + relativedelta(months=6),
        "1y": date + relativedelta(years=1),
        "2y": date + relativedelta(years=2),
        "3y": date + relativedelta(years=3),
        "5y": date + relativedelta(years=5),
        "10y": date + relativedelta(years=10)
    }.get(code, None)

# --- Preventive Checks UI ---
st.subheader(t["health_checks"])
if "preventive_status" not in st.session_state:
    st.session_state.preventive_status = {}
if "preventive_dates" not in st.session_state:
    st.session_state.preventive_dates = {}

summary = []
all_done = True

for name, icon, interval, freq, reason in get_checks(age, gender, weight):
    st.markdown(f"<div style='background:#ecfdf5;border-left:5px solid #10b981;padding:1rem;border-radius:10px;'>", unsafe_allow_html=True)
    col1, col2 = st.columns([5, 2])
    col1.markdown(f"### {icon} {name}")
    col1.markdown(f"_Recommended: {freq}_")
    if st.button(t["why_is_important"], key=f"why_{name}"):
        st.info(reason)
    status = col2.radio(t["status"], [t["not_done"], t["done"]], key=f"status_{name}")
    st.session_state.preventive_status[name] = status
    if status == t["done"]:
        done_date = col2.date_input("✅ When?", key=f"date_{name}", value=datetime.date.today())
        next_due = add_interval(done_date, interval)
        if next_due:
            st.success(f"{t['next_check']}{next_due.strftime('%Y-%m-%d')}")
            summary.append((name, next_due))
            st.session_state.preventive_dates[name] = next_due
        else:
            st.info(t["no_followup"])
    else:
        all_done = False
        st.warning(f"{t['should_schedule']} **{name}** soon.")
    st.markdown("</div>", unsafe_allow_html=True)

if all_done and summary:
    st.subheader(t["summary_title"])
    for name, date in sorted(summary, key=lambda x: x[1]):
        st.markdown(f"- 🗓️ **{name}** → {date.strftime('%B %d, %Y')}")
