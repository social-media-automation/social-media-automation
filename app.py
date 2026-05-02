import streamlit as st
import time

st.title("🤖 AI Social Media Automation Tool")

topic = st.text_input("Enter topic", "AI in Healthcare")

if st.button("Generate"):
    with st.spinner("Generating..."):
        time.sleep(1)

    st.success("Post Generated!")

    st.write(f"""
    🚀 {topic} is transforming the future!
    
    #AI #{topic.replace(' ', '')}
    """)
