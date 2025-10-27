
from utils.record_speech import record_and_recognize
from utils.translate_text import translate_text
from utils.text_to_speech import speak_text
from utils.play_audio import play_output

def main():
    print("=== 🌐 Speech-to-Speech Translator ===")
    text = record_and_recognize()
    if text:
        translated = translate_text(text)
        speak_text(translated)
        play_output()

if __name__ == "__main__":
    main()
