from pydub import AudioSegment
from pydub.playback import play
from config import OUTPUT_AUDIO

def play_output():
    print("▶️ Playing translated speech...")
    sound = AudioSegment.from_mp3(OUTPUT_AUDIO)
    play(sound)
