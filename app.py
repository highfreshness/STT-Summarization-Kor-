import streamlit as st
from audiorecorder import audiorecorder
from summarization import summarization_text
from slider import slide
from stt import stt_wav
from catch_audio import Catch_Audio


st.markdown("## **π€ STT(Speech To Text) & β­Summarization**")

option = st.selectbox("μλ ₯ λ°©μμ μ νν΄μ£ΌμΈμ", ("λ§μ΄ν¬", ".wav νμΌ μλ‘λ"))

if option == "λ§μ΄ν¬":
    max_len = slide()
    audio = audiorecorder("λΉμ μμ", "λΉμ μ€...")
    CA = Catch_Audio(audio)
    
    if len(CA.audio) > 0:
        # To play audio in frontend:
        st.audio(CA.audio)
        # To save audio to a file:
        wav_file_path = CA.mic_make_wav()
        result = stt_wav(wav_file_path)
        st.code(summarization_text(result), language='python')
        CA.drop_mp3_wav()

elif option == ".wav νμΌ μλ‘λ":
    try:
        uploaded_files = st.file_uploader(".wav νμ₯μ νμΌμ λ£μ΄μ£ΌμΈμ", accept_multiple_files=False)
        max_len = slide()
        preprocessing = stt_wav(uploaded_files)
        st.markdown("### π λν λ΄μ© μμ½")
        with st.spinner('νμ€νΈλ₯Ό μμ½νλ μ€ μλλ€.'):  
            st.code(summarization_text(preprocessing), language='python')
    except AssertionError:
        pass
