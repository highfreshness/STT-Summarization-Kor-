import streamlit as st
import speech_recognition as sr
from datetime import datetime

def stt_wav(wav):
    r = sr.Recognizer()
    with sr.AudioFile(wav) as source:
        audio = r.record(source, duration=120) # 2λΆ μ ν
    result = r.recognize_google(audio, language="ko-KR")
    st.markdown("### π STT - λΆμ λν λ΄μ©")
    st.code(result, language='python')
    return result 
    
# def stt_audio(sound):
#     r = sr.Recognizer()
#     audio = r.listen(sound)
#     result = r.recognize_google(audio, language="ko-KR")
#     st.markdown("### π - STT λΆμ λν λ΄μ©")
#     st.code(result, language='python')
#     return result