import streamlit as st
from PIL import Image
import pytesseract
from transformers import pipeline
from io import BytesIO
import base64

# Page Config
st.set_page_config(page_title="💊 Smart Medication Scanner", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .title {
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        color: #10b981;
        margin-top: 1rem;
    }
    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .highlight {
        background-color: #ecfdf5;
        border-left: 5px solid #10b981;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .pill-name {
        font-size: 1.4rem;
        color: #065f46;
        font-weight: 600;
    }
    .answer {
        font-size: 1rem;
        color: #111827;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>💊 Smart AI Medication Scanner</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Upload prescriptions or medication labels to get intelligent insights</div>", unsafe_allow_html=True)

# Load AI Model
@st.cache_resource

def load_medical_qa():
    return pipeline("question-answering", model="dmis-lab/biobert-base-cased-v1.1-squad")

qa_model = load_medical_qa()

# Upload Image
uploaded_file = st.file_uploader("📷 Upload Prescription or Medication Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Uploaded Image", use_column_width=True)

    with st.spinner("🔍 Extracting text with OCR..."):
        extracted_text = pytesseract.image_to_string(image)

    if extracted_text.strip():
        st.markdown("### 📝 Extracted Text")
        st.code(extracted_text)

        st.markdown("### 🧠 AI Insights")
        # Extract possible drug names or candidates from text
        lines = [line.strip() for line in extracted_text.splitlines() if line.strip() and len(line.strip()) > 3]
        unique_terms = list(set(lines))

        for med in unique_terms:
            if med.replace(" ", "").isalpha():  # crude filter
                st.markdown(f"<div class='pill-name'>🔹 {med}</div>", unsafe_allow_html=True)
                try:
                    answer = qa_model(question=f"What is {med} used for?", context=extracted_text)
                    st.markdown(f"<div class='highlight answer'>{answer['answer']}</div>", unsafe_allow_html=True)
                except:
                    st.warning(f"Couldn't find relevant data for '{med}'.")
    else:
        st.warning("❌ OCR couldn't extract readable text. Try another image.")
else:
    st.info("👈 Upload an image to begin analysis.")
