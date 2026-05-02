import streamlit as st
import time
import pandas as pd
from datetime import datetime, timedelta
import random
from streamlit_option_menu import option_menu
import json
import re

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="SocialMediaAI | Enterprise Suite",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CUSTOM CSS - PREMIUM DESIGN
# ============================================
st.markdown("""
<style>
    /* Import Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Container */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Glass Card Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s ease;
    }
    
    /* Gradient Text */
    .gradient-text {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }
    
    /* Premium Button */
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 32px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Stat Cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 1.5rem;
        color: white;
        text-align: center;
        transition: all 0.3s ease;
        margin: 0.5rem 0;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
    }
    
    /* Platform Cards */
    .platform-card {
        background: white;
        border-radius: 16px;
        padding: 1rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
        border: 1px solid #e0e0e0;
        text-align: center;
    }
    
    .platform-card:hover {
        transform: translateX(5px);
        border-color: #667eea;
        box-shadow: 0 5px 15px rgba(102,126,234,0.2);
    }
    
    /* Success Box */
    .success-box {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border-left: 5px solid #28a745;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%);
        border-left: 5px solid #17a2b8;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    /* Metric Container */
    .metric-container {
        background: white;
        border-radius: 16px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* Animated Border */
    @keyframes borderPulse {
        0% { border-color: #667eea; }
        50% { border-color: #764ba2; }
        100% { border-color: #667eea; }
    }
    
    .animated-border {
        border: 2px solid #667eea;
        animation: borderPulse 2s infinite;
        border-radius: 16px;
        padding: 1px;
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .stat-card {
            margin: 0.25rem 0;
            padding: 1rem;
        }
        .glass-card {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# SESSION STATE INITIALIZATION
# ============================================
if 'post_count' not in st.session_state:
    st.session_state.post_count = 1247
    st.session_state.posts_history = []
    st.session_state.engagement_rate = 8.4
    st.session_state.reach = 284500
    st.session_state.active_campaign = None
    st.session_state.notifications = []

# ============================================
# HEADER SECTION
# ============================================
col1, col2, col3, col4, col5 = st.columns([1.5, 2, 1, 1, 1])

with col1:
    st.markdown("""
    <div style="display: flex; align-items: center;">
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    width: 50px; height: 50px; border-radius: 15px; 
                    display: flex; align-items: center; justify-content: center;">
            <span style="font-size: 28px;">🎯</span>
        </div>
        <div style="margin-left: 12px;">
            <span style="font-size: 20px; font-weight: 800;">SocialMedia<span class="gradient-text">AI</span></span>
            <br>
            <span style="font-size: 12px; color: #666;">Enterprise Suite v3.0</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: rgba(102,126,234,0.1); border-radius: 12px; padding: 8px 16px; text-align: center;">
        <span style="font-size: 12px; color: #667eea;">⚡ SYSTEM ONLINE</span>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="background: rgba(102,126,234,0.1); border-radius: 12px; padding: 8px 16px; text-align: center;">
        <span style="font-size: 12px; color: #667eea;">🤖 AI READY</span>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div style="background: rgba(102,126,234,0.1); border-radius: 12px; padding: 8px 16px; text-align: center;">
        <span style="font-size: 12px; color: #667eea;">🌐 5 PLATFORMS</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================
# PREMIUM METRICS DASHBOARD
# ============================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="stat-card">
        <div style="font-size: 14px; opacity: 0.9;">TOTAL POSTS</div>
        <div style="font-size: 36px; font-weight: 800; margin: 10px 0;">{st.session_state.post_count}+</div>
        <div style="font-size: 12px;">↑ 23% this week</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-card">
        <div style="font-size: 14px; opacity: 0.9;">ENGAGEMENT RATE</div>
        <div style="font-size: 36px; font-weight: 800; margin: 10px 0;">{st.session_state.engagement_rate}%</div>
        <div style="font-size: 12px;">↑ 5.2% vs last month</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-card">
        <div style="font-size: 14px; opacity: 0.9;">TOTAL REACH</div>
        <div style="font-size: 36px; font-weight: 800; margin: 10px 0;">{st.session_state.reach:,}</div>
        <div style="font-size: 12px;">🌍 Global audience</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="stat-card">
        <div style="font-size: 14px; opacity: 0.9;">AUTO-POSTED</div>
        <div style="font-size: 36px; font-weight: 800; margin: 10px 0;">{len(st.session_state.posts_history)}</div>
        <div style="font-size: 12px;">✅ 100% automation</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================
# NAVIGATION MENU (Without Plotly)
# ============================================
menu_items = ["✨ Campaign Studio", "🔍 Smart Analyzer", "📅 Auto-Pilot", "🌐 Cross-Platform", "📊 Analytics Hub", "⚙️ Insights"]
menu_icons = ["rocket", "microscope", "calendar-check", "globe2", "graph-up", "cpu"]

selected = option_menu(
    menu_title=None,
    options=menu_items,
    icons=menu_icons,
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "icon": {"color": "#667eea", "font-size": "18px"},
        "nav-link": {
            "font-size": "14px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "rgba(102,126,234,0.1)",
            "font-weight": "600",
            "border-radius": "12px",
        },
        "nav-link-selected": {
            "background": "linear-gradient(90deg, #667eea 0%, #764ba2 100%)",
            "color": "white",
        },
    },
)

# ============================================
# TAB 1: CAMPAIGN STUDIO
# ============================================
if selected == "✨ Campaign Studio":
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🎨 Campaign Creation Studio")
        st.markdown("*AI-powered content generation with intelligent automation*")
        st.markdown("---")
        
        col1, col2 = st.columns([1.2, 0.8])
        
        with col1:
            topic = st.text_input(
                "🎯 Campaign Topic",
                value="Artificial Intelligence in Healthcare",
                help="Enter your campaign theme"
            )
            
            col_a, col_b = st.columns(2)
            with col_a:
                campaign_type = st.selectbox(
                    "Campaign Type",
                    ["🚀 Product Launch", "📢 Brand Awareness", "🎉 Holiday Special", "📈 Growth Campaign"]
                )
                tone = st.select_slider(
                    "Content Tone",
                    options=["Casual", "Professional", "Inspirational", "Technical"],
                    value="Professional"
                )
            with col_b:
                target_platform = st.multiselect(
                    "Target Platforms",
                    ["Facebook", "Instagram", "LinkedIn", "Twitter/X", "Pinterest"],
                    default=["Facebook", "Instagram", "LinkedIn", "Twitter/X", "Pinterest"]
                )
                budget = st.select_slider(
                    "Campaign Priority",
                    options=["Standard", "High", "Enterprise"],
                    value="High"
                )
            
            st.markdown("---")
            st.markdown("### 🎯 Advanced Criteria")
            
            col_c, col_d = st.columns(2)
            with col_c:
                min_hashtags = st.slider("Minimum Hashtags", 1, 15, 5)
                max_length = st.slider("Max Description Length", 100, 500, 280)
            with col_d:
                include_emojis = st.toggle("✨ Include Emojis", value=True)
                viral_optimization = st.toggle("🚀 Viral Optimization", value=True)
        
        with col2:
            st.markdown("### 📱 Live AI Preview")
            
            preview_title = f"{'🚀 ' if include_emojis else ''}How {topic[:40]} is Transforming 2025{' 🎯' if include_emojis else ''}"
            preview_desc = f"Discover the revolutionary impact of {topic[:60]}. From breakthrough innovations to real-world applications, witness the future unfold. {random.choice(['✨', '💡', '🚀', '🎯']) if include_emojis else ''}"
            preview_hashtags = f"#{topic.replace(' ', '')[:20]} #Innovation #Future #Trending2025"
            
            st.markdown(f"""
            <div class="animated-border">
                <div style="padding: 20px; background: white; border-radius: 16px;">
                    <div style="background: #f8f9fa; padding: 12px; border-radius: 10px; margin-bottom: 10px;">
                        <strong>📌 Title:</strong><br>
                        {preview_title[:60]}
                    </div>
                    <div style="background: #f8f9fa; padding: 12px; border-radius: 10px; margin-bottom: 10px;">
                        <strong>📝 Description:</strong><br>
                        {preview_desc[:max_length]}
                    </div>
                    <div style="background: #f8f9fa; padding: 12px; border-radius: 10px;">
                        <strong>🔗 Hashtags:</strong><br>
                        {preview_hashtags}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("🚀 LAUNCH INTELLIGENT CAMPAIGN", use_container_width=True):
            with st.spinner("🎯 AI Orchestrating Campaign..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                st.session_state.post_count += 1
                st.balloons()
                
                st.markdown("""
                <div class="success-box">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 30px;">🎉</span>
                        <div>
                            <strong style="font-size: 18px;">CAMPAIGN DEPLOYED SUCCESSFULLY!</strong><br>
                            <span>Your content has been published to all selected platforms with AI optimization.</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("🎯 Predicted CTR", "4.8%", "+1.2%")
                with col_b:
                    st.metric("📈 Engagement Score", "92/100", "+15")
                with col_c:
                    st.metric("🎨 AI Confidence", "98%", "+3%")

# ============================================
# TAB 2: SMART ANALYZER
# ============================================
elif selected == "🔍 Smart Analyzer":
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🔬 AI-Powered Post Intelligence")
        st.markdown("*Deep learning analysis with predictive engagement scoring*")
        st.markdown("---")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            test_title = st.text_input("Post Title", "Groundbreaking AI Discovery in Medical Research")
            test_desc = st.text_area("Post Content", "Our latest breakthrough in AI-powered diagnostics achieved 99.9% accuracy in early disease detection, potentially saving millions of lives annually. 🏥✨", height=150)
            test_tags = st.text_input("Hashtags", "#AIHealth #MedicalInnovation #FutureTech #Breakthrough #DigitalHealth")
        
        with col2:
            st.markdown("### 🎯 Analysis Parameters")
            target_emotion = st.selectbox("Target Emotion", ["Inspiration", "Excitement", "Trust", "Curiosity", "Urgency"])
            industry = st.selectbox("Industry Focus", ["Healthcare", "Technology", "Marketing", "Education", "E-commerce"])
            benchmark = st.selectbox("Compare With", ["Top 10% Performers", "Industry Average", "Previous Campaigns"])
            
            if st.button("🔍 RUN DEEP ANALYSIS", use_container_width=True):
                with st.spinner("Neural network analyzing..."):
                    time.sleep(2)
                    
                    st.markdown("---")
                    st.markdown("### 📊 Comprehensive Analysis Report")
                    
                    col_metrics = st.columns(3)
                    with col_metrics[0]:
                        st.metric("🎯 Engagement Score", "96/100", "+12")
                    with col_metrics[1]:
                        st.metric("📈 Viral Potential", "High", "Top 8%")
                    with col_metrics[2]:
                        st.metric("🤖 AI Authenticity", "98%", "Excellent")
                    
                    # Simple bar chart using columns
                    st.markdown("### 📈 Content Performance Metrics")
                    metrics_data = {
                        "Clarity": 95,
                        "Emotion": 92,
                        "Relevance": 98,
                        "Trendiness": 89,
                        "Shareability": 94
                    }
                    
                    for metric, score in metrics_data.items():
                        st.markdown(f"""
                        <div style="margin: 10px 0;">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                                <span>{metric}</span>
                                <span>{score}%</span>
                            </div>
                            <div style="background: #e0e0e0; border-radius: 10px; overflow: hidden;">
                                <div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
                                            width: {score}%; height: 30px; border-radius: 10px; 
                                            display: flex; align-items: center; justify-content: center; 
                                            color: white; font-size: 12px;">
                                    {score}%
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.success("✅ Analysis complete. This post is predicted to perform in the top 8% of your industry!")
        
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================
# TAB 3: AUTO-PILOT
# ============================================
elif selected == "📅 Auto-Pilot":
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🤖 Autonomous Scheduling Engine")
        st.markdown("*AI-powered content calendar with predictive posting*")
        st.markdown("---")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 📅 Upcoming Auto-Scheduled Events")
            
            events = [
                {"date": "Tomorrow", "event": "Friday Weekly", "type": "Weekly", "posts": 5, "reach": "50K+"},
                {"date": "May 1, 2025", "event": "Labour Day", "type": "International", "posts": 5, "reach": "120K+"},
                {"date": "June 5, 2025", "event": "World Environment Day", "type": "Awareness", "posts": 5, "reach": "85K+"},
                {"date": "June 7, 2025", "event": "Eid-ul-Adha", "type": "Islamic Festival", "posts": 5, "reach": "200K+"},
                {"date": "Jan 1, 2026", "event": "New Year 2026", "type": "Global", "posts": 5, "reach": "500K+"},
            ]
            
            for event in events:
                st.markdown(f"""
                <div class="platform-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <strong>{event['event']}</strong><br>
                            <small style="color: #666;">📅 {event['date']} • {event['type']}</small>
                        </div>
                        <div style="text-align: right;">
                            <span style="color: #10b981;">✅ Scheduled</span><br>
                            <small>{event['posts']} platforms • {event['reach']} reach</small>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 🎯 Auto-Pilot Controls")
            
            ai_schedule = st.toggle("🤖 AI Smart Scheduling", value=True)
            auto_optimize = st.toggle("⚡ Auto-Optimize Timing", value=True)
            predictive_boost = st.toggle("📈 Predictive Boost", value=True)
            
            st.markdown("---")
            
            if st.button("🚀 ACTIVATE AUTO-PILOT", use_container_width=True):
                st.success("✅ Auto-Pilot engaged! Posts will be automatically generated and scheduled for all upcoming events.")
        
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================
# TAB 4: CROSS-PLATFORM
# ============================================
elif selected == "🌐 Cross-Platform":
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🌍 Unified Cross-Platform Command Center")
        st.markdown("*One-click distribution to all major social networks*")
        st.markdown("---")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        platforms_data = [
            {"name": "Facebook", "icon": "📘", "status": "Connected", "reach": "1.2M", "color": "#1877f2"},
            {"name": "Instagram", "icon": "📸", "status": "Connected", "reach": "890K", "color": "#e4405f"},
            {"name": "LinkedIn", "icon": "🔗", "status": "Connected", "reach": "450K", "color": "#0a66c2"},
            {"name": "Twitter/X", "icon": "🐦", "status": "Connected", "reach": "620K", "color": "#1da1f2"},
            {"name": "Pinterest", "icon": "📌", "status": "Connected", "reach": "340K", "color": "#bd081c"}
        ]
        
        for idx, platform in enumerate(platforms_data):
            with [col1, col2, col3, col4, col5][idx]:
                st.markdown(f"""
                <div class="platform-card">
                    <div style="font-size: 48px;">{platform['icon']}</div>
                    <strong>{platform['name']}</strong><br>
                    <small style="color: #10b981;">● {platform['status']}</small><br>
                    <small>📊 {platform['reach']}</small>
                    <div style="margin-top: 10px;">
                        <div style="background: {platform['color']}; height: 4px; border-radius: 2px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📊 Performance Dashboard")
            
            # Simple performance chart using columns
            platform_performance = {
                "Facebook": 35,
                "Instagram": 42,
                "LinkedIn": 12,
                "Twitter": 8,
                "Pinterest": 3
            }
            
            for platform, percent in platform_performance.items():
                st.markdown(f"""
                <div style="margin: 10px 0;">
                    <div style="display: flex; justify-content: space-between;">
                        <span>{platform}</span>
                        <span>{percent}%</span>
                    </div>
                    <div style="background: #e0e0e0; border-radius: 10px; overflow: hidden;">
                        <div style="background: linear-gradient(90deg, #667eea, #764ba2); 
                                    width: {percent}%; height: 30px; border-radius: 10px;
                                    display: flex; align-items: center; justify-content: center;
                                    color: white; font-size: 12px;">
                            {percent}% Engagement
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 🚀 Quick Actions")
            quick_post = st.text_area("Write a post...", height=150)
            if st.button("📤 Post to All Platforms", use_container_width=True):
                if quick_post:
                    st.success("✅ Post published to all 5 platforms successfully!")
                else:
                    st.warning("Please write a post first")
        
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================
# TAB 5: ANALYTICS HUB
# ============================================
elif selected == "📊 Analytics Hub":
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📈 Enterprise Analytics Intelligence")
        st.markdown("*Real-time metrics with predictive insights*")
        st.markdown("---")
        
        # Generate mock trend data
        st.markdown("### 📈 30-Day Engagement Trend")
        
        # Create a simple line chart using columns
        days = list(range(1, 31))
        engagement_values = [65, 68, 72, 70, 75, 78, 82, 80, 85, 88, 86, 89, 92, 90, 93, 95, 94, 96, 95, 97, 96, 98, 97, 96, 95, 94, 93, 92, 91, 90]
        
        # Display as a trend line using HTML/CSS
        st.markdown('<div style="background: white; padding: 20px; border-radius: 12px;">', unsafe_allow_html=True)
        
        # Create horizontal bar representation of trend
        cols = st.columns(30)
        for i, (day, value) in enumerate(zip(days, engagement_values)):
            with cols[i]:
                height = value / 2
                st.markdown(f"""
                <div style="text-align: center;">
                    <div style="background: linear-gradient(180deg, #667eea, #764ba2); 
                                height: {height}px; width: 100%; border-radius: 4px 4px 0 0;"></div>
                    <div style="font-size: 10px; margin-top: 5px;">{day}</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="metric-container">', unsafe_allow_html=True)
            st.metric("📈 Growth Rate", "+24.5%", "+5.2%")
            st.metric("👥 New Followers", "12,847", "+2,341")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="metric-container">', unsafe_allow_html=True)
            st.metric("💬 Total Comments", "45,892", "+8,234")
            st.metric("🔄 Total Shares", "28,456", "+5,678")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="metric-container">', unsafe_allow_html=True)
            st.metric("⭐ Average CTR", "4.8%", "+0.9%")
            st.metric("🎯 Conversion Rate", "3.2%", "+0.7%")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================
# TAB 6: INSIGHTS
# ============================================
elif selected == "⚙️ Insights":
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🧠 AI-Powered Strategic Insights")
        st.markdown("*Machine learning recommendations for optimal performance*")
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎯 AI Recommendations")
            recommendations = [
                "📊 Post between 8-10 AM for 47% higher engagement",
                "🎨 Use 3-5 emojis to increase click-through rate by 28%",
                "📹 Video content earns 4x more engagement on LinkedIn",
                "⏰ Schedule weekend posts for 35% better reach",
                "🔗 Add 1-2 links to drive 22% more traffic"
            ]
            
            for rec in recommendations:
                st.info(rec)
        
        with col2:
            st.markdown("### 🤖 Predictive Analytics")
            
            future_metrics = {
                "Next Week Reach": "+15.2%",
                "Engagement Forecast": "92/100",
                "Best Time to Post": "Wed 9 AM",
                "Trending Topic": "AI Technology",
                "Viral Score": "86/100"
            }
            
            for metric, value in future_metrics.items():
                st.markdown(f"""
                <div style="background: linear-gradient(90deg, rgba(102,126,234,0.1) 0%, rgba(118,75,162,0.1) 100%); 
                            padding: 12px; border-radius: 12px; margin: 8px 0;">
                    <div style="display: flex; justify-content: space-between;">
                        <span>{metric}</span>
                        <strong style="color: #667eea;">{value}</strong>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(102,126,234,0.05) 0%, rgba(118,75,162,0.05) 100%); border-radius: 16px;">
    <div style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap;">
        <div>🚀 <strong>1247+</strong> Campaigns Run</div>
        <div>🌍 <strong>5</strong> Platforms Connected</div>
        <div>🤖 <strong>98.5%</strong> AI Accuracy</div>
        <div>⚡ <strong>24/7</strong> Automation</div>
    </div>
    <div style="margin-top: 15px; color: #666; font-size: 12px;">
        © 2025 SocialMediaAI Enterprise Suite | Powered by Advanced Neural Networks
    </div>
</div>
""", unsafe_allow_html=True)
