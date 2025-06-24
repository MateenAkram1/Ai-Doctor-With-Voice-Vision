import logging
import pydub
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path,timeout=20,phrase_time_limit=None):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Please speak something...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Recording...")
            
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            wav_data = audio.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="wav", bitrate="128k")
            logging.info(f"Audio saved to {file_path}")
    
    except Exception as e:
        logging.error(f"Error during recording: {e}")
        return None
    

stt_model = "whisper-large-v3"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def transcribe_with_grok(stt_model,audio_file,GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    
    audio_file_path =open(audio_file, "rb")
    transcription = client.audio.transcriptions.create(
        file=audio_file_path,
        model=stt_model,
        language="en"
    )
    return transcription.text