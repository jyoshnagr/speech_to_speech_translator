from translate import Translator
from config import SOURCE_LANG, TARGET_LANG

def translate_text(text):
    print(f"🌍 Translating from {SOURCE_LANG} → {TARGET_LANG}")
    translator = Translator(from_lang=SOURCE_LANG, to_lang=TARGET_LANG)
    translated = translator.translate(text)
    print(f"💬 Translated: {translated}")
    return translated
