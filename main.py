from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
import tempfile
import os
from utils.record_speech import record_and_recognize
from utils.translate_text import translate_text
from utils.text_to_speech import speak_text
from utils.play_audio import play_output
from fastapi.responses import FileResponse
import base64


app = FastAPI(title="Speech-to-Speech Translator API")

def main():
    print("=== 🌐 Speech-to-Speech Translator ===")
    text = record_and_recognize()
    if text:
        translated = translate_text(text)
        speak_text(translated)
        play_output()

@app.get("/")
def root():
    return {"message": "Welcome to the Speech-to-Speech Translator API"}


@app.post("/translate-text/")
def api_translate_text(text: str):
    """Translate plain text and play the translated speech."""
    translated = translate_text(text)
    speak_text(translated)
    play_output()
    return {"original": text, "translated": translated}


@app.post("/translate-audio/")
async def api_translate_audio(file: UploadFile = File(...)):
    """
    Upload an audio file → recognize → translate → synthesize → return translated audio + text
    """
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            temp_path = tmp.name
            tmp.write(await file.read())

        # Run speech recognition on uploaded audio
        text, input_audio_path = record_and_recognize(temp_path)
        if not text:
            raise HTTPException(status_code=400, detail="Speech could not be recognized")

        # Translate text
        translated = translate_text(text)

        # Generate translated speech file
        output_path = speak_text(translated)  # <-- Modify speak_text to return the file path
        # play_output()

        # Cleanup uploaded file
        os.remove(temp_path)

        # ✅ Return JSON + audio file path
        return FileResponse(
            path=output_path,
            filename="translated_audio.wav",
            media_type="audio/wav",
            headers={
                # "X-Recognized-Text": text,
                # "X-Translated-Text": translated
                "X-Recognized-Text": base64.b64encode(text.encode()).decode(),
                "X-Translated-Text": base64.b64encode(translated.encode()).decode()
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "api":
        # Run FastAPI server mode
        port = int(os.environ.get("PORT", 8000))
        # uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
        uvicorn.run("main:app", host="0.0.0.0", port=port)
    else:
        # Default CLI mode
        main()

