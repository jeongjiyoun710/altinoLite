import speech_recognition as sr

# 음성 인식기 인스턴스 생성
recognizer = sr.Recognizer()

# 마이크를 음성 소스로 사용
with sr.Microphone() as source:
    print("말씀해 주세요...")
   
    # 잡음 수준을 자동으로 조정
    recognizer.adjust_for_ambient_noise(source)
   
    # 음성을 들음
    audio_data = recognizer.listen(source)
   
    try:
        # 음성을 텍스트로 변환 (한글 인식)
        text = recognizer.recognize_google(audio_data, language='ko-KR')
        print(f"인식된 텍스트: {text}")
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"구글 음성 인식 서비스에 문제가 있습니다: {e}")
