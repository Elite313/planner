"""
AI Summit Navigator - Premium Edition
Personalized itinerary for Product Managers, Tech Leaders & Engineers
India AI Impact Summit 2026
"""

import streamlit as st
import json
import os
from datetime import datetime
import hashlib
import base64
from urllib.parse import quote

# Page config
st.set_page_config(
    page_title="AI Summit Planner | India AI Impact Summit 2026",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

    .stApp {
        background-color: #FFFFFF;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Logo Section */
    .logo-section {
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 1rem;
    }

    .logo-section img {
        max-height: 80px;
        margin-bottom: 0.5rem;
    }

    .logo-badge {
        display: inline-block;
        background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
        color: white;
        padding: 0.25rem 1rem;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    /* Hero */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #1a1a1a;
        line-height: 1.1;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: #5C5C5A;
        font-weight: 400;
        margin-bottom: 1.5rem;
    }

    .hero-stats {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1rem;
        color: #1a1a1a;
        background: #f8f9fa;
        padding: 0.75rem 1.25rem;
        border-radius: 12px;
        display: inline-block;
        margin-bottom: 1.5rem;
    }

    /* Target Audience Badge */
    .audience-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 100px;
        font-size: 0.85rem;
        font-weight: 500;
        margin: 0.25rem;
    }

    /* Stats Cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        padding: 1.25rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }

    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
    }

    .stat-label {
        font-size: 0.8rem;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Question Card */
    .question-card {
        background: #ffffff;
        border: 2px solid #e5e7eb;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
    }

    .question-card:hover {
        border-color: #667eea;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.1);
    }

    .question-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }

    .question-subtitle {
        font-size: 0.9rem;
        color: #6b7280;
        margin-bottom: 1rem;
    }

    /* Session Cards */
    .session-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 1.25rem;
        margin: 0.75rem 0;
        transition: all 0.2s ease;
    }

    .session-card:hover {
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        transform: translateY(-2px);
    }

    .session-card.vip {
        border: 2px solid #f59e0b;
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
    }

    .session-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }

    .session-meta {
        font-size: 0.85rem;
        color: #6b7280;
        display: flex;
        gap: 1rem;
        margin-bottom: 0.5rem;
    }

    /* Badges */
    .match-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.4rem 0.8rem;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    .match-high { background: #d1fae5; color: #065f46; }
    .match-medium { background: #fef3c7; color: #92400e; }
    .match-low { background: #f3f4f6; color: #4b5563; }

    .vip-badge {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 100px;
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
    }

    .role-badge {
        background: #ede9fe;
        color: #5b21b6;
        padding: 0.25rem 0.75rem;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 500;
        margin: 0.125rem;
    }

    .topic-tag {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        background: #ede9fe;
        color: #5b21b6;
        border-radius: 100px;
        font-size: 0.7rem;
        font-weight: 500;
        margin: 0.1rem;
    }

    .speaker-tag {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.4rem 0.8rem;
        background: #f3f4f6;
        border-radius: 8px;
        font-size: 0.8rem;
        margin: 0.2rem;
    }

    /* Action Buttons */
    .action-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.2s ease;
        text-decoration: none;
        border: none;
    }

    .btn-whatsapp {
        background: #25D366;
        color: white;
    }

    .btn-whatsapp:hover {
        background: #128C7E;
        transform: translateY(-2px);
    }

    .btn-pdf {
        background: #dc2626;
        color: white;
    }

    .btn-pdf:hover {
        background: #b91c1c;
        transform: translateY(-2px);
    }

    .btn-share {
        background: #3b82f6;
        color: white;
    }

    .btn-share:hover {
        background: #2563eb;
        transform: translateY(-2px);
    }

    /* Expo Card */
    .expo-card {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.25rem;
        text-align: center;
        transition: all 0.2s ease;
        height: 100%;
    }

    .expo-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
    }

    .expo-icon { font-size: 2rem; margin-bottom: 0.75rem; }
    .expo-title { font-size: 1rem; font-weight: 600; color: #1a1a1a; margin-bottom: 0.4rem; }
    .expo-tags { font-size: 0.75rem; color: #6b7280; }

    /* Feature Badge */
    .feature-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.4rem 0.8rem;
        background: #f0fdf4;
        color: #166534;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-bottom: 0.75rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 1px solid #e5e7eb;
        color: #9ca3af;
        font-size: 0.85rem;
    }

    /* Streamlit Overrides */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.6rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }

    .stSelectbox > div > div, .stMultiSelect > div > div {
        border-radius: 12px;
        border: 2px solid #e5e7eb;
    }

    div[data-testid="stExpander"] {
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        overflow: hidden;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: #f8f9fa;
        padding: 0.5rem;
        border-radius: 12px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.6rem 1.25rem;
        font-weight: 500;
    }

    .stTabs [aria-selected="true"] {
        background: white;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .stProgress > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 100px;
    }

    /* Print styles for PDF */
    @media print {
        .no-print { display: none !important; }
        .stApp { background: white !important; }
    }
</style>
""", unsafe_allow_html=True)


# Load event data
@st.cache_data
def load_event_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "event_data.json")
    with open(data_path, "r") as f:
        return json.load(f)

EVENT_DATA = load_event_data()

# Community storage
COMMUNITY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "community_itineraries.json")

def load_community_data():
    if os.path.exists(COMMUNITY_FILE):
        with open(COMMUNITY_FILE, "r") as f:
            return json.load(f)
    return {"itineraries": [], "comments": []}

def save_community_data(data):
    with open(COMMUNITY_FILE, "w") as f:
        json.dump(data, f, indent=2)


# Constants
DAYS = ["2026-02-16", "2026-02-17", "2026-02-18", "2026-02-19", "2026-02-20"]
DAY_INFO = {
    "2026-02-16": {"short": "Feb 16", "name": "Monday", "theme": "Expo Launch & Inauguration"},
    "2026-02-17": {"short": "Feb 17", "name": "Tuesday", "theme": "Sectoral Deep Dives"},
    "2026-02-18": {"short": "Feb 18", "name": "Wednesday", "theme": "Research & Innovation"},
    "2026-02-19": {"short": "Feb 19", "name": "Thursday", "theme": "Summit Opening & CEOs"},
    "2026-02-20": {"short": "Feb 20", "name": "Friday", "theme": "Global Cooperation"},
}

# Roles focused on PM, Leaders, Tech
ROLES = {
    "pm": {
        "name": "Product Manager",
        "icon": "📱",
        "keywords": ["product", "roadmap", "strategy", "user", "market"],
        "recommended_tracks": ["economic_dev", "resilience", "human_capital"]
    },
    "tech_lead": {
        "name": "Tech Lead / Engineering Manager",
        "icon": "👨‍💻",
        "keywords": ["engineering", "architecture", "technical", "team", "delivery"],
        "recommended_tracks": ["science", "democratizing", "safe_ai"]
    },
    "engineer": {
        "name": "Software Engineer / Developer",
        "icon": "⚙️",
        "keywords": ["code", "development", "implementation", "technical", "build"],
        "recommended_tracks": ["science", "democratizing", "resilience"]
    },
    "founder": {
        "name": "Founder / CXO",
        "icon": "🚀",
        "keywords": ["startup", "business", "vision", "investment", "growth"],
        "recommended_tracks": ["economic_dev", "resilience", "inclusion"]
    },
    "vp_director": {
        "name": "VP / Director",
        "icon": "📊",
        "keywords": ["strategy", "leadership", "transformation", "scale", "operations"],
        "recommended_tracks": ["economic_dev", "resilience", "safe_ai"]
    },
    "researcher": {
        "name": "AI/ML Researcher",
        "icon": "🔬",
        "keywords": ["research", "papers", "models", "experiments", "innovation"],
        "recommended_tracks": ["science", "democratizing", "safe_ai"]
    },
    "data_scientist": {
        "name": "Data Scientist / ML Engineer",
        "icon": "📈",
        "keywords": ["data", "models", "analytics", "ml", "insights"],
        "recommended_tracks": ["science", "economic_dev", "democratizing"]
    },
    "architect": {
        "name": "Solutions / Enterprise Architect",
        "icon": "🏗️",
        "keywords": ["architecture", "enterprise", "integration", "systems", "design"],
        "recommended_tracks": ["resilience", "democratizing", "safe_ai"]
    },
}

# Interests
INTERESTS = {
    "Generative AI & LLMs": {
        "keywords": ["genai", "llm", "foundation-models", "chatgpt"],
        "icon": "🤖",
        "for_roles": ["engineer", "researcher", "data_scientist", "pm"]
    },
    "AI Product Strategy": {
        "keywords": ["product", "strategy", "roadmap", "market", "user"],
        "icon": "🎯",
        "for_roles": ["pm", "founder", "vp_director"]
    },
    "AI Safety & Ethics": {
        "keywords": ["ai-safety", "alignment", "responsible-ai", "ethics"],
        "icon": "🛡️",
        "for_roles": ["pm", "tech_lead", "vp_director", "researcher"]
    },
    "Enterprise AI Adoption": {
        "keywords": ["enterprise", "automation", "transformation", "scale"],
        "icon": "🏢",
        "for_roles": ["architect", "vp_director", "tech_lead", "pm"]
    },
    "AI Infrastructure & MLOps": {
        "keywords": ["infrastructure", "mlops", "deployment", "scale", "computing"],
        "icon": "⚡",
        "for_roles": ["engineer", "architect", "tech_lead", "data_scientist"]
    },
    "Leadership & Team Building": {
        "keywords": ["leadership", "team", "culture", "hiring", "management"],
        "icon": "👥",
        "for_roles": ["tech_lead", "vp_director", "founder"]
    },
    "Startup & VC Insights": {
        "keywords": ["startup", "funding", "vc", "growth", "entrepreneurship"],
        "icon": "💰",
        "for_roles": ["founder", "pm", "vp_director"]
    },
    "Research & Innovation": {
        "keywords": ["research", "papers", "innovation", "cutting-edge", "science"],
        "icon": "🔬",
        "for_roles": ["researcher", "data_scientist", "engineer"]
    },
    "Healthcare AI": {
        "keywords": ["healthcare", "medical", "diagnostics", "health"],
        "icon": "🏥",
        "for_roles": ["pm", "researcher", "founder"]
    },
    "FinTech & AI": {
        "keywords": ["fintech", "finance", "trading", "banking", "payments"],
        "icon": "💳",
        "for_roles": ["pm", "architect", "founder"]
    },
}

# Goals with networking scores
GOALS = {
    "networking": {
        "name": "Maximize Networking",
        "desc": "Meet industry leaders, potential partners & collaborators",
        "icon": "🤝",
        "score_boost": {"speakers": 5, "roundtable": 4, "ceo": 5}
    },
    "learning": {
        "name": "Deep Technical Learning",
        "desc": "Master new AI concepts, tools & techniques",
        "icon": "📚",
        "score_boost": {"workshop": 4, "technical": 3, "hands-on": 4}
    },
    "strategy": {
        "name": "Strategic Insights",
        "desc": "Understand market trends, competition & opportunities",
        "icon": "🎯",
        "score_boost": {"strategy", "market", "trends", "future"}
    },
    "hiring": {
        "name": "Talent & Hiring",
        "desc": "Find talent, build team, understand hiring landscape",
        "icon": "👔",
        "score_boost": {"talent", "hiring", "career", "skills"}
    },
    "investment": {
        "name": "Investment & Funding",
        "desc": "Meet investors, explore funding opportunities",
        "icon": "💰",
        "score_boost": {"investment", "funding", "vc", "startup"}
    },
    "partnerships": {
        "name": "Business Partnerships",
        "desc": "Explore B2B partnerships and collaborations",
        "icon": "🤝",
        "score_boost": {"partnership", "collaboration", "enterprise", "b2b"}
    },
}

# Company sizes for context
COMPANY_SIZES = [
    "Startup (1-50)",
    "Scale-up (51-200)",
    "Mid-size (201-1000)",
    "Enterprise (1000+)",
    "Freelance / Solo",
]

EXPO_ICONS = {
    "Healthcare AI": "🏥", "AgriTech": "🌾", "FinTech": "💳", "EdTech": "📚",
    "Smart Cities": "🏙️", "Climate & Sustainability": "🌍", "Manufacturing & Industry 4.0": "🏭",
    "Government & Public Services": "🏛️", "Startups & Innovation": "🚀", "International Pavilions": "🌐",
}


def calculate_session_score(session, profile):
    """Calculate relevance score with role-based weighting"""
    score = 0.0
    networking_roi = 0.0
    pm_relevance = 0.0
    tech_relevance = 0.0

    role_data = ROLES.get(profile.get("role", ""), {})
    role_keywords = role_data.get("keywords", [])

    # Level match
    session_level = session.get("level", "all")
    proficiency = profile.get("proficiency", "intermediate")

    if session_level == "all":
        score += 3.0
    elif session_level == proficiency:
        score += 5.0
    elif proficiency == "intermediate":
        score += 2.0

    # Topic match
    session_topics = session.get("topics", [])
    session_desc = (session.get("description", "") + " " + session.get("title", "")).lower()
    user_interests = profile.get("interests", [])

    for topic in session_topics:
        if topic in user_interests:
            score += 4.0

    # Role-specific keywords
    for keyword in role_keywords:
        if keyword in session_desc:
            score += 2.0
            if profile.get("role") in ["pm", "vp_director", "founder"]:
                pm_relevance += 2.0
            else:
                tech_relevance += 2.0

    # Goal-based scoring
    user_goals = profile.get("goals", [])

    if "networking" in user_goals:
        networking_keywords = ["ceo", "roundtable", "leaders", "networking", "connect"]
        for kw in networking_keywords:
            if kw in session_desc:
                networking_roi += 3.0
                score += 2.0

    if "learning" in user_goals:
        for kw in ["workshop", "technical", "deep-dive", "hands-on"]:
            if kw in session_desc:
                score += 2.0
                tech_relevance += 2.0

    if "strategy" in user_goals:
        for kw in ["strategy", "market", "trends", "future", "roadmap"]:
            if kw in session_desc:
                score += 2.0
                pm_relevance += 2.0

    # Speaker bonus
    if session.get("speakers"):
        score += 2.0
        networking_roi += 3.0
        top_speakers = ["sundar", "sam altman", "jensen", "demis", "yann", "dario", "satya"]
        for speaker in session.get("speakers", []):
            if any(name in speaker.lower() for name in top_speakers):
                score += 5.0
                networking_roi += 5.0
                session["is_vip"] = True

    session["networking_roi"] = networking_roi
    session["pm_relevance"] = pm_relevance
    session["tech_relevance"] = tech_relevance

    return score


def generate_itinerary(profile):
    """Generate personalized itinerary"""
    available_days = profile.get("days", DAYS)
    all_sessions = []

    for day in available_days:
        day_data = EVENT_DATA["daily_schedule"].get(day, {})
        sessions = day_data.get("sessions", [])
        for session in sessions:
            session_copy = session.copy()
            session_copy["date"] = day
            session_copy["day_name"] = day_data.get("day", "")
            session_copy["theme"] = day_data.get("theme", "")
            session_copy["score"] = calculate_session_score(session_copy, profile)
            all_sessions.append(session_copy)

    all_sessions.sort(key=lambda x: x["score"], reverse=True)

    itinerary = {}
    for day in available_days:
        day_sessions = [s for s in all_sessions if s["date"] == day]
        itinerary[day] = day_sessions[:5]

    return itinerary


def generate_whatsapp_message(profile, itinerary):
    """Generate WhatsApp shareable message"""
    role_name = ROLES.get(profile.get("role", ""), {}).get("name", "Attendee")

    msg = f"🤖 *My AI Summit 2026 Schedule*\n"
    msg += f"👤 {profile.get('name', 'Attendee')} | {role_name}\n"
    msg += f"📍 Bharat Mandapam, New Delhi\n"
    msg += f"📅 Feb 16-20, 2026\n\n"

    for day, sessions in itinerary.items():
        if sessions:
            day_info = DAY_INFO.get(day, {})
            msg += f"*{day_info.get('name', '')} ({day_info.get('short', '')})*\n"
            for s in sessions[:3]:
                msg += f"• {s.get('time', 'TBA')} - {s['title'][:40]}...\n"
            msg += "\n"

    msg += "📱 Create yours: https://planner.streamlit.app"
    return msg


def generate_pdf_html(profile, itinerary):
    """Generate HTML for PDF download"""
    role_name = ROLES.get(profile.get("role", ""), {}).get("name", "Attendee")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>AI Summit 2026 - Personalized Schedule</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; color: #1a1a1a; }}
            .header {{ text-align: center; margin-bottom: 30px; border-bottom: 3px solid #667eea; padding-bottom: 20px; }}
            .logo {{ font-size: 28px; font-weight: bold; color: #667eea; }}
            .subtitle {{ color: #666; margin-top: 5px; }}
            .profile {{ background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 25px; }}
            .profile h3 {{ margin: 0 0 10px 0; color: #667eea; }}
            .day {{ margin-bottom: 25px; }}
            .day-header {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 10px 15px; border-radius: 8px 8px 0 0; }}
            .day-header h3 {{ margin: 0; }}
            .day-theme {{ font-size: 0.9em; opacity: 0.9; }}
            .sessions {{ border: 1px solid #e5e7eb; border-top: none; border-radius: 0 0 8px 8px; }}
            .session {{ padding: 12px 15px; border-bottom: 1px solid #e5e7eb; }}
            .session:last-child {{ border-bottom: none; }}
            .session-title {{ font-weight: 600; color: #1a1a1a; }}
            .session-meta {{ font-size: 0.85em; color: #666; margin-top: 3px; }}
            .session-speakers {{ font-size: 0.85em; color: #667eea; margin-top: 3px; }}
            .vip {{ background: #fffbeb; border-left: 3px solid #f59e0b; }}
            .footer {{ text-align: center; margin-top: 30px; color: #999; font-size: 0.85em; }}
            .match {{ display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.75em; font-weight: 600; }}
            .match-high {{ background: #d1fae5; color: #065f46; }}
            .match-medium {{ background: #fef3c7; color: #92400e; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="logo">🤖 India AI Impact Summit 2026</div>
            <div class="subtitle">Personalized Schedule</div>
        </div>

        <div class="profile">
            <h3>👤 {profile.get('name', 'Attendee')}</h3>
            <p><strong>Role:</strong> {role_name}</p>
            <p><strong>Proficiency:</strong> {profile.get('proficiency', 'Intermediate').title()}</p>
            <p><strong>Goals:</strong> {', '.join(profile.get('goals', []))}</p>
        </div>
    """

    for day, sessions in itinerary.items():
        if sessions:
            day_info = DAY_INFO.get(day, {})
            html += f"""
            <div class="day">
                <div class="day-header">
                    <h3>{day_info.get('name', '')} - {day_info.get('short', '')}</h3>
                    <div class="day-theme">🎪 {day_info.get('theme', '')}</div>
                </div>
                <div class="sessions">
            """
            for s in sessions:
                vip_class = "vip" if s.get("is_vip") else ""
                match_class = "match-high" if s.get("score", 0) > 12 else "match-medium"
                speakers = ", ".join(s.get("speakers", [])[:2]) if s.get("speakers") else ""

                html += f"""
                <div class="session {vip_class}">
                    <div class="session-title">
                        {s['title']}
                        <span class="match {match_class}">{'⭐ VIP' if s.get('is_vip') else '✓ Match'}</span>
                    </div>
                    <div class="session-meta">🕐 {s.get('time', 'TBA')} | 📍 {s.get('venue', 'TBA')}</div>
                    {"<div class='session-speakers'>👤 " + speakers + "</div>" if speakers else ""}
                </div>
                """
            html += "</div></div>"

    html += """
        <div class="footer">
            <p>Generated by AI Summit Navigator | https://planner.streamlit.app</p>
            <p>India AI Impact Summit 2026 | Feb 16-20 | Bharat Mandapam, New Delhi</p>
        </div>
    </body>
    </html>
    """
    return html


def render_logo():
    """Render AI Summit logo"""
    st.markdown("""
    <div class="logo-section">
        <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
            <div style="font-size: 2.5rem;">🇮🇳</div>
            <div>
                <div style="font-size: 1.5rem; font-weight: 800; color: #1a1a1a; letter-spacing: -0.02em;">
                    India AI Impact Summit
                </div>
                <div style="font-size: 0.9rem; color: #667eea; font-weight: 600;">2026 | New Delhi</div>
            </div>
        </div>
        <div style="margin-top: 0.75rem;">
            <span class="logo-badge">Official Planner</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_hero():
    """Render hero section"""
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0 2rem 0;">
        <div class="feature-badge">✨ Free · No signup · Takes 30 seconds</div>
        <h1 class="hero-title">Your AI Summit Companion</h1>
        <p class="hero-subtitle">Built for Product Managers, Tech Leaders & Engineers<br>
        Navigate 700+ sessions with a personalized schedule</p>

        <div style="margin-bottom: 1rem;">
            <span class="audience-badge">📱 Product Managers</span>
            <span class="audience-badge">👨‍💻 Tech Leaders</span>
            <span class="audience-badge">⚙️ Engineers</span>
        </div>

        <div class="hero-stats">700+ Sessions · 3,250+ Speakers · 100+ Countries · 5 Days</div>
    </div>
    """, unsafe_allow_html=True)


def render_stats():
    """Render stats cards"""
    col1, col2, col3, col4 = st.columns(4)
    stats = [("700+", "Sessions"), ("3,250+", "Speakers"), ("300+", "Exhibitors"), ("100+", "Countries")]
    for col, (number, label) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{number}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)


def render_questionnaire():
    """Render wizard questionnaire"""
    if "wizard_step" not in st.session_state:
        st.session_state.wizard_step = 1
    if "profile" not in st.session_state:
        st.session_state.profile = {}

    step = st.session_state.wizard_step
    progress = step / 4
    st.progress(progress)
    st.markdown(f"<p style='text-align: center; color: #6b7280; margin-bottom: 1.5rem;'>Step {step} of 4</p>", unsafe_allow_html=True)

    if step == 1:
        st.markdown("""
        <div class="question-card">
            <div class="question-title">👋 Let's personalize your experience</div>
            <div class="question-subtitle">Tell us about yourself and your role</div>
        </div>
        """, unsafe_allow_html=True)

        name = st.text_input("Your Name", placeholder="Enter your name", key="q_name")

        # Phone for WhatsApp
        phone = st.text_input("WhatsApp Number (optional)", placeholder="+91 98765 43210", key="q_phone",
                             help="We'll send your schedule directly to WhatsApp")

        st.markdown("**Your Role**")
        role_cols = st.columns(2)
        selected_role = None
        for i, (role_id, role_data) in enumerate(ROLES.items()):
            with role_cols[i % 2]:
                if st.checkbox(f"{role_data['icon']} {role_data['name']}", key=f"role_{role_id}"):
                    selected_role = role_id

        company_size = st.selectbox("Company Size", ["Select..."] + COMPANY_SIZES, key="q_company")

        proficiency = st.select_slider(
            "AI/Tech Proficiency",
            options=["Beginner", "Intermediate", "Advanced"],
            value="Intermediate",
            key="q_prof"
        )

        col1, col2 = st.columns([1, 1])
        with col2:
            if st.button("Next →", key="next1", use_container_width=True):
                st.session_state.profile["name"] = name or "Attendee"
                st.session_state.profile["phone"] = phone
                st.session_state.profile["role"] = selected_role or "pm"
                st.session_state.profile["company_size"] = company_size
                st.session_state.profile["proficiency"] = proficiency.lower()
                st.session_state.wizard_step = 2
                st.rerun()

    elif step == 2:
        role = st.session_state.profile.get("role", "pm")
        role_name = ROLES.get(role, {}).get("name", "Professional")

        st.markdown(f"""
        <div class="question-card">
            <div class="question-title">🎯 What topics matter to you?</div>
            <div class="question-subtitle">Recommended for {role_name}s - select all that apply</div>
        </div>
        """, unsafe_allow_html=True)

        selected_interests = []
        cols = st.columns(2)

        for i, (interest_name, interest_data) in enumerate(INTERESTS.items()):
            with cols[i % 2]:
                # Highlight if recommended for role
                recommended = role in interest_data.get("for_roles", [])
                label = f"{interest_data['icon']} {interest_name}"
                if recommended:
                    label += " ⭐"

                if st.checkbox(label, value=recommended, key=f"int_{interest_name}"):
                    selected_interests.extend(interest_data["keywords"])

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back", key="back2", use_container_width=True):
                st.session_state.wizard_step = 1
                st.rerun()
        with col2:
            if st.button("Next →", key="next2", use_container_width=True):
                st.session_state.profile["interests"] = selected_interests if selected_interests else ["general"]
                st.session_state.wizard_step = 3
                st.rerun()

    elif step == 3:
        st.markdown("""
        <div class="question-card">
            <div class="question-title">🚀 What do you want to achieve?</div>
            <div class="question-subtitle">We'll optimize your schedule for maximum ROI</div>
        </div>
        """, unsafe_allow_html=True)

        selected_goals = []
        cols = st.columns(2)
        for i, (goal_id, goal_data) in enumerate(GOALS.items()):
            with cols[i % 2]:
                if st.checkbox(f"{goal_data['icon']} **{goal_data['name']}**\n\n{goal_data['desc']}", key=f"goal_{goal_id}"):
                    selected_goals.append(goal_id)

        st.markdown("---")
        st.markdown("**📅 Which days will you attend?**")
        selected_days = []
        day_cols = st.columns(5)
        for col, day in zip(day_cols, DAYS):
            with col:
                info = DAY_INFO[day]
                if st.checkbox(f"{info['name'][:3]}\n{info['short']}", value=True, key=f"day_{day}"):
                    selected_days.append(day)

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back", key="back3", use_container_width=True):
                st.session_state.wizard_step = 2
                st.rerun()
        with col2:
            if st.button("Generate My Schedule ✨", key="next3", use_container_width=True):
                st.session_state.profile["goals"] = selected_goals if selected_goals else ["learning"]
                st.session_state.profile["days"] = selected_days if selected_days else DAYS
                st.session_state.wizard_step = 4
                st.session_state.itinerary = generate_itinerary(st.session_state.profile)
                st.rerun()

    elif step == 4:
        render_itinerary_view()


def render_itinerary_view():
    """Render the generated itinerary with sharing options"""
    profile = st.session_state.profile
    itinerary = st.session_state.get("itinerary", {})
    role_name = ROLES.get(profile.get("role", ""), {}).get("name", "Attendee")
    role_icon = ROLES.get(profile.get("role", ""), {}).get("icon", "👤")

    # Header
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem 0 1.5rem 0;">
        <h2 style="font-size: 1.75rem; font-weight: 700; color: #1a1a1a; margin-bottom: 0.5rem;">
            ✨ {profile.get('name', 'Your')}'s AI Summit Schedule
        </h2>
        <p style="color: #6b7280;">
            <span class="role-badge">{role_icon} {role_name}</span>
            <span class="role-badge">📊 {profile.get('proficiency', 'intermediate').title()}</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Quick Actions - WhatsApp & PDF
    st.markdown("### 📤 Share Your Schedule")
    action_col1, action_col2, action_col3 = st.columns(3)

    with action_col1:
        # WhatsApp Share
        wa_message = generate_whatsapp_message(profile, itinerary)
        wa_link = f"https://wa.me/?text={quote(wa_message)}"

        if profile.get("phone"):
            phone_clean = profile["phone"].replace(" ", "").replace("-", "")
            if not phone_clean.startswith("+"):
                phone_clean = "+91" + phone_clean
            wa_link = f"https://wa.me/{phone_clean}?text={quote(wa_message)}"

        st.markdown(f"""
        <a href="{wa_link}" target="_blank" class="action-btn btn-whatsapp" style="display: block; text-align: center; text-decoration: none;">
            📱 Send to WhatsApp
        </a>
        """, unsafe_allow_html=True)

    with action_col2:
        # PDF Download
        pdf_html = generate_pdf_html(profile, itinerary)
        b64 = base64.b64encode(pdf_html.encode()).decode()
        href = f'<a href="data:text/html;base64,{b64}" download="ai_summit_schedule_{profile.get("name", "schedule").replace(" ", "_")}.html" class="action-btn btn-pdf" style="display: block; text-align: center; text-decoration: none;">📄 Download PDF</a>'
        st.markdown(href, unsafe_allow_html=True)

    with action_col3:
        if st.button("🔗 Share Link", use_container_width=True, key="share_link"):
            st.session_state.show_share = True

    st.markdown("---")

    # Profile summary
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Role", role_name[:15])
    with col2:
        st.metric("Proficiency", profile.get("proficiency", "").title())
    with col3:
        st.metric("Days", len(profile.get("days", [])))
    with col4:
        total_sessions = sum(len(s) for s in itinerary.values())
        st.metric("Sessions", total_sessions)

    st.markdown("---")

    # Day tabs
    if profile.get("days"):
        tabs = st.tabs([f"{DAY_INFO[day]['name']} ({DAY_INFO[day]['short']})" for day in profile["days"]])

        for tab, day in zip(tabs, profile["days"]):
            with tab:
                day_info = DAY_INFO[day]
                st.markdown(f"""
                <div style="padding: 0.75rem; background: #f8f9fa; border-radius: 12px; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #1a1a1a; font-size: 1.1rem;">🎪 {day_info['theme']}</h3>
                </div>
                """, unsafe_allow_html=True)

                sessions = itinerary.get(day, [])
                if not sessions:
                    st.info("No highly matched sessions. Try broadening your interests!")
                    continue

                for session in sessions:
                    score = session.get("score", 0)
                    is_vip = session.get("is_vip", False)
                    networking_roi = session.get("networking_roi", 0)

                    match_class = "match-high" if score > 12 else "match-medium" if score > 6 else "match-low"
                    match_text = "High Match" if score > 12 else "Good Match" if score > 6 else "Relevant"

                    with st.expander(f"**{session['title']}** | {session.get('time', 'TBA')} {'⭐' if is_vip else ''}"):
                        col1, col2 = st.columns([2, 1])

                        with col1:
                            st.markdown(f"**Description:** {session.get('description', 'N/A')}")
                            if session.get("speakers"):
                                st.markdown("**Speakers:**")
                                for speaker in session["speakers"][:3]:
                                    st.markdown(f'<span class="speaker-tag">👤 {speaker}</span>', unsafe_allow_html=True)
                            topics_html = " ".join([f'<span class="topic-tag">{t}</span>' for t in session.get("topics", [])[:5]])
                            st.markdown(f"**Topics:** {topics_html}", unsafe_allow_html=True)

                        with col2:
                            st.markdown(f'<span class="{match_class} match-badge">✓ {match_text}</span>', unsafe_allow_html=True)
                            if is_vip:
                                st.markdown('<span class="vip-badge">⭐ VIP</span>', unsafe_allow_html=True)
                            st.markdown(f"**Level:** {session.get('level', 'all').title()}")
                            if session.get("venue"):
                                st.markdown(f"**Venue:** {session['venue']}")
                            if networking_roi > 3:
                                st.markdown("🤝 **High Networking ROI**")
                            st.progress(min(score / 20, 1.0))
                            st.caption(f"Match: {score:.1f}/20")

    # Bottom actions
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Start Over", use_container_width=True):
            st.session_state.wizard_step = 1
            st.session_state.profile = {}
            st.session_state.itinerary = {}
            st.rerun()

    # Share modal
    if st.session_state.get("show_share"):
        with st.expander("📤 Share to Community", expanded=True):
            share_name = st.text_input("Display Name", value=profile.get("name", ""))
            share_bio = st.text_area("Brief Bio", placeholder="PM at startup, interested in GenAI...")
            if st.button("Share My Schedule"):
                community_data = load_community_data()
                share_entry = {
                    "id": hashlib.md5(f"{share_name}{datetime.now().isoformat()}".encode()).hexdigest()[:8],
                    "name": share_name,
                    "bio": share_bio,
                    "role": role_name,
                    "proficiency": profile.get("proficiency", ""),
                    "interests": list(set(profile.get("interests", [])))[:5],
                    "goals": profile.get("goals", [])[:3],
                    "itinerary": {day: [{"title": s["title"], "time": s.get("time", "TBA")} for s in sessions[:3]] for day, sessions in itinerary.items()},
                    "shared_at": datetime.now().isoformat(),
                }
                community_data["itineraries"].append(share_entry)
                save_community_data(community_data)
                st.success(f"✅ Shared! Code: **{share_entry['id']}**")
                st.session_state.show_share = False


def render_expo_guide():
    """Render expo pavilion guide"""
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0;">
        <h2 style="font-size: 1.75rem; font-weight: 700; color: #1a1a1a;">🏛️ Expo Pavilion Guide</h2>
        <p style="color: #6b7280;">300+ exhibitors across 10 thematic pavilions</p>
    </div>
    """, unsafe_allow_html=True)

    pavilions = EVENT_DATA.get("expo_pavilions", [])
    cols = st.columns(3)
    for i, pavilion in enumerate(pavilions):
        with cols[i % 3]:
            icon = EXPO_ICONS.get(pavilion["name"], "📍")
            st.markdown(f"""
            <div class="expo-card">
                <div class="expo-icon">{icon}</div>
                <div class="expo-title">{pavilion['name']}</div>
                <div class="expo-tags">{', '.join(pavilion.get('focus', [])[:3])}</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("")


def render_speakers():
    """Render speakers section"""
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0;">
        <h2 style="font-size: 1.75rem; font-weight: 700; color: #1a1a1a;">🎤 Featured Speakers</h2>
        <p style="color: #6b7280;">World's top AI minds</p>
    </div>
    """, unsafe_allow_html=True)

    speakers = EVENT_DATA.get("speakers", [])
    cols = st.columns(2)
    for i, speaker in enumerate(speakers):
        with cols[i % 2]:
            topics_html = " ".join([f'<span class="topic-tag">{t}</span>' for t in speaker.get("topics", [])])
            st.markdown(f"""
            <div class="session-card">
                <div class="session-title">{speaker['name']}</div>
                <div class="session-meta">{speaker['title']}, {speaker['company']}</div>
                <div>{topics_html}</div>
            </div>
            """, unsafe_allow_html=True)


def render_community():
    """Render community section"""
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0;">
        <h2 style="font-size: 1.75rem; font-weight: 700; color: #1a1a1a;">👥 Community Schedules</h2>
        <p style="color: #6b7280;">See what other PMs, Leaders & Engineers are planning</p>
    </div>
    """, unsafe_allow_html=True)

    community_data = load_community_data()
    itineraries = community_data.get("itineraries", [])

    if not itineraries:
        st.info("No shared schedules yet. Be the first!")
        return

    filter_role = st.selectbox("Filter by Role", ["All"] + [r["name"] for r in ROLES.values()])

    for entry in itineraries[-10:][::-1]:
        if filter_role != "All" and entry.get("role") != filter_role:
            continue
        with st.expander(f"**{entry['name']}** | {entry.get('role', '')} | {entry.get('shared_at', '')[:10]}"):
            st.markdown(f"*{entry.get('bio', 'No bio')}*")
            st.markdown("**Their Schedule:**")
            for day, sessions in entry.get("itinerary", {}).items():
                st.markdown(f"📅 **{DAY_INFO.get(day, {}).get('name', day)}:**")
                for s in sessions:
                    st.markdown(f"  • {s['title']} ({s['time']})")


def main():
    render_logo()

    if st.session_state.get("wizard_step", 1) < 4:
        render_hero()
        render_stats()
        st.markdown("---")
        render_questionnaire()
    else:
        tab1, tab2, tab3, tab4 = st.tabs(["📋 My Schedule", "🏛️ Expo", "🎤 Speakers", "👥 Community"])
        with tab1:
            render_itinerary_view()
        with tab2:
            render_expo_guide()
        with tab3:
            render_speakers()
        with tab4:
            render_community()

    st.markdown("""
    <div class="footer">
        <p>🇮🇳 <strong>India AI Impact Summit 2026</strong> | Feb 16-20 | Bharat Mandapam, New Delhi</p>
        <p style="margin-top: 0.5rem;">Made with ❤️ for PMs, Tech Leaders & Engineers</p>
        <p style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #e5e7eb;">
            <strong>Created by Abhishek Takkhi</strong>
            <br>
            <a href="https://www.linkedin.com/in/abhishektakkhi/" target="_blank" style="color: #667eea; text-decoration: none; font-weight: 500;">
                🔗 Connect on LinkedIn
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
