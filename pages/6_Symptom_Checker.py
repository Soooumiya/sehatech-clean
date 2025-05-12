import streamlit as st

st.set_page_config(page_title="Symptom Checker", layout="wide")

# --- Page Header ---
st.markdown("<h2 style='color:#0f766e;'>🔍 Symptom Checker</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748b;'>Describe your symptoms to get possible conditions and advice.</p>", unsafe_allow_html=True)

# --- Input Section ---
symptoms = st.text_area("📝 Describe your symptoms", placeholder="e.g., headache, fever, sore throat...")
duration = st.text_input("📆 Duration of symptoms", placeholder="e.g., 2 days, 1 week...")
severity = st.slider("📊 Severity (1: mild – 10: severe)", 1, 10, 5)

# --- Check Symptoms Button ---
if st.button("Check Symptoms"):
    if symptoms.strip() == "":
        st.warning("Please enter some symptoms.")
    else:
        with st.spinner("Analyzing your symptoms..."):
            # Simulated diagnosis logic
            conditions = [
                {
                    "name": "Common Cold",
                    "probability": "80%",
                    "urgency": "Low",
                    "description": "A viral infection with symptoms like sore throat, runny nose, and cough.",
                    "recommendations": ["Rest", "Hydration", "Over-the-counter meds"]
                },
                {
                    "name": "Flu",
                    "probability": "60%",
                    "urgency": "Moderate",
                    "description": "A respiratory illness with fever, chills, and body aches.",
                    "recommendations": ["See a doctor if symptoms persist", "Rest"]
                },
                {
                    "name": "COVID-19",
                    "probability": "30%",
                    "urgency": "High",
                    "description": "Can present symptoms like fever, cough, and loss of smell.",
                    "recommendations": ["Get tested", "Self-isolate", "Seek medical help if severe"]
                }
            ]

        st.markdown("<h4 style='color:#0f766e; margin-top: 2rem;'>🩺 Possible Conditions</h4>", unsafe_allow_html=True)
        
        for condition in conditions:
            urgency_color = {
                "High": "#ef4444",
                "Moderate": "#f59e0b",
                "Low": "#10b981"
            }.get(condition["urgency"], "#6b7280")

            st.markdown(f"""
                <div style="background-color:#f9fafb; padding:1rem; border-left: 5px solid {urgency_color}; border-radius: 8px; margin-bottom: 1rem;">
                    <strong style="font-size:1.2rem; color:#0f766e;">{condition['name']}</strong>
                    <p style="margin:0.3rem 0; color:#64748b;">{condition['description']}</p>
                    <p><strong>Probability:</strong> {condition['probability']}<br>
                    <strong>Urgency:</strong> <span style="color:{urgency_color};">{condition['urgency']}</span></p>
                    <ul>
                        {''.join(f'<li>{rec}</li>' for rec in condition['recommendations'])}
                    </ul>
                </div>
            """, unsafe_allow_html=True)

        st.info("⚠️ This is not a medical diagnosis. Always consult a healthcare provider for proper medical advice.")
