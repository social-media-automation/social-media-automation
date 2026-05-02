
# Step 4: Create the main app file
%%writefile app.py
import streamlit as st
import time
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Social Media Agent - Live Demo", layout="wide")

# Custom CSS
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
    .post-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 Social Media Automation Agent - Free Demo")
st.markdown("*Test the complete workflow online - No installation needed*")

# Sidebar
with st.sidebar:
    st.header("📊 Live Demo Stats")
    if 'post_count' not in st.session_state:
        st.session_state.post_count = 0
        st.session_state.posts = []
    
    st.metric("Total Tests", st.session_state.post_count)
    st.markdown("---")
    st.success("🟢 System Active")
    st.info("🔗 Demo Mode (Mock APIs)")
    st.caption("✅ Facebook | ✅ Instagram | ✅ LinkedIn | ✅ Twitter | ✅ Pinterest")

# Main tabs
tab1, tab2, tab3 = st.tabs(["🚀 Test Automation", "📅 Special Days Demo", "📊 Live Preview"])

with tab1:
    st.header("Test Complete Workflow")
    
    topic = st.text_input("Enter any topic", "Artificial Intelligence in Healthcare")
    
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox("Tone", ["professional", "casual", "funny"])
        min_hashtags = st.slider("Min Hashtags", 1, 5, 3)
    with col2:
        max_length = st.slider("Max Length", 100, 500, 280)
        check_errors = st.checkbox("Enable error detection", True)
    
    if st.button("🚀 RUN AUTOMATION TEST", use_container_width=True):
        st.session_state.post_count += 1
        
        # Step 1: Content Creation
        with st.spinner("🤖 Generating content..."):
            time.sleep(0.5)
            content = {
                "title": f"How {topic} is Transforming 2025",
                "description": f"Discover the future with {topic}. Innovation meets reality in this breakthrough technology!",
                "hashtags": f"#{topic.replace(' ', '')} #Innovation #Tech #Future"
            }
        
        # Step 2: Analysis
        with st.spinner("📊 Analyzing against criteria..."):
            time.sleep(0.5)
            hashtag_count = len(content['hashtags'].split())
            meets_criteria = hashtag_count >= min_hashtags and len(content['description']) <= max_length
        
        # Step 3: Error Detection
        with st.spinner("🔍 Checking for errors/glitches..."):
            time.sleep(0.5)
            has_error = check_errors and "ð" in content['description']
        
        # Step 4: Results
        st.markdown("---")
        
        col_result1, col_result2 = st.columns(2)
        
        with col_result1:
            st.markdown("### ✅ Generated Content")
            st.markdown(f"**Title:** {content['title']}")
            st.markdown(f"**Description:** {content['description']}")
            st.markdown(f"**Hashtags:** {content['hashtags']}")
        
        with col_result2:
            st.markdown("### 📊 Analysis Result")
            if meets_criteria and not has_error:
                st.success("✅ ALL CHECKS PASSED!")
                st.balloons()
            else:
                st.warning("⚠️ ISSUES FOUND")
                if not meets_criteria:
                    st.write("❌ Criteria not met")
                if has_error:
                    st.write("❌ Text glitch detected")
        
        # Step 5: Auto-Posting Simulation
        if meets_criteria and not has_error:
            st.markdown("### 🤖 Auto-Posting to All Platforms")
            platforms = ["Facebook", "Instagram", "LinkedIn", "Twitter", "Pinterest"]
            progress = st.progress(0)
            
            for i, plat in enumerate(platforms):
                progress.progress((i+1)*20)
                st.write(f"✅ Posted to {plat}")
                time.sleep(0.2)
            
            st.success("🎉 SUCCESS! Post published to all 5 platforms")
            
            # Save to history
            st.session_state.posts.append({
                "topic": topic,
                "status": "Success",
                "time": datetime.now().strftime("%H:%M:%S")
            })
        else:
            st.error("❌ Post BLOCKED - Fix issues before publishing")

with tab2:
    st.header("📅 Special Days Auto-Post Demo")
    
    special_days = {
        "Eid-ul-Adha": "Islamic Festival",
        "Labour Day": "International Workers Day", 
        "Friday": "Weekly Special",
        "New Year": "Celebration",
        "World Environment Day": "Awareness"
    }
    
    selected_day = st.selectbox("Select a special day", list(special_days.keys()))
    
    if st.button("🎯 Generate Auto-Post for Selected Day"):
        st.info(f"🤖 Generating post for {selected_day}...")
        time.sleep(1)
        
        posts = {
            "Eid-ul-Adha": "🕌 Wishing you joy and blessings on Eid-ul-Adha! May your sacrifices be accepted. #EidMubarak",
            "Labour Day": "👷 Honoring all workers worldwide! Thank you for your contributions. #LabourDay",
            "Friday": "📅 Happy Friday! Start your weekend with positivity. #FridayVibes",
            "New Year": "🎉 Happy New Year! New beginnings, new opportunities. #NewYear2025",
            "World Environment Day": "🌍 Protect our planet - every action counts! #WorldEnvironmentDay"
        }
        
        st.markdown(f"""
        <div class="success-box">
            <strong>✅ AUTO-GENERATED POST FOR {selected_day.upper()}</strong><br>
            {posts[selected_day]}<br><br>
            <small>📤 Automatically scheduled for: {selected_day}</small><br>
            <small>✅ Queued for: Facebook, Instagram, LinkedIn, Twitter, Pinterest</small>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("Post scheduled successfully!")

with tab3:
    st.header("🌐 Live Multi-Platform Preview")
    
    preview_topic = st.text_input("Preview topic", "AI Technology", key="preview")
    
    if preview_topic:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📘 Facebook Preview")
            st.markdown(f"""
            <div style="background: #f0f2f5; padding: 15px; border-radius: 10px;">
                <strong>🤖 {preview_topic} - The Future</strong><br>
                Discover how {preview_topic} is changing everything!<br>
                <small>#{preview_topic.replace(' ', '')} #Tech #Innovation</small>
                <div>👍 Like 💬 Comment 🔄 Share</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 📸 Instagram Preview")
            st.markdown(f"""
            <div style="background: linear-gradient(45deg, #f09433, #d62976); padding: 15px; border-radius: 10px; color: white;">
                <strong>✨ {preview_topic}</strong><br>
                Amazing {preview_topic} content!<br>
                <small>#{preview_topic.replace(' ', '')} #Trending</small>
                <div>❤️ Like 💬 Comment 📤 Share</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 🔗 LinkedIn Preview")
            st.markdown(f"""
            <div style="background: white; border: 1px solid #e0e0e0; padding: 15px; border-radius: 10px;">
                <strong>👔 Professional {preview_topic}</strong><br>
                Industry insights on {preview_topic}<br>
                <small>#{preview_topic.replace(' ', '')} #Business</small>
                <div>👍 Like 💬 Comment 🔄 Repost</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 🐦 Twitter Preview")
            st.markdown(f"""
            <div style="background: black; padding: 15px; border-radius: 10px; color: white;">
                <strong>🐦 {preview_topic}</strong><br>
                Breaking: {preview_topic} news!<br>
                <small>#{preview_topic.replace(' ', '')}</small>
                <div>🔁 Retweet ❤️ Like 💬 Reply</div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("🎯 **Try it now!** Enter any topic and click 'RUN AUTOMATION TEST' to see the complete workflow")

# Step 5: Run the app
!streamlit run app.py & npx localtunnel --port 8501
