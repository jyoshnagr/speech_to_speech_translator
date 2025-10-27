import speech_recognition as sr
from config import SOURCE_LANG, INPUT_AUDIO

def record_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)
        print("🧠 Recognizing speech...")

        try:
            text = recognizer.recognize_google(audio, language=SOURCE_LANG)
            print(f"📝 Recognized: {text}")
            with open(INPUT_AUDIO, "wb") as f:
                f.write(audio.get_wav_data())
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand the audio.")
        except sr.RequestError:
            print("⚠️ Google API unavailable.")
    return None
