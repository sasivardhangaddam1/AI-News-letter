import streamlit as st
from config.sources import NEWS_SOURCES

st.set_page_config(page_title="AI Newsletter MVP", page_icon="📰", layout="wide")

st.title("📰 Your Personalized AI Newsletter")
st.caption("Get curated AI insights delivered to your inbox every morning")

# Step 1: Topic Selection
st.subheader("1. Choose Your Topics")
selected_categories = st.selectbox(
    "Select your preferred topic:",
    options=list(NEWS_SOURCES.keys()),
    index=0,  # Default to first option (AI)
    key="topic_select"
)

st.write(f"You selected: {selected_categories}")

# Step 2: Email Input
st.subheader("2. Enter Your Email")
user_email = st.text_input(
    "Enter your email address:",
    placeholder="your@email.com",
    key="email_input"
)

# Step 3: Generate Button
if st.button("Generate My Newsletter", key="generate_btn"):
    st.success("🎉 Let's build the backend next!")
