import os
from datetime import datetime
from pytz import timezone
from stt import stt_wav
import streamlit as st

class Catch_Audio():
    def __init__(self, audio):
        self.time = datetime.now(timezone("Asia/Seoul")).strftime("%y%m%d_%H%M%S")
        self.audio = audio
    
    def mic_make_wav(self):
        if not os.path.exists("audiobox"):
            os.makedirs("audiobox")
        self.path = f"./audiobox/{self.time}"
        wav_file = open(f"{self.path}.mp3", "wb")
        wav_file.write(self.audio.tobytes())
        commandwav = f"ffmpeg -i {self.path}.mp3 {self.path}.wav"
        os.system(commandwav)
        return f"{self.path}.wav"
    
    def drop_mp3_wav(self):
        try:
            os.remove(f"{self.path}.mp3")
            os.remove(f"{self.path}.wav")
        except FileExistsError:
            pass