import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

# --- Page Setup ---
st.set_page_config(page_title="📁 Health Records & Preventive Calendar", layout="wide")

# --- Language Setup ---
lang = st.session_state.get("lang", "en")

# --- Translations ---
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
        "why_is_important": "💡 Why is this important?",
        "view_uploaded": "📁 View Uploaded Files",
        "when_done": "✅ When?",
        "recommended": "Recommended:",
        "schedule_soon": "soon.",
        "date_format": "%Y-%m-%d",
        "check_names": {
            "Blood Pressure": "Blood Pressure",
            "Cholesterol": "Cholesterol",
            "Diabetes": "Diabetes",
            "Dental": "Dental",
            "Eye Exam": "Eye Exam",
            "Skin Check": "Skin Check",
            "Mental Health": "Mental Health",
            "Hearing Test": "Hearing Test",
            "Colonoscopy": "Colonoscopy",
            "Thyroid": "Thyroid",
            "Hepatitis": "Hepatitis",
            "Flu Vaccine": "Flu Vaccine",
            "BMI": "BMI",
            "Kidney": "Kidney",
            "Vitamin D": "Vitamin D",
            "Sleep Health": "Sleep Health",
            "Bone Density": "Bone Density",
            "Breast Exam": "Breast Exam",
            "Cervical Pap": "Cervical Pap",
            "Prostate Exam": "Prostate Exam"
        }
    },
    "fr": {
        "upload_title": "📤 Télécharger les fichiers médicaux",
        "upload_instruction": "Glissez-déposez vos documents médicaux ici. Limite de 200 Mo par fichier • PDF, JPG, JPEG, PNG.",
        "consult_title": "🩺 Enregistrer les visites médicales",
        "consult_instruction": "Suivez vos consultations médicales et diagnostics.",
        "save_button": "Enregistrer la consultation",
        "error_fill": "❌ Veuillez remplir tous les champs avant d'enregistrer.",
        "saved": "✅ Consultation enregistrée.",
        "past_title": "📜 Consultations précédentes",
        "health_checks": "🧭 Vos bilans de santé personnalisés",
        "next_check": "Prochain contrôle recommandé le : ",
        "no_followup": "Aucun suivi régulier requis.",
        "should_schedule": "📌 Vous devriez planifier un",
        "summary_title": "📆 Calendrier : Vos prochains bilans",
        "file_uploaded": "✅ Fichier téléchargé.",
        "visit_date": "Date de la visite",
        "doctor_name": "Nom du médecin",
        "specialty": "Spécialité",
        "clinic": "Clinique / Hôpital",
        "notes": "Notes du médecin / Diagnostic",
        "status": "Statut",
        "done": "Effectué",
        "not_done": "Non effectué",
        "why_is_important": "💡 Pourquoi est-ce important ?",
        "view_uploaded": "📁 Voir les fichiers téléchargés",
        "when_done": "✅ Quand ?",
        "recommended": "Recommandé :",
        "schedule_soon": "bientôt.",
        "date_format": "%d %B %Y",
        "check_names": {
            "Blood Pressure": "Pression artérielle",
            "Cholesterol": "Cholestérol",
            "Diabetes": "Diabète",
            "Dental": "Dentaire",
            "Eye Exam": "Examen des yeux",
            "Skin Check": "Examen de la peau",
            "Mental Health": "Santé mentale",
            "Hearing Test": "Test auditif",
            "Colonoscopy": "Coloscopie",
            "Thyroid": "Thyroïde",
            "Hepatitis": "Hépatite",
            "Flu Vaccine": "Vaccin contre la grippe",
            "BMI": "IMC",
            "Kidney": "Reins",
            "Vitamin D": "Vitamine D",
            "Sleep Health": "Sommeil",
            "Bone Density": "Densité osseuse",
            "Breast Exam": "Examen des seins",
            "Cervical Pap": "Test de Pap",
            "Prostate Exam": "Examen de la prostate"
        }
    },
    "ar": {
        "upload_title": "📤 تحميل الملفات الطبية",
        "upload_instruction": "اسحب وأفلت مستنداتك الطبية هنا. الحد الأقصى 200 ميجابايت لكل ملف • PDF، JPG، JPEG، PNG.",
        "consult_title": "🩺 تسجيل زيارات الطبيب",
        "consult_instruction": "تتبع زيارات الطبيب والتشخيص.",
        "save_button": "حفظ الاستشارة",
        "error_fill": "❌ يرجى تعبئة جميع الحقول قبل الحفظ.",
        "saved": "✅ تم حفظ الاستشارة.",
        "past_title": "📜 الاستشارات السابقة",
        "health_checks": "🧭 الفحوصات الوقائية الخاصة بك",
        "next_check": "الموعد التالي الموصى به: ",
        "no_followup": "لا حاجة للمتابعة المنتظمة.",
        "should_schedule": "📌 يجب تحديد موعد لـ",
        "summary_title": "📆 تقويم الفحوصات القادمة",
        "file_uploaded": "✅ تم تحميل الملف.",
        "visit_date": "تاريخ الزيارة",
        "doctor_name": "اسم الطبيب",
        "specialty": "التخصص",
        "clinic": "العيادة / المستشفى",
        "notes": "ملاحظات الطبيب / التشخيص",
        "status": "الحالة",
        "done": "تم",
        "not_done": "لم يتم",
        "why_is_important": "💡 لماذا هذا مهم؟",
        "view_uploaded": "📁 عرض الملفات المحملة",
        "when_done": "✅ متى؟",
        "recommended": "موصى به:",
        "schedule_soon": "قريبًا.",
        "date_format": "%Y/%m/%d",
        "check_names": {
            "Blood Pressure": "ضغط الدم",
            "Cholesterol": "الكوليسترول",
            "Diabetes": "السكري",
            "Dental": "الأسنان",
            "Eye Exam": "فحص العين",
            "Skin Check": "فحص الجلد",
            "Mental Health": "الصحة النفسية",
            "Hearing Test": "اختبار السمع",
            "Colonoscopy": "تنظير القولون",
            "Thyroid": "الغدة الدرقية",
            "Hepatitis": "التهاب الكبد",
            "Flu Vaccine": "لقاح الإنفلونزا",
            "BMI": "مؤشر كتلة الجسم",
            "Kidney": "الكلى",
            "Vitamin D": "فيتامين د",
            "Sleep Health": "النوم",
            "Bone Density": "كثافة العظام",
            "Breast Exam": "فحص الثدي",
            "Cervical Pap": "مسحة عنق الرحم",
            "Prostate Exam": "فحص البروستاتا"
        }
    },
    "amz": {
        "upload_title": "📤 ⵉⵖⵔⵉ ⵓⵎⴰⵣⵉⵖ",
        "upload_instruction": "ⵓⵎⴰⵣⵉⵖ PDF, JPG, PNG ⴷ 200MB ⵏ ⴰⴼⵍⴽ.",
        "consult_title": "🩺 ⴰⴷⵔⴰⵡ ⵏ ⵉⵙⵉⵎⵎⵉⵏ",
        "consult_instruction": "ⵙⴰⵎⵓⵣⵓ ⴰⵏ ⵉⵙⵉⵎⵎⵉⵏ ⴷ ⴰⴳⵔⴰⵣ ⴰⵏⵓⴷ.",
        "save_button": "ⵙⴻⵎⵙ",
        "error_fill": "❌ ⴰⵏⴼⵉⴼ ⴰⴳⴷⵔⴰ ⵓⵙⴻⴷⴷⵉⵏ ⵏ.",
        "saved": "✅ ⵙⴻⵎⵙ ⵓⵙⵙⴰⵏ.",
        "past_title": "📜 ⵓⴷⴰⵔⴰⵡ ⵏ ⵉⵙⵉⵎⵎⵉⵏ",
        "health_checks": "🧭 ⵓⵙⵙⴰⵏ ⵏ ⵓⵙⵎⵎⴰⵏ",
        "next_check": "ⴰⵎⵙⵙⵓ ⴳ ⵉⵎⵣⵣⴰⵡ: ",
        "no_followup": "ⵓⵙⵎⵎⴰⴷ ⴰⴷⴰⵔⴰⵡ.",
        "should_schedule": "📌 ⵉⴼⴰⵍ ⴰⵎⵙⵙⵓ ⵏ",
        "summary_title": "📆 ⵙⴻⵎⵙⴰⵏ ⵏ ⵉⵎⵣⵣⴰⵡⵏ",
        "file_uploaded": "✅ ⴰⵎⴰⵣⵉⵖ ⴰⴷⵔⴰⵡ.",
        "visit_date": "ⵉⵎⵣⵣⴰⵡ ⵏ ⵓⵎⵎⵣⵉ",
        "doctor_name": "ⵓⵎⵎⴰⵣⵉⵖ",
        "specialty": "ⵙⵙⴻⵎⴰⵡ",
        "clinic": "ⵓⵎⵎⵙⴰⵏ",
        "notes": "ⴰⵙⵎⴰⵍ / ⴰⴳⵔⴰⵣ",
        "status": "ⵎⵓⵣⵓ",
        "done": "ⵙⴻⵎⵙ",
        "not_done": "ⵇⵓⵙⵎ",
        "why_is_important": "💡 ⵉⵎⴻⴼ ⵉⴽⴻⵔⴼ ⵓⵙⴻⴷⴷⵉⵏ ⵏ",
        "view_uploaded": "📁 ⵓⴷⴰⵔⴰⵡ ⵏ ⴰⵎⴰⵣⵉⵖⵏ",
        "when_done": "✅ ⵓⴷⴷⴰⵔ ⴷ ⵓⴳⵔⴰⵣ?",
        "recommended": "ⵉⵙⴰⵎⵎⴰⴷ:",
        "schedule_soon": "ⵓⴷⴷⴰⵔ.",
        "date_format": "%Y-%m-%d",
        "check_names": {
            "Blood Pressure": "ⵜⴰⵙⵉⵏⵜ ⴰⴼⴰⵙⴹ",
            "Cholesterol": "ⴽⵍⵓⵙⵜⴻⵔⵉⵍ",
            "Diabetes": "ⴰⵎⴰⵣⵉⵖ",
            "Dental": "ⵜⴰⵣⵣⴰⵡⵜ ⵏ ⵜⵉⵣⵉⵣⵉⵏ",
            "Eye Exam": "ⵜⴰⵣⵣⴰⵡⵜ ⵏ ⵜⵉⴼⵔⵉⵏ",
            "Skin Check": "ⵜⴰⵣⵣⴰⵡⵜ ⵏ ⵜⴰⵏⴰⵡⵉⵢⵜ",
            "Mental Health": "ⵜⴰⵙⵙⴰⵏⵜ ⵏ ⵓⵙⴻⵍⵍⵉⵏ",
            "Hearing Test": "ⵜⴰⵙⵉⵏⵜ ⵏ ⵜⴰⵎⴰⵙⵜ",
            "Colonoscopy": "ⵜⴰⵣⵡⴰⵍⵜ ⵏ ⵉⴽⵍⵉⵏ",
            "Thyroid": "ⴰⵣⴷⵉⵡⵉⴷ",
            "Hepatitis": "ⵜⴰⵣⴰⵍⵜ ⵏ ⴰⴷⴷⵔⴰⵡ",
            "Flu Vaccine": "ⵜⴰⵎⴰⵣⵉⵖⵜ ⵏ ⴰⵍⴼⵍⵓ",
            "BMI": "ⵉⵎⵙⴰⵡ ⵏ ⵜⴰⵙⵙⵓⵏⵜ",
            "Kidney": "ⵜⴰⴳⴻⵎⵜ",
            "Vitamin D": "ⴼⵉⵜⴰⵎⵉⵏ D",
            "Sleep Health": "ⵜⴰⵙⵙⴰⵏⵜ ⵏ ⵜⵉⵎⵎⵉ",
            "Bone Density": "ⵉⵙⵎⴰⵍ ⵏ ⴰⴼⵔⴰⴷ",
            "Breast Exam": "ⵜⴰⵣⵣⴰⵡⵜ ⵏ ⵓⴷⵙⴰⵏ",
            "Cervical Pap": "ⵜⴰⵙⵉⵏⵜ ⵏ ⵓⴽⴽⴰⵡ",
            "Prostate Exam": "ⵜⴰⵣⵣⴰⵡⵜ ⵏ ⵜⵓⴽⵍⵍⵉⵎⵓⵏ"
        }
    }
}

t = translations.get(lang, translations["en"])
check_names = t["check_names"]

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
    with st.expander(t["view_uploaded"]):
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
    translated_name = check_names.get(name, name)
    st.markdown("<div style='background:#ecfdf5;border-left:5px solid #10b981;padding:1rem;border-radius:10px;'>", unsafe_allow_html=True)
    col1, col2 = st.columns([5, 2])
    col1.markdown(f"### {icon} {translated_name}")
    col1.markdown(f"*{t['recommended']} {freq}*")
    if st.button(t["why_is_important"], key=f"why_{name}"):
        st.info(reason)
    status = col2.radio(t["status"], [t["not_done"], t["done"]], key=f"status_{name}")
    st.session_state.preventive_status[name] = status
    if status == t["done"]:
        done_date = col2.date_input(t["when_done"], key=f"date_{name}", value=datetime.date.today())
        next_due = add_interval(done_date, interval)
        if next_due:
            st.success(f"{t['next_check']}{next_due.strftime(t['date_format'])}")
            summary.append((translated_name, next_due))
            st.session_state.preventive_dates[name] = next_due
        else:
            st.info(t["no_followup"])
    else:
        all_done = False
        st.warning(f"{t['should_schedule']} **{translated_name}** {t['schedule_soon']}")
    st.markdown("</div>", unsafe_allow_html=True)

if all_done and summary:
    st.subheader(t["summary_title"])
    for name, date in sorted(summary, key=lambda x: x[1]):
        st.markdown(f"- 🗓️ **{name}** → {date.strftime(t['date_format'])}")
