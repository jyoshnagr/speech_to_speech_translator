# 🗣️ Speech-to-Speech Translator (Configurable)

Converts speech input into another language and plays the translated voice.

## ⚙️ Setup
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## ▶️ Run
```bash
python main.py
```

## 🌍 Change Languages
Edit `config.py`:
```python
SOURCE_LANG = "en"  # Input language
TARGET_LANG = "es"  # Output language
```

PyAudio==0.2.14

https://www.geeksforgeeks.org/nlp/speech-to-speech-translation/

Install Python 3.11

pyenv install 3.11.9


Set it locally (inside your project folder)

cd speech_translator
pyenv local 3.11.9


Create & activate venv

python -m venv venv
source venv/bin/activate


pyenv exec pip install -r requirements.txt

pyenv exec python main.py


