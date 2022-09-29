# python 3.8 버전 이미지
FROM python:3.8 

EXPOSE 8501

# 작업 디렉토리
WORKDIR /app

# 현재 디렉토리 위치의 전체 파일을 docker 생성 시 /app 디렉토리로 복사
COPY . /app

# 컨테이너 생성 시 미리 동작하는 명령어
RUN apt update
RUN apt install -y vim
RUN apt-get install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
RUN apt-get install -y ffmpeg
RUN apt-get install flac
RUN pip install -r requirements.txt