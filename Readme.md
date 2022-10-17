# 음성인식 기반 대화 요약 서비스

## [프로젝트 소개]

STT( Speech To Text )를 통해 대화내용을 문자로 변환 후  Summarization model을 통해 내용을 요약

## [담당 업무]

Streamlit을 이용한 Web 개발

## [기술스택] 

개발환경 : Docker, Linux

사용 언어 : Python

웹 구현 : Streamlit

STT : pyaudio, ffmpeg, SpeechRecognition

문서 요약 : PyTorch

## [주요 과업]

< STT >

- SpeechRecognition 라이브러리를 이용해 STT 구현
- streamlit 오디오 레코더 컴포넌트 [링크](https://github.com/theevann/streamlit-audiorecorder) 를 활용해 음성을 입력 받아 mp3 파일 저장
- SpeechRecognition 라이브러리로 음성 파일 전달

< Summarization >

* STT를 통해 변환된 텍스트를 NLP Summarization Task 모델에 넣어 내용을 요약
* alaggung/bart-r3f 모델 사용
  * 데이터 : AIHub 한국어 대화요약 데이터

< 웹 서비스 >

* Streamlit을 통해 프론트엔드 부분을 컴포넌트를 이용해 화면을 만들고 웹 서비스를 구동해 서비스 구현 



< 중요하게 생각한 부분 >

* 2명 이상이 동시에 기능을 사용해도 정상적으로 결과를 얻는 것
* Web으로 구현했을 때 간략하고 깔끔하게 기능들을 표현하고 사용할 수 있을 것



## [문제점]

* STT에 필요한 라이브러리 중 OS에 따라 설치가 정상적으로 되지 않는 라이브러리가 존재 (pyaudio, ffmpeg 등)

  > Docker를 이용해 Linux 가상환경을 구축해 프로젝트 진행 ( Linux에서는 대부분의 라이브러리 설치가 정상적으로 진행되는 것을 확인)

* SpeechRecognition 라이브러리에서 wav 확장자를 음성으로 받아 텍스트로 변경해주는데 웹을 통해 받은 음성을 바로 wav 확장자로 받아 넘길 경우 wav 파일의 포맷 오류 발생

  > 테스트 결과 mp3 파일로 변환 후 ffmpeg를 이용해 wav 파일로 변환하면 정상적으로 처리되는 것을 확인  

* Streamlit을 이용한 직접 배포 불가

  > Streamlit에서 제공해주는 배포 서비스를 이용하려고 했으나 pip 로 설치하지 않는 라이브러리가 있는 경우 별도 설치가 불가하기 때문에 Streamlit을 통한 배포는 불가능했다.

* 웹브라우저에서 음성 입력 사용 불가

  > 음성 입력 시 MediaRecorder Web API를 사용하는데 localhost / SSL 인증이된 서버에서만 사용이 가능한 것 같았다. 
