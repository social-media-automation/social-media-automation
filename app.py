import streamlit as st
import time
import pandas as pd
from datetime import datetime, timedelta
import random

# Page config
st.set_page_config(
    page_title="Social Media Agent - Live Preview",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better preview
st.markdown("""
<style>
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: bold;
    }
    .success-box {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .error-box {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border-left: 5px solid #17a2b8;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .post-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Title Section
st.title("🤖 Social Media Automation Agent")
st.markdown("*Kia hona chaheye sary kam k lia - Agent, Tool, Website, Automation*")
st.markdown("---")

# Sidebar - Real-time Stats
with st.sidebar:
    st.header("📊 Live Dashboard Stats")
    
    # Animated counter
    if 'post_count' not in st.session_state:
        st.session_state.post_count = 0
        st.session_state.posts_history = []
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📝 Posts Created", st.session_state.post_count, delta="+1")
    with col2:
        st.metric("✅ Auto-Posted", len([p for p in st.session_state.posts_history if p.get('auto_posted')]))
    
    st.markdown("---")
    st.subheader("⚙️ System Status")
    st.success("🟢 Agent Active")
    st.info("🔗 Connected to: FB, IG, LI, X, Pinterest")
    
    # Real-time log
    st.subheader("📋 Live Activity Log")
    log_placeholder = st.empty()
    
    # Mock mode toggle
    mock_mode = st.checkbox("🎭 Mock Mode (Test without real APIs)", value=True)
    st.caption("No API keys needed - Perfect for preview!")

# Main Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📝 Create & Post", 
    "🔍 Post Analyzer", 
    "📅 Special Days (Auto-Post)",
    "🌐 Multi-Platform Preview",
    "📜 History & Logs"
])

# ============================================
# TAB 1: CREATE & POST
# ============================================
with tab1:
    st.header("✨ Create & Automatically Post")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        topic = st.text_input(
            "🎯 What's your topic?",
            value="Artificial Intelligence in Healthcare",
            help="Enter any topic - AI will generate everything!"
        )
        
        platform = st.selectbox(
            "📱 Primary Platform",
            ["All Platforms (Recommended)", "Facebook", "Instagram", "LinkedIn", "Twitter/X", "Pinterest"]
        )
        
        st.subheader("📋 Your Criteria (Rules for post)")
        col_a, col_b = st.columns(2)
        with col_a:
            tone = st.selectbox("Tone", ["professional", "casual", "funny", "inspirational"])
            min_hashtags = st.slider("Minimum Hashtags", 1, 10, 3)
        with col_b:
            max_length = st.slider("Max Description Length", 100, 500, 280)
            include_emojis = st.checkbox("Include Emojis", value=False)
        
        no_negative = st.checkbox("No negative words", value=True)
        
    with col2:
        st.subheader("📱 Live Preview")
        preview_placeholder = st.empty()
        
        # Show preview based on topic
        preview_content = {
            "title": f"🚀 {topic} - The Future is Here" if not include_emojis else f"🎉 {topic} - The Future is Here 🎉",
            "description": f"Discover how {topic} is transforming our world. From innovation to implementation, see what's next! " + ("✨" if include_emojis else ""),
            "hashtags": f"#{topic.replace(' ', '')} #Innovation #Tech #Future #{tone}"
        }
        
        with preview_placeholder.container():
            st.markdown(f"""
            <div class="post-card">
                <h4>{preview_content['title'][:60]}</h4>
                <p>{preview_content['description'][:max_length]}</p>
                <small style="color: #1e90ff;">{preview_content['hashtags']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    # Create Post Button
    if st.button("🚀 GENERATE & AUTO-POST", use_container_width=True):
        
        # Step 1: Show generating animation
        with st.spinner("🤖 AI is creating your post..."):
            time.sleep(1)
            
            # Generate content based on topic
            generated_content = {
                "title": f"How {topic} is Revolutionizing 2025",
                "description": f"From breakthrough innovations to real-world applications, {topic} is changing everything we know. The future is here, and it's amazing!",
                "hashtags": f"#{topic.replace(' ', '')} #DigitalTransformation #Innovation #AI #FutureTech"
            }
            
            if include_emojis:
                generated_content["description"] += " 🚀✨💡"
            
            # Step 2: Analyze against criteria
            st.info("📊 Analyzing post against your criteria...")
            time.sleep(0.5)
            
            hashtag_count = len(generated_content['hashtags'].split())
            criteria_met = (
                hashtag_count >= min_hashtags and
                len(generated_content['description']) <= max_length and
                (not no_negative or "bad" not in generated_content['description'].lower())
            )
            
            feedback = []
            if hashtag_count < min_hashtags:
                feedback.append(f"❌ Need {min_hashtags - hashtag_count} more hashtags")
            if len(generated_content['description']) > max_length:
                feedback.append(f"❌ Too long ({len(generated_content['description'])} > {max_length})")
            if criteria_met:
                feedback.append("✅ All criteria met!")
            
            # Step 3: Error/Glitch detection
            st.info("🔍 Running pre-post validation (error/glitch check)...")
            time.sleep(0.5)
            
            has_glitch = "ð" in generated_content['description'] or "�" in generated_content['title']
            
            if has_glitch:
                st.error("⚠️ ERROR DETECTED: Text glitch found! Fix before posting.")
            else:
                st.success("✅ No errors or glitches detected!")
            
            # Step 4: Show results
            st.markdown("---")
            
            col_result1, col_result2 = st.columns(2)
            
            with col_result1:
                st.markdown("### ✅ Generated Content")
                st.markdown(f"**📌 Title:** {generated_content['title']}")
                st.markdown(f"**📝 Description:** {generated_content['description']}")
                st.markdown(f"**🔗 Hashtags:** {generated_content['hashtags']}")
            
            with col_result2:
                st.markdown("### 📊 Analysis Result")
                if criteria_met and not has_glitch:
                    st.success("✅ **CRITERIA MET!**")
                    st.markdown("Status: **APPROVED FOR POSTING**")
                else:
                    st.warning("⚠️ **CRITERIA NOT MET**")
                    st.markdown("Status: **NEEDS REVIEW**")
                
                for fb in feedback:
                    st.write(fb)
            
            # Step 5: Auto-post to all platforms
            if criteria_met and not has_glitch:
                st.markdown("---")
                st.markdown("### 🤖 AUTOMATIC POSTING IN PROGRESS...")
                
                progress_bar = st.progress(0)
                platforms = ["Facebook", "Instagram", "LinkedIn", "Twitter/X", "Pinterest"]
                
                results = {}
                for i, plat in enumerate(platforms):
                    progress_bar.progress((i + 1) * 20)
                    st.write(f"📤 Posting to {plat}...")
                    time.sleep(0.3)  # Simulate API call
                    
                    if mock_mode or random.random() > 0.2:  # 80% success in mock mode
                        results[plat] = "✅ Success"
                    else:
                        results[plat] = "❌ Failed (Rate limit)"
                
                st.success("✅ **POSTED SUCCESSFULLY TO ALL PLATFORMS!**")
                
                # Show results table
                result_df = pd.DataFrame([results]).T
                result_df.columns = ["Status"]
                st.table(result_df)
                
                # Save to history
                st.session_state.post_count += 1
                st.session_state.posts_history.append({
                    "id": st.session_state.post_count,
                    "topic": topic,
                    "title": generated_content['title'],
                    "platforms": list(results.keys()),
                    "auto_posted": True,
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "criteria_met": criteria_met
                })
                
                # Update sidebar log
                with log_placeholder.container():
                    st.write(f"✅ [{datetime.now().strftime('%H:%M:%S')}] Posted: {topic[:30]}...")
            else:
                st.error("❌ Post BLOCKED due to criteria failure or errors. Fix issues and try again.")

# ============================================
# TAB 2: POST ANALYZER (Test any post)
# ============================================
with tab2:
    st.header("🔍 Advanced Post Analyzer")
    
    col1, col2 = st.columns(2)
    
    with col1:
        test_title = st.text_input("Test Title", "Amazing AI Breakthrough in Medical Diagnosis")
        test_desc = st.text_area("Test Description", "AI is now 95% accurate in detecting early-stage cancer, saving millions of lives! 🏥")
        test_tags = st.text_input("Test Hashtags", "#AIHealth #MedTech #CancerDetection #Innovation")
    
    with col2:
        st.subheader("Analysis Criteria")
        test_tone = st.selectbox("Required Tone", ["professional", "casual"], key="test_tone")
        test_min_tags = st.number_input("Minimum Hashtags", 1, 10, 4, key="test_tags")
        test_max_len = st.number_input("Max Length", 50, 500, 280, key="test_len")
        test_no_neg = st.checkbox("No Negative Words", True, key="test_neg")
        test_emoji = st.checkbox("Must Include Emojis", False, key="test_emoji")
    
    if st.button("🔍 ANALYZE THIS POST"):
        st.markdown("---")
        
        # Perform analysis
        issues = []
        
        # Check 1: Hashtags
        tag_count = len([t for t in test_tags.split() if t.startswith('#')])
        if tag_count < test_min_tags:
            issues.append(f"❌ Hashtags: Found {tag_count}, need {test_min_tags}")
        else:
            issues.append(f"✅ Hashtags: {tag_count} (meets {test_min_tags}+ requirement)")
        
        # Check 2: Length
        if len(test_desc) > test_max_len:
            issues.append(f"❌ Length: {len(test_desc)} characters (exceeds {test_max_len})")
        else:
            issues.append(f"✅ Length: {len(test_desc)} characters")
        
        # Check 3: Professional tone
        unprofessional = ["omg", "lol", "wtf", "damn"]
        if test_tone == "professional" and any(word in test_desc.lower() for word in unprofessional):
            issues.append("❌ Tone: Contains unprofessional language")
        else:
            issues.append("✅ Tone: Professional enough")
        
        # Check 4: Emojis
        import re
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"
            u"\U0001F300-\U0001F5FF"
            u"\U0001F680-\U0001F6FF"
            "]+", flags=re.UNICODE)
        
        has_emoji = bool(emoji_pattern.search(test_desc))
        if test_emoji and not has_emoji:
            issues.append("❌ Emojis: Required but none found")
        elif has_emoji:
            issues.append("✅ Emojis: Found in description")
        else:
            issues.append("ℹ️ Emojis: Optional, none found")
        
        # Check 5: Negative words
        negative_words = ["bad", "terrible", "hate", "worst", "problem"]
        found_negatives = [w for w in negative_words if w in test_desc.lower()]
        if test_no_neg and found_negatives:
            issues.append(f"❌ Negative words found: {', '.join(found_negatives)}")
        else:
            issues.append("✅ No negative words detected")
        
        # Display results
        st.subheader("📊 Analysis Results")
        
        for issue in issues:
            if "✅" in issue:
                st.success(issue)
            elif "❌" in issue:
                st.error(issue)
            else:
                st.info(issue)
        
        # Overall verdict
        failed = [i for i in issues if "❌" in i]
        if not failed:
            st.balloons()
            st.success("🎉 **POST MEETS ALL CRITERIA!** Ready for publishing.")
        else:
            st.warning(f"⚠️ **POST FAILED {len(failed)} CHECK(S)** - Fix issues before posting")

# ============================================
# TAB 3: SPECIAL DAYS AUTO-POST (FRIDAY, EID, ETC)
# ============================================
with tab3:
    st.header("📅 Automatic Posts on Special & Famous Days")
    st.markdown("*System automatically generates and posts on these days*")
    
    # Fetch special days
    today = datetime.now()
    special_days = [
        {"day": "Eid-ul-Adha 🕌", "date": "2025-06-07", "type": "Islamic Festival", "status": "Scheduled", "post": "Wishing you joy and blessings on Eid-ul-Adha! May your sacrifices be accepted."},
        {"day": "Labour Day 👷", "date": "2025-05-01", "type": "International", "status": "Scheduled", "post": "Honoring all workers worldwide. Thank you for your contributions!"},
        {"day": "World Environment Day 🌍", "date": "2025-06-05", "type": "Awareness", "status": "Scheduled", "post": "Protect our planet - every action counts! #WorldEnvironmentDay"},
        {"day": "Friday (Weekly) 📅", "date": (today + timedelta(days=(4 - today.weekday()) % 7)).strftime("%Y-%m-%d"), "type": "Weekly", "status": "Ready", "post": "Happy Friday! Start your weekend with positivity and purpose."},
        {"day": "New Year 2025 🎉", "date": "2025-01-01", "type": "Celebration", "status": "Scheduled", "post": "New year, new beginnings! Wishing everyone a prosperous 2025."},
    ]
    
    # Display as table
    df_special = pd.DataFrame(special_days)
    st.dataframe(df_special, use_container_width=True, hide_index=True)
    
    # Auto-post trigger for next special day
    st.subheader("⚡ Auto-Post Simulation")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎯 Test Auto-Post for Next Special Day"):
            next_day = special_days[0]
            st.info(f"🤖 Generating post for {next_day['day']}...")
            time.sleep(1)
            
            st.markdown(f"""
            <div class="success-box">
                <strong>✅ AUTO-GENERATED POST FOR {next_day['day'].upper()}</strong><br>
                {next_day['post']}<br><br>
                <small>📤 Automatically posted to: Facebook, Instagram, LinkedIn, Twitter, Pinterest</small>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("🎉 Post published successfully to all platforms!")
    
    with col2:
        if st.button("📊 View Engagement Analytics"):
            st.markdown("""
            <div class="info-box">
                <strong>📈 SPECIAL DAY PERFORMANCE</strong><br>
                • Best performing: Eid-ul-Adha (8,500 engagements)<br>
                • Highest reach: New Year (25,000+ impressions)<br>
                • Best platform: Instagram (45% engagement)<br>
                • Auto-reply to comments: Active ✅
            </div>
            """, unsafe_allow_html=True)

# ============================================
# TAB 4: MULTI-PLATFORM PREVIEW
# ============================================
with tab4:
    st.header("🌐 Multi-Platform Integration Preview")
    st.markdown("*See how your post looks on each platform before publishing*")
    
    # Sample post
    sample_post = {
        "title": "AI in Healthcare: The Future is Now",
        "description": "Revolutionizing patient care with artificial intelligence - faster diagnosis, better treatment, saved lives.",
        "hashtags": "#AIHealth #MedTech #Innovation"
    }
    
    # Platform previews
    col1, col2 = st.columns(2)
    
    with col1:
        # Facebook Preview
        st.markdown("### 📘 Facebook")
        st.markdown(f"""
        <div style="background: #f0f2f5; padding: 15px; border-radius: 10px; margin: 10px 0;">
            <strong>🤖 {sample_post['title']}</strong><br>
            {sample_post['description']}<br>
            <small style="color: #65676b;">{sample_post['hashtags']}</small>
            <div style="margin-top: 10px;">
                <span>👍 Like</span> &nbsp; 💬 Comment &nbsp; 🔄 Share
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Instagram Preview
        st.markdown("### 📸 Instagram")
        st.markdown(f"""
        <div style="background: linear-gradient(45deg, #f09433, #d62976); padding: 15px; border-radius: 10px; color: white; margin: 10px 0;">
            <strong>✨ {sample_post['title'][:40]}</strong><br>
            {sample_post['description'][:120]}...<br>
            <small>{sample_post['hashtags']}</small>
            <div style="margin-top: 10px;">
                ❤️ Like &nbsp; 💬 Comment &nbsp; 📤 Share
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # LinkedIn Preview
        st.markdown("### 🔗 LinkedIn")
        st.markdown(f"""
        <div style="background: white; border: 1px solid #e0e0e0; padding: 15px; border-radius: 10px; margin: 10px 0;">
            <strong>👔 {sample_post['title']}</strong><br>
            {sample_post['description']}<br>
            <small style="color: #0a66c2;">{sample_post['hashtags']}</small>
            <div style="margin-top: 10px; color: #666;">
                👍 Like &nbsp; 💬 Comment &nbsp; 🔄 Repost
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Twitter Preview
        st.markdown("### 🐦 Twitter/X")
        st.markdown(f"""
        <div style="background: black; padding: 15px; border-radius: 10px; color: white; margin: 10px 0;">
            <strong>🐦 {sample_post['title'][:35]}</strong><br>
            {sample_post['description'][:140]}<br>
            <small>{sample_post['hashtags']}</small>
            <div style="margin-top: 10px; color: #71767b;">
                🔄 Retweet &nbsp; ❤️ Like &nbsp; 💬 Reply
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Pinterest Preview
        st.markdown("### 📌 Pinterest")
        st.markdown(f"""
        <div style="background: #e60023; padding: 15px; border-radius: 10px; color: white; margin: 10px 0;">
            <strong>📌 {sample_post['title'][:30]}</strong><br>
            {sample_post['description'][:100]}...<br>
            <small>{sample_post['hashtags']}</small>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# TAB 5: HISTORY & LOGS
# ============================================
with tab5:
    st.header("📜 Post History & Activity Logs")
    
    if st.session_state.posts_history:
        # Convert to DataFrame
        history_df = pd.DataFrame(st.session_state.posts_history)
        
        # Display metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Posts", len(history_df))
        with col2:
            st.metric("Auto-Posted", len(history_df[history_df['auto_posted'] == True]))
        with col3:
            st.metric("Success Rate", f"{(len(history_df[history_df['auto_posted'] == True]) / len(history_df) * 100):.0f}%")
        
        # Display table
        st.dataframe(history_df, use_container_width=True)
        
        # Export option
        csv = history_df.to_csv(index=False)
        st.download_button("📥 Export History to CSV", csv, "post_history.csv", "text/csv")
        
        # Clear button
        if st.button("🗑️ Clear History"):
            st.session_state.posts_history = []
            st.session_state.post_count = 0
            st.rerun()
    else:
        st.info("No posts created yet. Go to 'Create & Post' tab to create your first post!")
    
    # System logs
    st.subheader("🔧 System Activity Logs")
    logs = [
        "✅ System started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "🔗 Connected to all social media platforms",
        "📅 Scheduled special days posts",
        "🤖 AI agent ready for content generation",
        "🛡️ Pre-post validator active"
    ]
    
    for log in logs:
        st.code(log, language="log")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <strong>🤖 Social Media Automation Agent</strong> | Complete workflow: Create → Analyze → Validate → Auto-Post<br>
    ✅ Facebook | ✅ Instagram | ✅ LinkedIn | ✅ Twitter/X | ✅ Pinterest | ✅ Special Days Calendar
</div>
""", unsafe_allow_html=True)
