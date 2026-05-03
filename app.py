import streamlit as st
from gtts import gTTS
import io

# 1. Setup the App Name and Page Layout
st.set_page_config(page_title="Deutsch AI Tutor", page_icon="🇩🇪")

# Professional Header
st.title("🤖 Deutsch AI Tutor")
st.markdown("Your personal companion for learning German.")

# 2. Sidebar Navigation
st.sidebar.title("Navigation")
menu = ["Home", "Reading & Listening", "Writing Practice"]
choice = st.sidebar.radio("Go to", menu)

# --- HOME PAGE ---
if choice == "Home":
    st.subheader("Willkommen!")
    st.write("Pick a module from the sidebar to start practicing your German skills.")
    st.image("https://unsplash.com", caption="Lerne Deutsch!")

# --- READING & LISTENING ---
elif choice == "Reading & Listening":
    st.header("Reading & Listening Practice")
    st.write("Read the sentence below and click the button to hear the correct pronunciation.")
    
    # Practice Sentence
    german_text = "Ich lerne Deutsch mit meinem KI-Tutor."
    st.info(f"**German:** {german_text}")
    st.write("**English Translation:** I am learning German with my AI tutor.")
    
    # Text-to-Speech (Listening)
    if st.button("🔊 Listen to German"):
        with st.spinner("Generating audio..."):
            # Create the audio file using Google Text-to-Speech
            tts = gTTS(text=german_text, lang='de')
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            st.audio(audio_fp, format='audio/mp3')

# --- WRITING PRACTICE ---
elif choice == "Writing Practice":
    st.header("Writing Practice")
    st.write("Translate the following sentence into German:")
    st.warning("**English:** The weather is very nice today.")
    
    # User Input for Writing
    user_answer = st.text_input("Your German translation:", placeholder="Type here...")
    
    if st.button("Check My Answer"):
        correct_answer = "Das Wetter ist heute sehr schön"
        # Simple check (stripping punctuation and making it lowercase for easier matching)
        if user_answer.strip().lower().replace(".", "") == correct_answer.lower():
            st.success("🎉 Richtig! Excellent work.")
        else:
            st.error(f"Nicht ganz. The correct answer is: **{correct_answer}.**")
            st.write("Tip: Remember that German nouns like 'Wetter' are always capitalized!")
