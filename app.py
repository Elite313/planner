"""
AI Summit Navigator - Premium Edition
Personalized itinerary for Product Managers & Tech Engineers
India AI Impact Summit 2026
"""

import streamlit as st
import json
import os
import base64
from urllib.parse import quote
from textwrap import dedent

# ----------------------------
# Helpers
# ----------------------------
def md_html(html: str):
    """Render HTML/CSS reliably (prevents Streamlit from treating indented HTML as code)."""
    st.markdown(dedent(html), unsafe_allow_html=True)


# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="AI Summit Planner | India AI Impact Summit 2026",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------
# Custom CSS
# ----------------------------
md_html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

/* Apply your font to content, but DON'T break icon fonts */
.stApp { font-family: 'Plus Jakarta Sans', sans-serif; }

/* normal text elements */
.stMarkdown, .stMarkdown * ,
.stText, .stText * ,
label, input, textarea, button, select {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
}

/* restore Streamlit icon fonts */
.material-icons, .material-symbols-outlined, .material-symbols-rounded {
  font-family: 'Material Icons' !important;
}


/* Keep code blocks readable */
code, pre, pre * { font-family: 'JetBrains Mono', monospace !important; }

.stApp { background: linear-gradient(180deg, #fafbfc 0%, #ffffff 100%); }

#MainMenu, footer, header { visibility: hidden; }

.main .block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

/* Logo Header */
.logo-header {
    background: linear-gradient(135deg, #0c1445 0%, #1a237e 50%, #283593 100%);
    padding: 1.25rem 2rem;
    border-radius: 20px;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 10px 40px rgba(26, 35, 126, 0.2);
    position: relative;
    overflow: hidden;
}

.logo-header::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 300px;
    height: 100%;
    background: linear-gradient(135deg, transparent 0%, rgba(255,255,255,0.05) 100%);
}

.logo-left {
    display: flex;
    align-items: center;
    gap: 1rem;
    z-index: 1;
}

.logo-icon {
    width: 50px;
    height: 50px;
    background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
}

.logo-text h1 {
    color: white;
    font-size: 1.3rem;
    font-weight: 700;
    margin: 0;
    letter-spacing: -0.01em;
}

.logo-text p {
    color: rgba(255,255,255,0.7);
    font-size: 0.8rem;
    margin: 0.2rem 0 0 0;
}

.logo-badge {
    background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 100px;
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    z-index: 1;
}

/* Hero Section */
.hero-section { text-align: center; padding: 1.5rem 0 2rem; }

.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
    color: #047857;
    padding: 0.5rem 1.25rem;
    border-radius: 100px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 1.25rem;
    border: 1px solid #a7f3d0;
}

.hero-title {
    font-size: 2.5rem;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.1;
    margin-bottom: 0.75rem;
    letter-spacing: -0.03em;
}

.hero-title span {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-hook { font-size: 1.15rem; color: #475569; margin-bottom: 1.5rem; line-height: 1.5; }
.hero-hook strong { color: #0f172a; }

/* Audience Pills */
.audience-row {
    display: flex;
    justify-content: center;
    gap: 0.75rem;
    flex-wrap: wrap;
    margin-bottom: 1.5rem;
}

.audience-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.6rem 1.25rem;
    border-radius: 100px;
    font-size: 0.85rem;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.pill-pm { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
.pill-eng { background: linear-gradient(135deg, #059669 0%, #10b981 100%); color: white; }

/* Stats Row */
.stats-row {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    padding: 1rem 1.5rem;
    background: white;
    border-radius: 16px;
    margin: 1.5rem 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    border: 1px solid #e2e8f0;
}

.stat-item { text-align: center; padding: 0 1rem; border-right: 1px solid #e2e8f0; }
.stat-item:last-child { border-right: none; }

.stat-number {
    font-size: 1.5rem;
    font-weight: 800;
    color: #0f172a;
    font-family: 'JetBrains Mono', monospace;
}

.stat-label {
    font-size: 0.7rem;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* Question Card */
.question-card {
    background: white;
    border-radius: 20px;
    padding: 1.75rem;
    margin: 1.25rem 0;
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.06);
    border: 1px solid #e2e8f0;
}

.question-header { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem; }

.question-number {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.95rem;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.question-title { font-size: 1.2rem; font-weight: 700; color: #0f172a; }

.question-subtitle {
    font-size: 0.9rem;
    color: #64748b;
    margin-left: 3rem;
    margin-bottom: 1.25rem;
}

/* Session Card */
.session-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1.25rem;
    margin: 0.75rem 0;
    transition: all 0.2s ease;
}

.session-card:hover { box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08); transform: translateY(-2px); }

.session-title { font-size: 1rem; font-weight: 600; color: #0f172a; margin-bottom: 0.4rem; }
.session-meta { font-size: 0.8rem; color: #64748b; margin-bottom: 0.5rem; }

/* Badges */
.badge {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    padding: 0.3rem 0.7rem;
    border-radius: 100px;
    font-size: 0.72rem;
    font-weight: 600;
}

.badge-high { background: #dcfce7; color: #166534; }
.badge-medium { background: #fef9c3; color: #854d0e; }
.badge-vip { background: linear-gradient(135deg, #f59e0b, #d97706); color: white; }
.badge-pm { background: #ede9fe; color: #6d28d9; }
.badge-eng { background: #d1fae5; color: #047857; }
.badge-restricted { background: #fee2e2; color: #dc2626; }
.badge-public { background: #dbeafe; color: #1d4ed8; }

.topic-tag {
    display: inline-block;
    padding: 0.2rem 0.5rem;
    background: #f1f5f9;
    color: #475569;
    border-radius: 6px;
    font-size: 0.7rem;
    font-weight: 500;
    margin: 0.1rem;
}

/* Venue */
.venue-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1.25rem;
    margin: 0.5rem 0;
    transition: all 0.2s ease;
}

.venue-card:hover { box-shadow: 0 6px 20px rgba(0,0,0,0.08); }

.venue-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.75rem;
}

.venue-name { font-size: 1rem; font-weight: 700; color: #0f172a; }

.venue-access {
    font-size: 0.75rem;
    padding: 0.25rem 0.6rem;
    border-radius: 100px;
}

.access-vip {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    color: #92400e;
    border: 1px solid #fcd34d;
}

.access-public {
    background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
    color: #1e40af;
    border: 1px solid #93c5fd;
}

.access-restricted {
    background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
    color: #991b1b;
    border: 1px solid #fca5a5;
}

.venue-details { font-size: 0.85rem; color: #64748b; }

.venue-tip {
    background: #f0fdf4;
    border-left: 3px solid #10b981;
    padding: 0.75rem 1rem;
    margin-top: 0.75rem;
    border-radius: 0 8px 8px 0;
    font-size: 0.8rem;
    color: #065f46;
}

/* Action Buttons */
.action-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.875rem 1.5rem;
    border-radius: 12px;
    font-weight: 600;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.2s ease;
    text-decoration: none;
    border: none;
    width: 100%;
    text-align: center;
}

.btn-whatsapp { background: linear-gradient(135deg, #25D366 0%, #128C7E 100%); color: white; }
.btn-pdf { background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); color: white; }
.btn-share { background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); color: white; }

.action-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15); }

/* Expo Card */
.expo-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1.25rem;
    text-align: center;
    transition: all 0.2s ease;
    height: 100%;
}

.expo-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08); }

.expo-icon { font-size: 2rem; margin-bottom: 0.75rem; }
.expo-title { font-size: 0.95rem; font-weight: 600; color: #0f172a; margin-bottom: 0.25rem; }
.expo-tags { font-size: 0.75rem; color: #64748b; }

/* Gate Info */
.gate-card {
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
}

.gate-number { font-size: 1.25rem; font-weight: 800; color: #1e40af; }
.gate-name { font-size: 0.8rem; color: #64748b; }

/* Footer */
.footer {
    text-align: center;
    padding: 2.5rem 1rem;
    margin-top: 3rem;
    background: linear-gradient(135deg, #0c1445 0%, #1a237e 100%);
    border-radius: 20px;
    color: white;
}

.footer p { margin: 0.5rem 0; }
.footer a { color: #a5b4fc; }

.creator-section {
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(255,255,255,0.1);
}

/* Streamlit Overrides */
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 0.75rem 2rem;
    border-radius: 12px;
    font-weight: 600;
    font-size: 1rem;
    transition: all 0.2s ease;
    width: 100%;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

div[data-testid="stExpander"] {
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    overflow: hidden;
    background: white;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 0.5rem;
    background: #f1f5f9;
    padding: 0.5rem;
    border-radius: 12px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 0.75rem 1.25rem;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background: white;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.stProgress > div > div {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 100px;
}
</style>
""")


# ----------------------------
# Data
# ----------------------------
@st.cache_data
def load_event_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "event_data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

EVENT_DATA = load_event_data()

COMMUNITY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "community_itineraries.json")


def load_community_data():
    if os.path.exists(COMMUNITY_FILE):
        with open(COMMUNITY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"itineraries": []}


def save_community_data(data):
    with open(COMMUNITY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


DAYS = ["2026-02-16", "2026-02-17", "2026-02-18", "2026-02-19", "2026-02-20"]
DAY_INFO = {
    "2026-02-16": {"short": "Feb 16", "name": "Monday", "theme": "Expo Launch & Inauguration"},
    "2026-02-17": {"short": "Feb 17", "name": "Tuesday", "theme": "Sectoral Deep Dives"},
    "2026-02-18": {"short": "Feb 18", "name": "Wednesday", "theme": "Research & Innovation"},
    "2026-02-19": {"short": "Feb 19", "name": "Thursday", "theme": "Summit Opening & CEOs"},
    "2026-02-20": {"short": "Feb 20", "name": "Friday", "theme": "Global Cooperation"},
}

VENUE_MAP = {
    "bharat_mandapam": {
        "name": "Bharat Mandapam",
        "icon": "🏛️",
        "levels": ["Level 1", "Level 2", "Level 3", "Amphitheater"],
        "access": "public",
        "sessions": ["Opening Ceremony", "Plenary Sessions", "CEO Roundtables"],
        "tip": "Main venue - arrive 30 mins early for security check"
    },
    "plenary_hall_b": {
        "name": "Plenary Hall B",
        "icon": "🎤",
        "access": "vip",
        "sessions": ["VIP Sessions", "Leaders' Plenary", "Closing Ceremony"],
        "tip": "VIP/Delegate pass required. Located near Hall 14"
    },
    "west_wing": {
        "name": "West Wing",
        "icon": "🏢",
        "access": "public",
        "sessions": ["Panel Discussions", "Workshops", "Breakout Sessions"],
        "tip": "Multiple meeting rooms. Check room number on your ticket"
    },
    "hall_14": {
        "name": "Hall 14 (Ground & First Floor)",
        "icon": "🎪",
        "access": "public",
        "sessions": ["International Pavilions", "France Pavilion", "Country Exhibits"],
        "tip": "Largest international pavilion area. French Pavilion is 436 m²"
    },
    "hall_1_5": {
        "name": "Halls 1-5",
        "icon": "🏭",
        "access": "public",
        "sessions": ["Startup Showcases", "Tech Demos", "Industry Exhibits"],
        "tip": "Ground & First floors. Connected via East Plaza"
    },
    "hall_6": {
        "name": "Hall 6",
        "icon": "📊",
        "access": "public",
        "sessions": ["Research Symposium", "Academic Sessions"],
        "tip": "Near National Science Centre. Food court nearby"
    },
    "hall_11": {
        "name": "Hall 11",
        "icon": "🤖",
        "access": "public",
        "sessions": ["AI Demos", "Startup Pitches", "Innovation Zone"],
        "tip": "Adjacent to main food court area"
    }
}

GATES = {
    "gate_1": {"name": "Gate 1", "location": "East (Bhairon Marg)", "helpdesk": True, "nearest": "Halls 5-6"},
    "gate_4": {"name": "Gate 4", "location": "East (Bhairon Marg)", "helpdesk": True, "nearest": "Halls 3-5"},
    "gate_6": {"name": "Gate 6", "location": "South (Mathura Road)", "helpdesk": False, "nearest": "Halls 1-2"},
    "gate_7": {"name": "Gate 7", "location": "South (Mathura Road)", "helpdesk": True, "nearest": "Bharat Mandapam"},
    "gate_8": {"name": "Gate 8", "location": "Southwest", "helpdesk": False, "nearest": "West Wing"},
    "gate_10": {"name": "Gate 10", "location": "West", "helpdesk": True, "nearest": "Hall 14"},
    "gate_11": {"name": "Gate 11", "location": "Northwest", "helpdesk": False, "nearest": "Hall 6, 11"},
}

ROLES = {
    "product": {
        "apm": {"name": "APM", "full": "Associate Product Manager", "icon": "🌱", "level": "Entry"},
        "pm": {"name": "PM", "full": "Product Manager", "icon": "📱", "level": "Mid"},
        "spm": {"name": "SPM", "full": "Senior Product Manager", "icon": "🎯", "level": "Senior"},
        "gpm": {"name": "GPM", "full": "Group Product Manager", "icon": "👥", "level": "Lead"},
        "director": {"name": "Director", "full": "Director of Product", "icon": "📊", "level": "Director"},
        "vp": {"name": "VP", "full": "VP of Product", "icon": "🏢", "level": "VP"},
        "cpo": {"name": "CPO", "full": "Chief Product Officer", "icon": "👔", "level": "C-Suite"},
    },
    "engineering": {
        "sde1": {"name": "SDE-1", "full": "Software Engineer", "icon": "💻", "level": "Entry"},
        "sde2": {"name": "SDE-2", "full": "Senior Engineer", "icon": "⚙️", "level": "Mid"},
        "sde3": {"name": "Staff", "full": "Staff Engineer", "icon": "🔧", "level": "Senior"},
        "tech_lead": {"name": "TL", "full": "Tech Lead", "icon": "👨‍💻", "level": "Lead"},
        "em": {"name": "EM", "full": "Engineering Manager", "icon": "👥", "level": "Manager"},
        "ds": {"name": "DS", "full": "Data Scientist", "icon": "📈", "level": "IC"},
        "mle": {"name": "MLE", "full": "ML Engineer", "icon": "🤖", "level": "IC"},
        "architect": {"name": "Arch", "full": "Architect", "icon": "🏗️", "level": "Senior"},
        "director_eng": {"name": "Dir", "full": "Director of Eng", "icon": "📊", "level": "Director"},
        "vp_eng": {"name": "VP", "full": "VP Engineering", "icon": "🏢", "level": "VP"},
        "cto": {"name": "CTO", "full": "CTO", "icon": "👔", "level": "C-Suite"},
    }
}

SECTORS = {
    "edtech": {"name": "EdTech", "icon": "📚"},
    "fintech": {"name": "FinTech", "icon": "💳"},
    "healthtech": {"name": "HealthTech", "icon": "🏥"},
    "ecommerce": {"name": "E-Commerce", "icon": "🛒"},
    "saas": {"name": "SaaS / B2B", "icon": "☁️"},
    "consumer": {"name": "Consumer", "icon": "📱"},
    "mobility": {"name": "Mobility", "icon": "🚗"},
    "agritech": {"name": "AgriTech", "icon": "🌾"},
    "climate": {"name": "Climate", "icon": "🌍"},
    "gaming": {"name": "Gaming", "icon": "🎮"},
    "govtech": {"name": "GovTech", "icon": "🏛️"},
    "deeptech": {"name": "DeepTech", "icon": "🔬"},
}

INTERESTS = {
    "Generative AI & LLMs": {"keywords": ["genai", "llm", "foundation-models"], "icon": "🤖"},
    "AI Product Strategy": {"keywords": ["product", "strategy", "roadmap"], "icon": "🎯"},
    "AI Safety & Ethics": {"keywords": ["ai-safety", "alignment", "responsible-ai"], "icon": "🛡️"},
    "Enterprise AI": {"keywords": ["enterprise", "automation", "transformation"], "icon": "🏢"},
    "MLOps & Infra": {"keywords": ["infrastructure", "mlops", "deployment"], "icon": "⚡"},
    "AI Leadership": {"keywords": ["leadership", "team", "hiring"], "icon": "👥"},
    "Startup & VC": {"keywords": ["startup", "funding", "vc"], "icon": "💰"},
    "Research": {"keywords": ["research", "papers", "innovation"], "icon": "🔬"},
}

GOALS = {
    "networking": {"name": "Networking", "icon": "🤝"},
    "learning": {"name": "Learning", "icon": "📚"},
    "strategy": {"name": "Strategy", "icon": "🎯"},
    "hiring": {"name": "Hiring", "icon": "👔"},
    "investment": {"name": "Investment", "icon": "💰"},
    "partnerships": {"name": "Partnerships", "icon": "🤝"},
}

EXPO_ICONS = {
    "Healthcare AI": "🏥",
    "AgriTech": "🌾",
    "FinTech": "💳",
    "EdTech": "📚",
    "Smart Cities": "🏙️",
    "Climate & Sustainability": "🌍",
    "Manufacturing & Industry 4.0": "🏭",
    "Government & Public Services": "🏛️",
    "Startups & Innovation": "🚀",
    "International Pavilions": "🌐",
}


# ----------------------------
# Core logic
# ----------------------------
def calculate_session_score(session, profile):
    score = 0.0
    session_desc = (session.get("description", "") + " " + session.get("title", "")).lower()

    # Interest match
    for topic in session.get("topics", []):
        if topic in profile.get("interests", []):
            score += 4.0

    # Sector match (simple keyword presence)
    for sector_id in profile.get("sectors", []):
        sector_data = SECTORS.get(sector_id, {})
        if sector_data.get("name", "").lower() in session_desc:
            score += 3.0

    # Speaker bonus
    if session.get("speakers"):
        score += 2.0
        top_speakers = ["sundar", "sam altman", "jensen", "demis", "yann", "dario"]
        for speaker in session.get("speakers", []):
            if any(name in speaker.lower() for name in top_speakers):
                score += 5.0
                session["is_vip"] = True

    return score


def generate_itinerary(profile):
    itinerary = {}
    for day in profile.get("days", DAYS):
        day_data = EVENT_DATA.get("daily_schedule", {}).get(day, {})
        sessions = []
        for s in day_data.get("sessions", []):
            s_copy = s.copy()
            s_copy["date"] = day
            s_copy["score"] = calculate_session_score(s_copy, profile)
            sessions.append(s_copy)

        sessions.sort(key=lambda x: x["score"], reverse=True)
        itinerary[day] = sessions[:5]
    return itinerary


def generate_whatsapp_message(profile, itinerary):
    track = profile.get("track", "product")
    role_id = profile.get("role", "pm")
    role_name = ROLES.get(track, {}).get(role_id, {}).get("full", "Attendee")

    msg = "🇮🇳 *My AI Summit 2026 Schedule*\n\n"
    msg += f"👤 {profile.get('name', 'Attendee')} | {role_name}\n"
    msg += "📍 Bharat Mandapam, New Delhi\n\n"

    for day, sessions in itinerary.items():
        if sessions:
            msg += f"*{DAY_INFO[day]['name']}*\n"
            for s in sessions[:3]:
                title = (s.get("title", "") or "")[:30]
                msg += f"• {s.get('time', 'TBA')} - {title}...\n"
            msg += "\n"

    msg += "📱 Get yours: https://planner.streamlit.app"
    return msg


def generate_pdf_html(profile, itinerary):
    track = profile.get("track", "product")
    role_id = profile.get("role", "pm")
    role_name = ROLES.get(track, {}).get(role_id, {}).get("full", "Attendee")

    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>AI Summit 2026</title>
<style>
body{{font-family:Arial;margin:40px;color:#1a1a1a}}
.header{{text-align:center;border-bottom:3px solid #667eea;padding-bottom:20px;margin-bottom:20px}}
.day{{margin-bottom:20px}}
.day-header{{background:#667eea;color:white;padding:10px;border-radius:8px 8px 0 0}}
.sessions{{border:1px solid #e5e7eb;border-top:none;border-radius:0 0 8px 8px}}
.session{{padding:10px;border-bottom:1px solid #e5e7eb}}
.vip{{background:#fffbeb}}
</style></head><body>
<div class="header">
<h1>🇮🇳 India AI Impact Summit 2026</h1>
<p>{profile.get('name', 'Attendee')} | {role_name}</p>
</div>
"""

    for day, sessions in itinerary.items():
        if sessions:
            html += f'<div class="day"><div class="day-header"><strong>{DAY_INFO[day]["name"]}</strong> - {DAY_INFO[day]["theme"]}</div><div class="sessions">'
            for s in sessions:
                vip = "vip" if s.get("is_vip") else ""
                html += f'<div class="session {vip}"><strong>{s.get("title","")}</strong><br>🕐 {s.get("time", "TBA")}</div>'
            html += "</div></div>"

    html += '<div style="text-align:center;margin-top:30px;color:#999"><p>Created by Abhishek Takkhi</p></div></body></html>'
    return html


# ----------------------------
# UI renderers
# ----------------------------
def render_logo():
    md_html("""
<div class="logo-header">
  <div class="logo-left">
    <div class="logo-icon">🇮🇳</div>
    <div class="logo-text">
      <h1>India AI Impact Summit</h1>
      <p>Feb 16-20, 2026 • Bharat Mandapam, New Delhi</p>
    </div>
  </div>
  <div class="logo-badge">Official Planner</div>
</div>
""")


def render_hero():
    md_html("""
<div class="hero-section">
  <div class="hero-eyebrow">✨ Free • No signup • 30 seconds</div>

  <h1 class="hero-title">
    700+ Sessions.<br>
    <span>One Perfect Schedule.</span>
  </h1>

  <p class="hero-hook">
    Stop scrolling through endless agendas.<br>
    Tell us your <strong>role</strong>, <strong>sector</strong> & <strong>goals</strong> — we'll build your <strong>personalized AI Summit itinerary</strong> with VIP sessions, networking hotspots & venue navigation.
  </p>

  <div class="audience-row">
    <span class="audience-pill pill-pm">📱 PMs • SPMs • Directors • VPs • CPOs</span>
    <span class="audience-pill pill-eng">⚙️ Engineers • DSs • MLEs • Tech Leads • CTOs</span>
  </div>

  <div class="stats-row">
    <div class="stat-item">
      <div class="stat-number">700+</div>
      <div class="stat-label">Sessions</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">3,250+</div>
      <div class="stat-label">Speakers</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">31</div>
      <div class="stat-label">VIP Sessions</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">10</div>
      <div class="stat-label">Expo Halls</div>
    </div>
  </div>
</div>
""")


def render_questionnaire():
    if "step" not in st.session_state:
        st.session_state.step = 1
    if "profile" not in st.session_state:
        st.session_state.profile = {}

    step = st.session_state.step
    st.progress(step / 6)
    md_html(f"<p style='text-align:center;color:#64748b;margin:0.75rem 0 1.25rem;'>Step {step} of 6</p>")

    if step == 1:
        md_html("""
<div class="question-card">
  <div class="question-header">
    <div class="question-number">1</div>
    <div class="question-title">Choose your track</div>
  </div>
  <p class="question-subtitle">We'll show roles and recommendations specific to your career path</p>
</div>
""")

        c1, c2 = st.columns(2)
        with c1:
            if st.button("📱 Product & Strategy\n\nAPM → PM → SPM → GPM → Director → VP → CPO", use_container_width=True):
                st.session_state.profile["track"] = "product"
                st.session_state.step = 2
                st.rerun()
        with c2:
            if st.button("⚙️ Engineering & Data\n\nSDE → Staff → TL → EM → DS → MLE → Architect → CTO", use_container_width=True):
                st.session_state.profile["track"] = "engineering"
                st.session_state.step = 2
                st.rerun()

    elif step == 2:
        track = st.session_state.profile.get("track", "product")
        track_roles = ROLES.get(track, {})

        md_html("""
<div class="question-card">
  <div class="question-header">
    <div class="question-number">2</div>
    <div class="question-title">Your role & details</div>
  </div>
  <p class="question-subtitle">Select your current level</p>
</div>
""")

        name = st.text_input("Your Name", placeholder="Enter your name")
        phone = st.text_input("WhatsApp (optional)", placeholder="+91 98765 43210", help="Get schedule on WhatsApp")

        st.markdown("**Select your role:**")
        cols = st.columns(4)
        selected_role = None
        for i, (role_id, role_data) in enumerate(track_roles.items()):
            with cols[i % 4]:
                btn_label = f"{role_data['icon']} {role_data['name']}\n({role_data['level']})"
                if st.button(btn_label, key=f"role_{role_id}", use_container_width=True):
                    selected_role = role_id

        if selected_role:
            st.session_state.profile["name"] = name or "Attendee"
            st.session_state.profile["phone"] = phone
            st.session_state.profile["role"] = selected_role
            st.session_state.step = 3
            st.rerun()

        if st.button("← Back"):
            st.session_state.step = 1
            st.rerun()

    elif step == 3:
        md_html("""
<div class="question-card">
  <div class="question-header">
    <div class="question-number">3</div>
    <div class="question-title">Which sector(s) are you from?</div>
  </div>
  <p class="question-subtitle">Helps us match industry-specific sessions</p>
</div>
""")

        selected_sectors = []
        cols = st.columns(4)
        for i, (sector_id, sector_data) in enumerate(SECTORS.items()):
            with cols[i % 4]:
                if st.checkbox(f"{sector_data['icon']} {sector_data['name']}", key=f"sector_{sector_id}"):
                    selected_sectors.append(sector_id)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("← Back", use_container_width=True):
                st.session_state.step = 2
                st.rerun()
        with c2:
            if st.button("Next →", use_container_width=True):
                st.session_state.profile["sectors"] = selected_sectors
                st.session_state.step = 4
                st.rerun()

    elif step == 4:
        md_html("""
<div class="question-card">
  <div class="question-header">
    <div class="question-number">4</div>
    <div class="question-title">Interests</div>
  </div>
  <p class="question-subtitle">What topics excite you?</p>
</div>
""")

        selected_interests = []
        cols = st.columns(2)
        for i, (name, data) in enumerate(INTERESTS.items()):
            with cols[i % 2]:
                if st.checkbox(f"{data['icon']} {name}", key=f"int_{name}"):
                    selected_interests.extend(data["keywords"])

        c1, c2 = st.columns(2)
        with c1:
            if st.button("← Back", use_container_width=True):
                st.session_state.step = 3
                st.rerun()
        with c2:
            if st.button("Next →", use_container_width=True):
                st.session_state.profile["interests"] = selected_interests if selected_interests else ["general"]
                st.session_state.step = 5
                st.rerun()

    elif step == 5:
        md_html("""
<div class="question-card">
  <div class="question-header">
    <div class="question-number">5</div>
    <div class="question-title">Goals</div>
  </div>
  <p class="question-subtitle">Why are you attending?</p>
</div>
""")

        selected_goals = []
        cols = st.columns(3)
        for i, (goal_id, goal_data) in enumerate(GOALS.items()):
            with cols[i % 3]:
                if st.checkbox(f"{goal_data['icon']} {goal_data['name']}", key=f"goal_{goal_id}"):
                    selected_goals.append(goal_id)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("← Back", use_container_width=True):
                st.session_state.step = 4
                st.rerun()
        with c2:
            if st.button("Next →", use_container_width=True):
                st.session_state.profile["goals"] = selected_goals if selected_goals else ["learning"]
                st.session_state.step = 6
                st.rerun()

    elif step == 6:
        md_html("""
<div class="question-card">
  <div class="question-header">
    <div class="question-number">6</div>
    <div class="question-title">Which days will you attend?</div>
  </div>
</div>
""")

        selected_days = []
        cols = st.columns(5)
        for col, day in zip(cols, DAYS):
            with col:
                info = DAY_INFO[day]
                if st.checkbox(f"{info['name'][:3]}\n{info['short']}", value=True, key=f"day_{day}"):
                    selected_days.append(day)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("← Back", use_container_width=True):
                st.session_state.step = 5
                st.rerun()
        with c2:
            if st.button("🚀 Generate My Schedule", use_container_width=True):
                st.session_state.profile["days"] = selected_days if selected_days else DAYS
                st.session_state.itinerary = generate_itinerary(st.session_state.profile)
                st.session_state.step = 7
                st.rerun()


def render_itinerary():
    profile = st.session_state.profile
    itinerary = st.session_state.get("itinerary", {})

    track = profile.get("track", "product")
    role_id = profile.get("role", "pm")
    role_data = ROLES.get(track, {}).get(role_id, {})
    sectors = [SECTORS.get(s, {}).get("name", s) for s in profile.get("sectors", [])]

    md_html(f"""
<div style="text-align:center;padding:1rem 0 1.5rem;">
  <h2 style="font-size:1.6rem;font-weight:700;color:#0f172a;margin-bottom:0.5rem;">
    ✨ {profile.get('name', 'Your')}'s AI Summit Schedule
  </h2>
  <p style="color:#64748b;">
    <span class="badge badge-{'pm' if track == 'product' else 'eng'}">{role_data.get('icon', '')} {role_data.get('full', '')}</span>
    {' '.join([f'<span class="topic-tag">{s}</span>' for s in sectors[:3]])}
  </p>
</div>
""")

    st.markdown("### 📤 Share Your Schedule")
    c1, c2, c3 = st.columns(3)

    with c1:
        wa_msg = generate_whatsapp_message(profile, itinerary)
        wa_link = f"https://wa.me/?text={quote(wa_msg)}"
        if profile.get("phone"):
            phone = profile["phone"].replace(" ", "").replace("-", "")
            if not phone.startswith("+"):
                phone = "+91" + phone
            wa_link = f"https://wa.me/{phone}?text={quote(wa_msg)}"
        md_html(f'<a href="{wa_link}" target="_blank" class="action-btn btn-whatsapp">📱 WhatsApp</a>')

    with c2:
        pdf_html = generate_pdf_html(profile, itinerary)
        b64 = base64.b64encode(pdf_html.encode()).decode()
        md_html(f'<a href="data:text/html;base64,{b64}" download="schedule.html" class="action-btn btn-pdf">📄 Download</a>')

    with c3:
        md_html('<div class="action-btn btn-share">🔗 Share Link</div>')

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Role", role_data.get("name", ""))
    c2.metric("Sectors", len(profile.get("sectors", [])))
    c3.metric("Days", len(profile.get("days", [])))
    c4.metric("Sessions", sum(len(s) for s in itinerary.values()))

    st.markdown("---")

    if profile.get("days"):
        tabs = st.tabs([f"{DAY_INFO[d]['name']} ({DAY_INFO[d]['short']})" for d in profile["days"]])

        for tab, day in zip(tabs, profile["days"]):
            with tab:
                md_html(f'<div style="padding:0.75rem;background:#f8fafc;border-radius:12px;margin-bottom:1rem;"><strong>🎪 {DAY_INFO[day]["theme"]}</strong></div>')

                sessions = itinerary.get(day, [])
                if not sessions:
                    st.info("No highly matched sessions.")
                    continue

                for s in sessions:
    score = s.get("score", 0)
    is_vip = s.get("is_vip", False)

    with st.expander(f"**{s.get('title','')}** | {s.get('time', 'TBA')} {'⭐' if is_vip else ''}"):
        c1, c2 = st.columns([2, 1])

        with c1:
            st.write(s.get("description", ""))
            if s.get("speakers"):
                st.write(f"**Speakers:** {', '.join(s['speakers'][:3])}")
            md_html(" ".join([f'<span class="topic-tag">{t}</span>' for t in s.get("topics", [])[:5]]))

        with c2:
            if is_vip:
                md_html('<span class="badge badge-vip">⭐ VIP Session</span>')

            md_html(
                f'<span class="badge badge-{"high" if score > 10 else "medium"}">'
                f'✓ {"High" if score > 10 else "Good"} Match</span>'
            )

            hall = s.get("hall") or s.get("hall_name") or s.get("room")

            if hall and venue:
                st.write(f"📍 {hall} • {venue}")
            elif hall:
                st.write(f"📍 {hall}")
            elif venue:
                st.write(f"📍 {venue}")

            st.progress(min(score / 20, 1.0))


    st.markdown("---")
    if st.button("🔄 Start Over", use_container_width=True):
        st.session_state.step = 1
        st.session_state.profile = {}
        st.session_state.itinerary = {}
        st.rerun()


def render_venue_map():
    md_html("""
<div style="text-align:center;padding:1.5rem 0;">
  <h2 style="font-size:1.5rem;font-weight:700;color:#0f172a;">🗺️ Venue Map & Access Guide</h2>
  <p style="color:#64748b;">Know where to go and what you can access</p>
</div>
""")

    md_html("""
<div style="display:flex;justify-content:center;gap:1rem;margin-bottom:1.5rem;flex-wrap:wrap;">
  <span class="badge badge-public">🟢 Public Access</span>
  <span class="badge badge-vip">⭐ VIP/Delegate Only</span>
  <span class="badge badge-restricted">🔴 Restricted</span>
</div>
""")

    for _, venue in VENUE_MAP.items():
        access_class = f"access-{venue['access']}"
        access_label = "Public Access" if venue["access"] == "public" else "VIP/Delegate Only" if venue["access"] == "vip" else "Restricted"

        md_html(f"""
<div class="venue-card">
  <div class="venue-header">
    <div class="venue-name">{venue['icon']} {venue['name']}</div>
    <span class="venue-access {access_class}">{access_label}</span>
  </div>
  <div class="venue-details">
    <strong>Sessions:</strong> {', '.join(venue.get('sessions', [])[:3])}
  </div>
  <div class="venue-tip">💡 {venue.get('tip', '')}</div>
</div>
""")

    st.markdown("### 🚪 Entry Gates")
    md_html("<p style='color:#64748b;'>Helpdesks available at marked gates</p>")

    cols = st.columns(4)
    for i, gate in enumerate(GATES.values()):
        with cols[i % 4]:
            helpdesk = "✅ Helpdesk" if gate["helpdesk"] else ""
            md_html(f"""
<div class="gate-card">
  <div class="gate-number">{gate['name']}</div>
  <div class="gate-name">{gate['location']}</div>
  <div style="font-size:0.7rem;color:#059669;">{helpdesk}</div>
  <div style="font-size:0.7rem;color:#64748b;">Near: {gate['nearest']}</div>
</div>
""")
            st.write("")

    st.markdown("### 💡 Navigation Tips")
    tips = [
        "🅿️ **Parking**: JLN Parking is 5.1 km away - plan extra time",
        "🍔 **Food Courts**: Available near Hall 6, Hall 11, Plenary Hall B, and East Plaza",
        "🚶 **Walking**: Halls 1-5 are connected via East Plaza (10-15 min walk end-to-end)",
        "📱 **Best Gate**: Use Gate 7 for Bharat Mandapam, Gate 1/4 for Halls 3-6",
        "⭐ **VIP Access**: Plenary Hall B requires VIP/Delegate badge - check your registration",
    ]
    for tip in tips:
        st.markdown(f"- {tip}")


def render_expo():
    md_html("""
<div style="text-align:center;padding:1.5rem 0;">
  <h2>🏛️ Expo Pavilions</h2>
  <p style="color:#64748b;">300+ exhibitors across 10 halls</p>
</div>
""")

    pavilions = EVENT_DATA.get("expo_pavilions", [])
    cols = st.columns(3)
    for i, p in enumerate(pavilions):
        with cols[i % 3]:
            icon = EXPO_ICONS.get(p.get("name", ""), "📍")
            md_html(f"""
<div class="expo-card">
  <div class="expo-icon">{icon}</div>
  <div class="expo-title">{p.get("name","")}</div>
  <div class="expo-tags">{", ".join(p.get("focus", [])[:3])}</div>
</div>
""")
            st.write("")


def render_speakers():
    md_html("""
<div style="text-align:center;padding:1.5rem 0;">
  <h2>🎤 Featured Speakers</h2>
</div>
""")

    speakers = EVENT_DATA.get("speakers", [])
    cols = st.columns(2)
    for i, s in enumerate(speakers):
        with cols[i % 2]:
            md_html(f"""
<div class="session-card">
  <div class="session-title">{s.get("name","")}</div>
  <div class="session-meta">{s.get("title","")}, {s.get("company","")}</div>
</div>
""")


def render_community():
    md_html("""
<div style="text-align:center;padding:1.5rem 0;">
  <h2>👥 Community Schedules</h2>
</div>
""")

    data = load_community_data()
    if not data.get("itineraries"):
        st.info("No shared schedules yet. Be the first!")
    else:
        for entry in data["itineraries"][-5:][::-1]:
            with st.expander(f"**{entry.get('name', 'User')}** | {entry.get('role', '')}"):
                st.write(f"Sectors: {', '.join(entry.get('sectors', []))}")


def render_footer():
    md_html("""
<div class="footer">
  <p style="font-size:1.1rem;"><strong>🇮🇳 India AI Impact Summit 2026</strong></p>
  <p style="opacity:0.8;">Feb 16-20 • Bharat Mandapam • Pragati Maidan, New Delhi</p>
  <p style="opacity:0.6;font-size:0.85rem;">सर्वजन हिताय | सर्वजन सुखाय</p>
  <p style="opacity:0.6;font-size:0.8rem;">Welfare for All | Happiness of All</p>
  <div class="creator-section">
    <p><strong>Created by Abhishek Takkhi</strong></p>
    <p><a href="https://www.linkedin.com/in/abhishek-t-922055391/" target="_blank">🔗 Connect on LinkedIn</a></p>
  </div>
</div>
""")


# ----------------------------
# Main
# ----------------------------
def main():
    render_logo()

    if st.session_state.get("step", 1) <= 6:
        render_hero()
        render_questionnaire()
    else:
        tabs = st.tabs(["📋 My Schedule", "🗺️ Venue Map", "🏛️ Expo", "🎤 Speakers", "👥 Community"])
        with tabs[0]:
            render_itinerary()
        with tabs[1]:
            render_venue_map()
        with tabs[2]:
            render_expo()
        with tabs[3]:
            render_speakers()
        with tabs[4]:
            render_community()

    render_footer()


if __name__ == "__main__":
    main()
