from gtts import gTTS
from playsound import playsound
import os

def text_to_speech_with_gtts(input_text, output_mp3="output.mp3"):
    language = "en"

    if os.path.exists(output_mp3):
        try:
            os.remove(output_mp3)
        except PermissionError:
            print(f" Cannot delete {output_mp3}: file in use.")
            return

   
    tts = gTTS(text=input_text, lang=language, slow=False)
    tts.save(output_mp3)

    try:
        playsound(output_mp3)
    except Exception as e:
        print(f"Error playing sound: {e}")
