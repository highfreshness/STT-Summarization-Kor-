import os
import streamlit as st
from stt import stt_wav
from audiorecorder import audiorecorder
from summarization import summarization_text
from pydub import AudioSegment



st.markdown("# **🎤 STT(Speech To Text) & ⭐Summarization**")

option = st.selectbox("입력 방식을 선택해주세요", ("마이크", ".wav 파일 업로드"))

if option == "마이크":
    audio = audiorecorder("녹음 시작", "녹음 중...")

    if len(audio) > 0:
    # To play audio in frontend:
        st.audio(audio)
        # To save audio to a file:
        wav_file = open("audio.mp3", "wb")
        wav_file.write(audio.tobytes())
        ###
        AudioSegment.from_mp3("./audio.mp3").export("./src.wav", format="wav")
        ###
        # commandwav = "ffmpeg -y -i audio.mp3 audio.wav"
        # os.system(commandwav)
        try:
            preprocessing = stt_wav("src.wav")
            st.markdown("### 🔑 대화 내용 요약")
            with st.spinner('텍스트를 요약하는 중 입니다.'):
                st.code(summarization_text(preprocessing), language='python')
        except FileNotFoundError:
            st.error("음성이 입력되지 않았습니다. 다시 입력해주세요", icon="🚨")

elif option == ".wav 파일 업로드":
    try:
        uploaded_files = st.file_uploader(".wav 확장자 파일을 넣어주세요", accept_multiple_files=False)
        preprocessing = stt_wav(uploaded_files)
        st.markdown("### 🔑 대화 내용 요약")
        with st.spinner('텍스트를 요약하는 중 입니다.'):
            st.code(summarization_text(preprocessing), language='python')
    except AssertionError:
        pass

# 사용했던 음성 파일 삭제
try:
    os.remove("audio.mp3")
    os.remove("audio.wav")
except FileNotFoundError:
    pass
