"""
AI Summit Navigator - Premium Edition
A beautifully designed personalized itinerary generator for AI Impact Summit 2026
Inspired by modern event planning UX patterns
"""

import streamlit as st
import json
import os
from datetime import datetime
import hashlib

# Page config - White theme
st.set_page_config(
    page_title="AI Summit Planner | India AI Impact Summit 2026",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for white theme and modern styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

    /* Global Styles */
    .stApp {
        background-color: #FFFFFF;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Hero Section */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        color: #1a1a1a;
        line-height: 1.1;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: #5C5C5A;
        font-weight: 400;
        margin-bottom: 2rem;
    }

    .hero-stats {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.1rem;
        color: #1a1a1a;
        background: #f8f9fa;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        display: inline-block;
        margin-bottom: 2rem;
    }

    /* Stats Cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
    }

    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Progress Steps */
    .progress-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 2rem 0;
        padding: 1.5rem;
        background: #f8f9fa;
        border-radius: 16px;
    }

    .step {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        color: #9ca3af;
    }

    .step.active {
        color: #1a1a1a;
    }

    .step.completed {
        color: #10b981;
    }

    .step-number {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: #e5e7eb;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        font-size: 0.875rem;
    }

    .step.active .step-number {
        background: #1a1a1a;
        color: white;
    }

    .step.completed .step-number {
        background: #10b981;
        color: white;
    }

    /* Question Cards */
    .question-card {
        background: #ffffff;
        border: 2px solid #e5e7eb;
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        transition: all 0.2s ease;
    }

    .question-card:hover {
        border-color: #667eea;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.1);
    }

    .question-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }

    .question-subtitle {
        font-size: 0.95rem;
        color: #6b7280;
        margin-bottom: 1.5rem;
    }

    /* Option Pills */
    .option-pill {
        display: inline-block;
        padding: 0.75rem 1.25rem;
        margin: 0.25rem;
        border: 2px solid #e5e7eb;
        border-radius: 100px;
        cursor: pointer;
        transition: all 0.2s ease;
        font-weight: 500;
        color: #374151;
    }

    .option-pill:hover {
        border-color: #667eea;
        background: #f5f3ff;
    }

    .option-pill.selected {
        border-color: #667eea;
        background: #667eea;
        color: white;
    }

    /* Session Cards */
    .session-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
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
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }

    .session-meta {
        font-size: 0.875rem;
        color: #6b7280;
        display: flex;
        gap: 1rem;
        margin-bottom: 0.75rem;
    }

    .session-description {
        font-size: 0.95rem;
        color: #4b5563;
        line-height: 1.6;
    }

    /* Match Score Badge */
    .match-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 100px;
        font-size: 0.875rem;
        font-weight: 600;
    }

    .match-high {
        background: #d1fae5;
        color: #065f46;
    }

    .match-medium {
        background: #fef3c7;
        color: #92400e;
    }

    .match-low {
        background: #f3f4f6;
        color: #4b5563;
    }

    /* VIP Badge */
    .vip-badge {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Speaker Tags */
    .speaker-tag {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        background: #f3f4f6;
        border-radius: 8px;
        font-size: 0.875rem;
        margin: 0.25rem;
    }

    /* Topic Tags */
    .topic-tag {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        background: #ede9fe;
        color: #5b21b6;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 500;
        margin: 0.125rem;
    }

    /* Day Navigation */
    .day-nav {
        display: flex;
        gap: 0.5rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }

    .day-pill {
        padding: 0.75rem 1.5rem;
        border: 2px solid #e5e7eb;
        border-radius: 100px;
        cursor: pointer;
        transition: all 0.2s ease;
        font-weight: 500;
    }

    .day-pill:hover {
        border-color: #667eea;
    }

    .day-pill.active {
        background: #1a1a1a;
        color: white;
        border-color: #1a1a1a;
    }

    /* CTA Buttons */
    .cta-primary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        border: none;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }

    .cta-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }

    .cta-secondary {
        background: white;
        color: #1a1a1a;
        padding: 1rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        border: 2px solid #e5e7eb;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .cta-secondary:hover {
        border-color: #1a1a1a;
    }

    /* Feature Badge */
    .feature-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        background: #f0fdf4;
        color: #166534;
        border-radius: 100px;
        font-size: 0.875rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }

    /* Expo Card */
    .expo-card {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.2s ease;
    }

    .expo-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
    }

    .expo-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .expo-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }

    .expo-tags {
        font-size: 0.8rem;
        color: #6b7280;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 0;
        margin-top: 4rem;
        border-top: 1px solid #e5e7eb;
        color: #9ca3af;
        font-size: 0.875rem;
    }

    /* Streamlit overrides */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }

    .stSelectbox > div > div {
        border-radius: 12px;
        border: 2px solid #e5e7eb;
    }

    .stMultiSelect > div > div {
        border-radius: 12px;
        border: 2px solid #e5e7eb;
    }

    .stRadio > div {
        gap: 0.5rem;
    }

    .stCheckbox > label {
        font-weight: 500;
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
        padding: 0.75rem 1.5rem;
        font-weight: 500;
    }

    .stTabs [aria-selected="true"] {
        background: white;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 100px;
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

# Community data storage
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

ROLES = [
    "Tech Professional / Engineer",
    "Startup Founder / Entrepreneur",
    "Researcher / Academic",
    "Policy Maker / Government",
    "Investor / VC",
    "Student / Early Career",
    "Business Executive / Leader",
    "Consultant / Advisor",
]

INTERESTS = {
    "Generative AI & LLMs": ["genai", "llm", "foundation-models", "chatgpt"],
    "AI Safety & Ethics": ["ai-safety", "alignment", "responsible-ai", "ethics"],
    "Healthcare AI": ["healthcare", "diagnostics", "drug-discovery", "health-equity"],
    "Enterprise AI": ["enterprise", "automation", "productivity", "business"],
    "Policy & Governance": ["policy", "governance", "regulation", "law"],
    "Research & Science": ["research", "academic", "papers", "science"],
    "Startups & Innovation": ["startups", "entrepreneurship", "demos", "funding"],
    "Education & Skills": ["education", "skills", "learning", "career"],
    "Climate & Sustainability": ["climate", "sustainability", "energy", "environment"],
    "Hardware & Infrastructure": ["computing", "hardware", "gpu", "infrastructure"],
}

GOALS = [
    ("networking", "Maximize Networking Opportunities", "Meet industry leaders and peers"),
    ("learning", "Deep Learning & Skill Building", "Attend technical sessions and workshops"),
    ("business", "Business & Investment Insights", "Explore partnerships and funding"),
    ("policy", "Policy & Governance Updates", "Understand regulatory landscape"),
    ("inspiration", "Get Inspired by Innovators", "Hear from visionary speakers"),
    ("demos", "See Cutting-Edge Demos", "Experience latest AI applications"),
]

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


def calculate_session_score(session, profile):
    """Calculate relevance score with networking ROI"""
    score = 0.0
    networking_score = 0.0
    learning_score = 0.0

    # Level match
    session_level = session.get("level", "all")
    proficiency = profile.get("proficiency", "intermediate")

    if session_level == "all":
        score += 3.0
    elif session_level == proficiency:
        score += 5.0
    elif proficiency == "intermediate":
        score += 2.0
    elif proficiency == "advanced" and session_level == "intermediate":
        score += 3.0

    # Topic match
    session_topics = session.get("topics", [])
    user_interests = profile.get("interests", [])

    for topic in session_topics:
        if topic in user_interests:
            score += 4.0
            learning_score += 2.0
        for interest in user_interests:
            if interest in topic or topic in interest:
                score += 1.5
                learning_score += 1.0

    # Goal matching
    session_desc = (session.get("description", "") + " " + session.get("title", "")).lower()
    user_goals = profile.get("goals", [])

    if "networking" in user_goals:
        networking_keywords = ["networking", "leaders", "ceo", "roundtable", "connect", "meet"]
        for kw in networking_keywords:
            if kw in session_desc:
                networking_score += 3.0
                score += 2.0

    if "learning" in user_goals:
        learning_keywords = ["workshop", "tutorial", "deep-dive", "technical", "hands-on"]
        for kw in learning_keywords:
            if kw in session_desc:
                learning_score += 2.0
                score += 2.0

    # Speaker bonus (networking potential)
    if session.get("speakers"):
        score += 1.5
        networking_score += 2.0
        top_speakers = ["sundar", "sam altman", "jensen", "demis", "yann", "dario"]
        for speaker in session.get("speakers", []):
            if any(name in speaker.lower() for name in top_speakers):
                score += 5.0
                networking_score += 5.0

    # VIP session bonus
    if session.get("level") == "advanced" and session.get("speakers"):
        session["is_vip"] = True
        score += 3.0

    session["networking_roi"] = networking_score
    session["learning_value"] = learning_score

    return score


def generate_itinerary(profile):
    """Generate personalized itinerary with ROI scoring"""
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

    # Sort by score
    all_sessions.sort(key=lambda x: x["score"], reverse=True)

    # Group by day
    itinerary = {}
    for day in available_days:
        day_sessions = [s for s in all_sessions if s["date"] == day]
        itinerary[day] = day_sessions[:5]

    return itinerary


def render_hero():
    """Render hero section"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0 3rem 0;">
        <div class="feature-badge">✨ Free · No signup · Takes 30 seconds</div>
        <h1 class="hero-title">Your Personal AI Summit Guide</h1>
        <p class="hero-subtitle">Navigate 700+ sessions across 5 days. Get a personalized schedule<br>optimized for your interests, goals, and networking ROI.</p>
        <div class="hero-stats">700+ Sessions · 3,250+ Speakers · 300+ Exhibitors · 5 Days</div>
    </div>
    """, unsafe_allow_html=True)


def render_stats():
    """Render stats cards"""
    col1, col2, col3, col4 = st.columns(4)

    stats = [
        ("700+", "Sessions"),
        ("3,250+", "Speakers"),
        ("300+", "Exhibitors"),
        ("100+", "Countries"),
    ]

    for col, (number, label) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{number}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)


def render_progress(step):
    """Render progress steps"""
    steps = [
        ("1", "Your Profile"),
        ("2", "Interests & Goals"),
        ("3", "Your Schedule"),
    ]

    st.markdown(f"""
    <div class="progress-container">
        {"".join([f'''
        <div class="step {'completed' if i < step else 'active' if i == step else ''}">
            <div class="step-number">{'✓' if i < step else i}</div>
            <span>{name}</span>
        </div>
        ''' for i, (num, name) in enumerate(steps, 1)])}
    </div>
    """, unsafe_allow_html=True)


def render_questionnaire():
    """Render the 9-question wizard"""
    if "wizard_step" not in st.session_state:
        st.session_state.wizard_step = 1
    if "profile" not in st.session_state:
        st.session_state.profile = {}

    step = st.session_state.wizard_step

    # Progress indicator
    progress = step / 4
    st.progress(progress)
    st.markdown(f"<p style='text-align: center; color: #6b7280; margin-bottom: 2rem;'>Step {step} of 4</p>", unsafe_allow_html=True)

    if step == 1:
        st.markdown("""
        <div class="question-card">
            <div class="question-title">👋 Let's get to know you</div>
            <div class="question-subtitle">Tell us a bit about yourself so we can personalize your experience</div>
        </div>
        """, unsafe_allow_html=True)

        name = st.text_input("Your Name", placeholder="Enter your name", key="q_name")
        role = st.selectbox("Your Role", ["Select your role..."] + ROLES, key="q_role")
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
                st.session_state.profile["role"] = role if role != "Select your role..." else "Professional"
                st.session_state.profile["proficiency"] = proficiency.lower()
                st.session_state.wizard_step = 2
                st.rerun()

    elif step == 2:
        st.markdown("""
        <div class="question-card">
            <div class="question-title">🎯 What topics excite you?</div>
            <div class="question-subtitle">Select all areas you'd like to explore at the summit</div>
        </div>
        """, unsafe_allow_html=True)

        selected_interests = []
        cols = st.columns(2)
        for i, (interest_name, keywords) in enumerate(INTERESTS.items()):
            with cols[i % 2]:
                if st.checkbox(interest_name, key=f"int_{interest_name}"):
                    selected_interests.extend(keywords)

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
            <div class="question-subtitle">We'll optimize your schedule for maximum value</div>
        </div>
        """, unsafe_allow_html=True)

        selected_goals = []
        for goal_id, goal_name, goal_desc in GOALS:
            if st.checkbox(f"**{goal_name}** - {goal_desc}", key=f"goal_{goal_id}"):
                selected_goals.append(goal_id)

        st.markdown("---")
        st.markdown("**📅 Which days will you attend?**")

        selected_days = []
        cols = st.columns(5)
        for col, day in zip(cols, DAYS):
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
    """Render the generated itinerary"""
    profile = st.session_state.profile
    itinerary = st.session_state.get("itinerary", {})

    # Header
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem 0 2rem 0;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1a1a1a; margin-bottom: 0.5rem;">
            ✨ {profile.get('name', 'Your')}'s Personalized Schedule
        </h2>
        <p style="color: #6b7280;">Optimized for your interests and goals</p>
    </div>
    """, unsafe_allow_html=True)

    # Profile summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Proficiency", profile.get("proficiency", "intermediate").title())
    with col2:
        st.metric("Interest Areas", len(set(profile.get("interests", []))))
    with col3:
        st.metric("Days Attending", len(profile.get("days", [])))

    st.markdown("---")

    # Day tabs
    if profile.get("days"):
        tabs = st.tabs([f"{DAY_INFO[day]['name']} ({DAY_INFO[day]['short']})" for day in profile["days"]])

        for tab, day in zip(tabs, profile["days"]):
            with tab:
                day_info = DAY_INFO[day]
                st.markdown(f"""
                <div style="padding: 1rem; background: #f8f9fa; border-radius: 12px; margin-bottom: 1.5rem;">
                    <h3 style="margin: 0; color: #1a1a1a;">🎪 {day_info['theme']}</h3>
                </div>
                """, unsafe_allow_html=True)

                sessions = itinerary.get(day, [])
                if not sessions:
                    st.info("No highly matched sessions for this day. Try broadening your interests!")
                    continue

                for session in sessions:
                    score = session.get("score", 0)
                    is_vip = session.get("is_vip", False)
                    networking_roi = session.get("networking_roi", 0)

                    # Determine match level
                    if score > 12:
                        match_class = "match-high"
                        match_text = "High Match"
                    elif score > 6:
                        match_class = "match-medium"
                        match_text = "Good Match"
                    else:
                        match_class = "match-low"
                        match_text = "Relevant"

                    # Session card
                    vip_class = "vip" if is_vip else ""
                    vip_badge = '<span class="vip-badge">VIP Session</span>' if is_vip else ''

                    with st.expander(f"**{session['title']}** | {session.get('time', 'TBA')}"):
                        col1, col2 = st.columns([2, 1])

                        with col1:
                            st.markdown(f"**Description:** {session.get('description', 'N/A')}")

                            if session.get("speakers"):
                                st.markdown("**Speakers:**")
                                for speaker in session["speakers"][:3]:
                                    st.markdown(f'<span class="speaker-tag">👤 {speaker}</span>', unsafe_allow_html=True)

                            st.markdown("**Topics:**")
                            topics_html = " ".join([f'<span class="topic-tag">{t}</span>' for t in session.get("topics", [])[:5]])
                            st.markdown(topics_html, unsafe_allow_html=True)

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
                            st.caption(f"Match Score: {score:.1f}/20")

    # Actions
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔄 Start Over", use_container_width=True):
            st.session_state.wizard_step = 1
            st.session_state.profile = {}
            st.session_state.itinerary = {}
            st.rerun()

    with col2:
        if st.button("📤 Share Schedule", use_container_width=True):
            st.session_state.show_share = True

    with col3:
        if st.button("📥 Download PDF", use_container_width=True):
            st.info("PDF download coming soon!")

    # Share modal
    if st.session_state.get("show_share"):
        with st.expander("Share Your Schedule", expanded=True):
            share_name = st.text_input("Display Name", value=profile.get("name", ""))
            share_bio = st.text_area("Brief Bio", placeholder="AI researcher, startup founder, etc.")

            if st.button("Share to Community"):
                community_data = load_community_data()
                share_entry = {
                    "id": hashlib.md5(f"{share_name}{datetime.now().isoformat()}".encode()).hexdigest()[:8],
                    "name": share_name,
                    "bio": share_bio,
                    "proficiency": profile.get("proficiency", ""),
                    "interests": list(set(profile.get("interests", [])))[:5],
                    "goals": profile.get("goals", [])[:3],
                    "itinerary": {
                        day: [{"title": s["title"], "time": s.get("time", "TBA")} for s in sessions[:3]]
                        for day, sessions in itinerary.items()
                    },
                    "shared_at": datetime.now().isoformat(),
                }
                community_data["itineraries"].append(share_entry)
                save_community_data(community_data)
                st.success(f"✅ Shared! Your code: **{share_entry['id']}**")
                st.session_state.show_share = False


def render_expo_guide():
    """Render expo pavilion guide"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1a1a1a;">🏛️ Expo Pavilion Guide</h2>
        <p style="color: #6b7280;">300+ exhibitors across 10 thematic pavilions</p>
    </div>
    """, unsafe_allow_html=True)

    pavilions = EVENT_DATA.get("expo_pavilions", [])

    cols = st.columns(3)
    for i, pavilion in enumerate(pavilions):
        with cols[i % 3]:
            icon = EXPO_ICONS.get(pavilion["name"], "📍")
            focus_tags = ", ".join(pavilion.get("focus", [])[:3])

            st.markdown(f"""
            <div class="expo-card">
                <div class="expo-icon">{icon}</div>
                <div class="expo-title">{pavilion['name']}</div>
                <div class="expo-tags">{focus_tags}</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("")


def render_speakers():
    """Render speakers section"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1a1a1a;">🎤 Featured Speakers</h2>
        <p style="color: #6b7280;">World's leading AI minds under one roof</p>
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
    <div style="text-align: center; padding: 2rem 0;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1a1a1a;">👥 Community Schedules</h2>
        <p style="color: #6b7280;">See what others are planning</p>
    </div>
    """, unsafe_allow_html=True)

    community_data = load_community_data()
    itineraries = community_data.get("itineraries", [])

    if not itineraries:
        st.info("No shared schedules yet. Be the first to share yours!")
        return

    # Filter
    filter_prof = st.selectbox("Filter by proficiency", ["All", "Beginner", "Intermediate", "Advanced"])

    for entry in itineraries[-10:][::-1]:
        if filter_prof != "All" and entry.get("proficiency", "").lower() != filter_prof.lower():
            continue

        with st.expander(f"**{entry['name']}** | {entry.get('proficiency', '').title()} | Shared {entry.get('shared_at', '')[:10]}"):
            st.markdown(f"*{entry.get('bio', 'No bio')}*")

            interests_html = " ".join([f'<span class="topic-tag">{i}</span>' for i in entry.get("interests", [])[:5]])
            st.markdown(f"**Interests:** {interests_html}", unsafe_allow_html=True)

            st.markdown("**Their Schedule:**")
            for day, sessions in entry.get("itinerary", {}).items():
                st.markdown(f"📅 **{DAY_INFO.get(day, {}).get('name', day)}:**")
                for s in sessions:
                    st.markdown(f"  • {s['title']} ({s['time']})")


def main():
    """Main app"""
    # Check if we're in wizard mode or showing results
    if st.session_state.get("wizard_step", 1) < 4:
        # Show hero and wizard
        render_hero()
        render_stats()
        st.markdown("---")
        render_questionnaire()
    else:
        # Show tabs with results
        tab1, tab2, tab3, tab4 = st.tabs([
            "📋 My Schedule",
            "🏛️ Expo Guide",
            "🎤 Speakers",
            "👥 Community"
        ])

        with tab1:
            render_itinerary_view()

        with tab2:
            render_expo_guide()

        with tab3:
            render_speakers()

        with tab4:
            render_community()

    # Footer
    st.markdown("""
    <div class="footer">
        <p>Built for <strong>India AI Impact Summit 2026</strong> · Feb 16-20, New Delhi</p>
        <p style="margin-top: 0.5rem;">Made with ❤️ for the AI community</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
