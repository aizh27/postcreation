import streamlit as st
import google.generativeai as genai
from streamlit_extras.stylable_container import stylable_container

# Load your API Key (store this in .streamlit/secrets.toml in deployment)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

# App UI
st.title("📱 Social Media Trend Post Generator")
st.markdown("Generate **trending topic posts** with AI-generated **captions** and **hashtags**")

# Input fields
platform = st.selectbox("Choose Platform", ["Instagram", "LinkedIn", "Twitter", "Facebook", "YouTube"])
custom_interest = st.text_input("Your Area of Interest (optional)", placeholder="e.g., AI, Fashion, Startups")

# Generate Button
if st.button("Generate Trending Post"):
    with st.spinner("Thinking..."):
        # Prompt Engineering
        prompt = f"""
        You are a social media trend analyst and content creator.
        Identify 3 currently trending topics based on recent global or niche interests{f" in {custom_interest}" if custom_interest else ""}.
        For each topic, write:
        1. A short, catchy caption suitable for {platform}
        2. 5-7 relevant and trending hashtags

        Output format:
        ### Topic Title
        Caption: ...
        Hashtags: ...
        """
        try:
            response = model.generate_content(prompt)
            st.success("Here's your AI-powered trending post pack:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error generating content: {e}")
