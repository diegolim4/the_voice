from openai import OpenAI
import os

def transcribe_audio(audio_file):
    try:
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

        audio_file= open(audio_file, "rb")

        transcription = client.audio.transcriptions.create(
          model="whisper-1", 
          file=audio_file
        )

        return transcription.text
    except Exception as e:
        return f'Erro - transcribe_audio: {e}'
