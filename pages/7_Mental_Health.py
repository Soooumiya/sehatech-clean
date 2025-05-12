import streamlit as st
import datetime
import random
import time
import os

# --- Language setup ---
lang = st.session_state.get("lang", "en")

# --- Translations dictionary ---
translations = {
    "en": {
        "title": "🧠 How Are You Feeling Today?",
        "moods": ["😊 Happy", "😢 Sad", "😡 Angry", "😰 Anxious", "😐 Neutral"],
        "mood_messages": {
            "😊 Happy": "That's wonderful! Keep shining 🌞",
            "😢 Sad": "It's okay to feel sad. Talk to someone you trust. 💙",
            "😡 Angry": "Take deep breaths. Relax your mind. 🔥",
            "😰 Anxious": "You're safe. Breathe... 🌬️",
            "😐 Neutral": "Take a pause. You're doing fine. 🧘"
        },
        "journal": "📝 Journal",
        "write": "Write your thoughts:",
        "save": "💾 Save Entry",
        "saved": "Saved!",
        "warning": "Please write something.",
        "reflections": "📚 Past Reflections",
        "choose_activity": "Choose your activity:",
        "breathing": "🌬️ Breathing Exercise",
        "yoga": "🧘 Play Local Yoga Video",
        "quran": "🎧 Listen to Quran (Offline)",
        "music": "🎵 Relaxing Music (Offline)",
        "duration": "Duration (seconds)",
        "start": "▶️ Start Breathing",
        "complete": "✅ Breathing complete!",
        "now_playing": "Now playing",
        "choose_surah": "Choose Surah:",
        "choose_track": "Choose Track:",
        "seconds_remaining": "seconds remaining",
        "tip": "💡 Mental Health Tip of the Day",
        "footer": "© 2025 Mental Health App",
        "tips": [
            "Pause and breathe deeply.",
            "Drink water and stretch.",
            "List three things you're grateful for.",
            "Disconnect for 10 minutes.",
            "Call someone you love.",
            "Be kind to yourself.",
            "Rest is not laziness."
        ],
        "quran_options": ["Surah Ar-Rahman", "Surah Yasin", "Surah Al-Mulk"],
        "music_options": ["Forest Sounds", "Ocean Waves"]
    },
    "fr": {
        "title": "🧠 Comment vous sentez-vous aujourd'hui ?",
        "moods": ["😊 Heureux", "😢 Triste", "😡 En colère", "😰 Anxieux", "😐 Neutre"],
        "mood_messages": {
            "😊 Heureux": "C'est merveilleux ! Continuez à briller 🌞",
            "😢 Triste": "C'est normal d'être triste. Parlez à quelqu'un. 💙",
            "😡 En colère": "Respirez profondément. Calmez votre esprit. 🔥",
            "😰 Anxieux": "Vous êtes en sécurité. Respirez... 🌬️",
            "😐 Neutre": "Prenez une pause. Vous allez bien. 🧘"
        },
        "journal": "📝 Journal",
        "write": "Écrivez vos pensées :",
        "save": "💾 Enregistrer",
        "saved": "Enregistré !",
        "warning": "Veuillez écrire quelque chose.",
        "reflections": "📚 Réflexions passées",
        "choose_activity": "Choisissez une activité :",
        "breathing": "🌬️ Exercice de respiration",
        "yoga": "🧘 Lire la vidéo de yoga locale",
        "quran": "🎧 Écouter le Coran (hors ligne)",
        "music": "🎵 Musique relaxante (hors ligne)",
        "duration": "Durée (secondes)",
        "start": "▶️ Démarrer",
        "complete": "✅ Respiration terminée !",
        "now_playing": "Lecture en cours",
        "choose_surah": "Choisissez une sourate :",
        "choose_track": "Choisissez une piste :",
        "seconds_remaining": "secondes restantes",
        "tip": "💡 Conseil bien-être du jour",
        "footer": "© 2025 Application Bien-être Mental",
        "tips": [
            "Faites une pause et respirez profondément.",
            "Buvez de l'eau et étirez-vous.",
            "Notez trois choses pour lesquelles vous êtes reconnaissant.",
            "Déconnectez-vous pendant 10 minutes.",
            "Appelez quelqu'un que vous aimez.",
            "Soyez bienveillant envers vous-même.",
            "Se reposer n'est pas être paresseux."
        ],
        "quran_options": ["Sourate Ar-Rahman", "Sourate Yasin", "Sourate Al-Mulk"],
        "music_options": ["Sons de la forêt", "Vagues de l'océan"]
    },
    "ar": {
        "title": "🧠 كيف تشعر اليوم؟",
        "moods": ["😊 سعيد", "😢 حزين", "😡 غاضب", "😰 قلق", "😐 محايد"],
        "mood_messages": {
            "😊 سعيد": "هذا رائع! استمر في التألق 🌞",
            "😢 حزين": "لا بأس أن تشعر بالحزن. تحدث إلى شخص تثق به. 💙",
            "😡 غاضب": "تنفس بعمق. استرخي. 🔥",
            "😰 قلق": "أنت بأمان. تنفس... 🌬️",
            "😐 محايد": "خذ استراحة. أنت بخير. 🧘"
        },
        "journal": "📝 المفكرة",
        "write": "اكتب أفكارك:",
        "save": "💾 حفظ الإدخال",
        "saved": "تم الحفظ!",
        "warning": "يرجى كتابة شيء ما.",
        "reflections": "📚 تأملات سابقة",
        "choose_activity": "اختر نشاطًا:",
        "breathing": "🌬️ تمرين التنفس",
        "yoga": "🧘 تشغيل فيديو يوجا",
        "quran": "🎧 استمع إلى القرآن (بدون إنترنت)",
        "music": "🎵 موسيقى مريحة (بدون إنترنت)",
        "duration": "المدة (ثوانٍ)",
        "start": "▶️ ابدأ التمرين",
        "complete": "✅ تم التمرين!",
        "now_playing": "يتم التشغيل الآن",
        "choose_surah": "اختر السورة:",
        "choose_track": "اختر المقطع:",
        "seconds_remaining": "ثوانٍ متبقية",
        "tip": "💡 نصيحة لراحتك النفسية اليوم",
        "footer": "© 2025 تطبيق الصحة النفسية",
        "tips": [
            "توقف وتنفس بعمق.",
            "اشرب الماء وتمدد.",
            "اكتب ثلاث نعم في حياتك.",
            "افصل الهاتف لمدة 10 دقائق.",
            "اتصل بشخص تحبه.",
            "كن لطيفاً مع نفسك.",
            "الراحة ليست كسلاً."
        ],
        "quran_options": ["سورة الرحمن", "سورة يس", "سورة الملك"],
        "music_options": ["أصوات الغابة", "أمواج المحيط"]
    }
}

# --- Get current language dictionary ---
T = translations.get(lang, translations["en"])
def t(k): return T.get(k, k)

# --- Page Configuration ---
st.set_page_config(page_title=t("title"))
st.title(t("title"))

# --- Mood Selection ---
mood = st.radio("", T["moods"], horizontal=True)
st.success(T["mood_messages"][mood])

# --- Journal Section ---
st.subheader(t("journal"))
entry = st.text_area(t("write"))

if "journal" not in st.session_state:
    st.session_state.journal = []

if st.button(t("save")):
    if entry.strip():
        st.session_state.journal.append({
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "text": entry
        })
        st.success(t("saved"))
    else:
        st.warning(t("warning"))

if st.session_state.journal:
    st.subheader(t("reflections"))
    for item in reversed(st.session_state.journal):
        st.markdown(f"**{item['date']}**  \n{item['text']}")
        st.markdown("---")

# --- Activities Section ---
st.subheader(t("choose_activity"))
activity = st.selectbox("", [t("breathing"), t("yoga"), t("quran"), t("music")])

# Breathing Exercise
if activity == t("breathing"):
    duration = st.slider(t("duration"), 10, 60, 30)
    if st.button(t("start")):
        bar = st.progress(0)
        counter = st.empty()
        for i in range(duration):
            remaining = duration - i
            counter.markdown(
                f"<div style='text-align:center;font-size:24px;'>{remaining} {t('seconds_remaining')}</div>",
                unsafe_allow_html=True
            )
            bar.progress((i + 1) / duration)
            time.sleep(1)
        bar.empty()
        counter.empty()
        st.success(t("complete"))

# Yoga Video
elif activity == t("yoga"):
    if os.path.exists("videos/Yoga.mp4"):
        st.video("videos/Yoga.mp4")
    else:
        st.warning("Yoga video not found.")

# Quran Audio Playlist
elif activity == t("quran"):
    surahs = T["quran_options"]
    files = {
        surahs[0]: "audio/quran/Surah_Ar_Rahman.mp3",
        surahs[1]: "audio/quran/Surah_Yasin.mp3",
        surahs[2]: "audio/quran/Surah_Al_Mulk.mp3"
    }
    choice = st.selectbox(t("choose_surah"), list(files.keys()))
    if os.path.exists(files[choice]):
        st.audio(files[choice])
        st.caption(f"{t('now_playing')}: {choice}")
    else:
        st.warning("Audio file not found.")

# Relaxing Music Playlist
elif activity == t("music"):
    tracks = T["music_options"]
    files = {
        tracks[0]: "audio/music/Forest_Sounds.mp3",
        tracks[1]: "audio/music/Ocean_Waves.mp3"
    }
    choice = st.selectbox(t("choose_track"), list(files.keys()))
    if os.path.exists(files[choice]):
        st.audio(files[choice])
        st.caption(f"{t('now_playing')}: {choice}")
    else:
        st.warning("Audio file not found.")

# --- Mental Health Tip of the Day ---
st.subheader(t("tip"))
st.info(random.choice(T["tips"]))

# --- Footer ---
st.markdown(f"<div style='text-align:center;color:gray;margin-top:2rem'>{t('footer')}</div>", unsafe_allow_html=True)
