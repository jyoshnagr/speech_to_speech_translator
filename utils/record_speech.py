import speech_recognition as sr
from config import SOURCE_LANG, INPUT_AUDIO
import os

def record_and_recognize(audio_path=None, source_lang=None):
    recognizer = sr.Recognizer()

    if audio_path:
        # Load from uploaded file
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
    else:
        # Record from mic
        with sr.Microphone() as source:
            print("🎙️ Speak now...")
            audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing speech...")
        text = recognizer.recognize_google(audio, language=source_lang)
        print(f"📝 Recognized: {text}")

        # Save input audio to file
        with open(INPUT_AUDIO, "wb") as f:
            f.write(audio.get_wav_data())

        # ✅ Return both recognized text and file path
        return text, os.path.abspath(INPUT_AUDIO)

    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return None, None
    except sr.RequestError as e:
        print(f"⚠️ Recognition error: {e}")
        return None, None