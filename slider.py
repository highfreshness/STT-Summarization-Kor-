import streamlit as st

def slide():
    max_len = st.slider(
                "요약될 문장의 최대 길이를 설정해 주세요",
                min_value=20,
                max_value=100,
                value=20,
                help="요약된 문장의 최대 길이를 설정할 수 있습니다.",
            )
    return max_len