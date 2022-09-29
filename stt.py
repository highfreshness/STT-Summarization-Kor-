import streamlit as st
import speech_recognition as sr

def stt_wav(wav):
    r = sr.Recognizer()
    with sr.AudioFile(wav) as source:
        audio = r.record(source, duration=120) # 2분 제한
    result = r.recognize_google(audio, language="ko-KR")
    st.markdown("### 🎆 STT - 분석 대화 내용")
    st.code(result, language='python')
    return result 
    
# def stt_audio(sound):
#     r = sr.Recognizer()
#     audio = r.listen(sound)
#     result = r.recognize_google(audio, language="ko-KR")
#     st.markdown("### 🎆 - STT 분석 대화 내용")
#     st.code(result, language='python')
#     return result