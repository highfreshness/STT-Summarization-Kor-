import os
import streamlit as st
from audiorecorder import audiorecorder
from summarization import summarization_text
from stt import stt_wav


st.markdown("## **🎤 STT(Speech To Text) & ⭐Summarization**")

option = st.selectbox("입력 방식을 선택해주세요", ("마이크", ".wav 파일 업로드"))

if option == "마이크":
    audio = audiorecorder("녹음 시작", "녹음 중...")
    if len(audio) > 0:
        # To play audio in frontend:
        st.audio(audio)
        # To save audio to a file:
        wav_file = open("audio.mp3", "wb")
        wav_file.write(audio.tobytes())
        commandwav = "ffmpeg -y -i audio.mp3 audio.wav"
        os.system(commandwav)
        preprocessing = stt_wav("audio.wav")
        st.code(summarization_text(preprocessing), language='python')

elif option == ".wav 파일 업로드":
    try:
        uploaded_files = st.file_uploader(".wav 확장자 파일을 넣어주세요", accept_multiple_files=False)
        preprocessing = stt_wav(uploaded_files)
        st.markdown("### 🔑 대화 내용 요약")
        with st.spinner('텍스트를 요약하는 중 입니다.'):
            st.code(summarization_text(preprocessing), language='python')
    except AssertionError:
        pass
# text = """
# 올 여름 혼자어때 둘이어때 셋이어때 올여름 여행어때 바다어때 여기어때
# 여행할 때 여기어때 여행어때 여기어때
# """
