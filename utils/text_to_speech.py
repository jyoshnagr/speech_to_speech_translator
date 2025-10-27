from gtts import gTTS
from config import TARGET_LANG, OUTPUT_AUDIO
import os
OUTPUT_AUDIO = "translated_audio.wav"

def speak_text(text):
    print("🔊 Converting translated text to speech...")
    tts = gTTS(text=text, lang=TARGET_LANG)
    tts.save(OUTPUT_AUDIO)
    print(f"✅ Saved translated speech to {OUTPUT_AUDIO}")
    # return OUTPUT_AUDIO
    return os.path.abspath(OUTPUT_AUDIO)
