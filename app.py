import streamlit as st
from audiorecorder import audiorecorder
from summarization import summarization_text
from slider import slide
from stt import stt_wav
from catch_audio import Catch_Audio


st.markdown("## **🎤 STT(Speech To Text) & ⭐Summarization**")

option = st.selectbox("입력 방식을 선택해주세요", ("마이크", ".wav 파일 업로드"))

if option == "마이크":
    max_len = slide()
    audio = audiorecorder("녹음 시작", "녹음 중...")
    CA = Catch_Audio(audio)
    
    if len(CA.audio) > 0:
        # To play audio in frontend:
        st.audio(CA.audio)
        # To save audio to a file:
        wav_file_path = CA.mic_make_wav()
        result = stt_wav(wav_file_path)
        st.code(summarization_text(result), language='python')
        CA.drop_mp3_wav()

elif option == ".wav 파일 업로드":
    try:
        uploaded_files = st.file_uploader(".wav 확장자 파일을 넣어주세요", accept_multiple_files=False)
        max_len = slide()
        preprocessing = stt_wav(uploaded_files)
        st.markdown("### 🔑 대화 내용 요약")
        with st.spinner('텍스트를 요약하는 중 입니다.'):  
            st.code(summarization_text(preprocessing), language='python')
    except AssertionError:
        pass
