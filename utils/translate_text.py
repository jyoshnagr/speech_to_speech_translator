from translate import Translator
# from config import SOURCE_LANG, TARGET_LANG

def translate_text(text, source_lang, target_lang):
    print(f"🌍 Translating from {source_lang} → {target_lang}")
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translated = translator.translate(text)
    print(f"💬 Translated: {translated}")
    return translated
