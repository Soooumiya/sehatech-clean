import streamlit as st
import urllib.parse
from streamlit_geolocation import streamlit_geolocation

# --- Language Selection ---
lang = st.session_state.get("lang", "en")

# --- Translations ---
translations = {
    "en": {
        "title": "📍 Nearby Health Services",
        "subtitle": "Search for hospitals, clinics, or pharmacies near your location",
        "enter_location": "📍 Enter your area, city, or ZIP",
        "placeholder": "e.g. Riyadh, 11564",
        "map_title": "🗺️ Map of results",
        "open_map": "🔗 Open full map in Google Maps",
        "info": "👈 Enter a location and choose a service type to begin.",
        "types": ["Hospital", "Clinic", "Pharmacy"],
        "use_my_location": "📍 Use My Location",
        "location_error": "⚠️ We couldn’t get your location. Please enable location permissions in your browser settings and try again.",
        "location_prompt": "🔒 Please allow location access when prompted by your browser."
    },
    # Add FR, AR, AMZ versions if needed
}

t = translations[lang]

# --- Page Config ---
st.set_page_config(page_title=t["title"], layout="centered")

# --- Style ---
st.markdown("""
    <style>
        .main-title {
            font-size: 2.4rem;
            text-align: center;
            color: #1f2937;
            margin-bottom: 0.5rem;
        }
        .sub-title {
            font-size: 1.05rem;
            text-align: center;
            color: #6b7280;
            margin-bottom: 2rem;
        }
        .service-tabs {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin-bottom: 2rem;
        }
        .tab {
            border: 1.5px solid #10b981;
            border-radius: 999px;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            cursor: pointer;
            background: white;
            color: #065f46;
            transition: all 0.2s ease-in-out;
        }
        .tab:hover {
            background: #d1fae5;
        }
        .tab.selected {
            background: #10b981;
            color: white;
        }
        .map-note {
            font-size: 0.95rem;
            color: #4b5563;
            text-align: center;
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Titles ---
st.markdown(f"<div class='main-title'>{t['title']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sub-title'>{t['subtitle']}</div>", unsafe_allow_html=True)

# --- Service Type Selector ---
place_types = t["types"]
if "selected_service" not in st.session_state:
    st.session_state.selected_service = place_types[0]

st.markdown('<div class="service-tabs">', unsafe_allow_html=True)
for ptype in place_types:
    selected_class = "selected" if st.session_state.selected_service == ptype else ""
    st.markdown(f"""
        <div class="tab {selected_class}" onclick="document.getElementById('{ptype}_btn').click();">{ptype}</div>
    """, unsafe_allow_html=True)
    st.button("", key=f"{ptype}_btn", on_click=lambda p=ptype: st.session_state.update({"selected_service": p}))
st.markdown('</div>', unsafe_allow_html=True)

# --- Location Input ---
location = st.text_input(t["enter_location"], placeholder=t["placeholder"])

# --- Use My Location Button ---
use_gps = st.button(t["use_my_location"])

# --- GPS Logic ---
if use_gps:
    st.info(t["location_prompt"])  # Ask for permission

    loc = streamlit_geolocation()
    if loc and loc.get("latitude") and loc.get("longitude"):
        lat, lon = loc["latitude"], loc["longitude"]
        query = f"{st.session_state.selected_service} near {lat},{lon}"
        maps_url = f"https://www.google.com/maps/search/{urllib.parse.quote(query)}"
        st.markdown(f"### {t['map_title']}")
        st.components.v1.iframe(maps_url, height=500)
        st.markdown(f"<div class='map-note'><a href='{maps_url}' target='_blank'>{t['open_map']}</a></div>", unsafe_allow_html=True)
    else:
        st.warning(t["location_error"])

# --- Fallback: Manual Entry ---
elif location:
    query = f"{st.session_state.selected_service} near {location}"
    maps_url = f"https://www.google.com/maps/search/{urllib.parse.quote(query)}"
    st.markdown(f"### {t['map_title']}")
    st.components.v1.iframe(maps_url, height=500)
    st.markdown(f"<div class='map-note'><a href='{maps_url}' target='_blank'>{t['open_map']}</a></div>", unsafe_allow_html=True)
else:
    st.info(t["info"])
