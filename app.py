import streamlit as st
from gtts import gTTS
import io
from streamlit_mic_recorder import mic_recorder

# 1. Page Setup
st.set_page_config(page_title="Deutsch AI Tutor", page_icon="🇩🇪", layout="centered")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_scale=True)

# 2. Title & Sidebar
st.title("🤖 Deutsch AI Tutor")
st.sidebar.title("Navigation")
menu = ["Home", "Reading & Listening", "Writing Practice", "Speaking Practice"]
choice = st.sidebar.radio("Choose a skill to practice:", menu)

# --- HOME PAGE ---
if choice == "Home":
    st.subheader("Willkommen! (Welcome!)")
    st.write("This app helps you master German through four key pillars. Select a module in the sidebar to begin.")
    st.image("https://unsplash.com", caption="Brandenburg Gate, Berlin")
    
    st.markdown("""
    ### Your Daily Goals:
    - [ ] Practice **Listening** to native-like audio.
    - [ ] Complete 5 **Writing** translations.
    - [ ] Record yourself **Speaking** 3 sentences.
    """)

# --- READING & LISTENING ---
elif choice == "Reading & Listening":
    st.header("Reading & Listening")
    st.write("Read the sentence and listen to the pronunciation.")
    
    # Practice Content
    practice_text = "Heute ist das Wetter wirklich ausgezeichnet."
    translation = "Today the weather is truly excellent."
    
    st.info(f"**German:** {practice_text}")
    st.caption(f"**English:** {translation}")
    
    if st.button("🔊 Play Audio"):
        with st.spinner("Generating German audio..."):
            tts = gTTS(text=practice_text, lang='de')
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            st.audio(audio_fp, format='audio/mp3')

# --- WRITING PRACTICE ---
elif choice == "Writing Practice":
    st.header("Writing Practice")
    st.write("Translate the following into German:")
    
    challenge = "Where is the nearest train station?"
    st.warning(f"**English:** {challenge}")
    
    user_input = st.text_input("Your German translation:", placeholder="Type your answer here...")
    
    if st.button("Check Answer"):
        correct = "Wo ist der nächste Bahnhof"
        # Clean input for easier matching
        clean_user = user_input.strip().lower().replace("?", "").replace(".", "")
        clean_correct = correct.lower()
        
        if clean_user == clean_correct:
            st.success("🎉 Ausgezeichnet! (Excellent!)")
        else:
            st.error(f"Try again! The correct version is: **{correct}?**")
            st.write("Note: In German, 'Bahnhof' is masculine (der) and capitalized.")

# --- SPEAKING PRACTICE ---
elif choice == "Speaking Practice":
    st.header("Speaking Practice")
    st.write("Repeat the sentence below out loud.")
    
    sentence_to_say = "Ich möchte gerne einen Kaffee bestellen."
    st.info(f"**Say this:** {sentence_to_say}")
    
    # Microphone implementation
    st.write("Click the button below, say the sentence, then stop:")
    audio = mic_recorder(
        start_prompt="🎙️ Start Recording",
        stop_prompt="⏹️ Stop & Save",
        key='recorder'
    )

    if audio:
        st.success("Recording captured!")
        st.audio(audio['bytes'])
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("Your Voice ☝️")
        with col2:
            if st.button("Hear Native Guide"):
                tts = gTTS(text=sentence_to_say, lang='de')
                audio_fp = io.BytesIO()
                tts.write_to_fp(audio_fp)
                st.audio(audio_fp, format='audio/mp3')
