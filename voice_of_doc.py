import pygame
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


#input_text="Hi this is Ai with Hassan!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

import time

def text_to_speech_with_gtts(input_text, output_mp3="output.mp3"):
    language = "en"

    # Save as MP3 first
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_mp3)

    pygame.mixer.init()
    pygame.mixer.music.load(output_mp3)
    pygame.mixer.music.play()

    # Wait for audio to finish
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    


