from gtts import gTTS
import os
from io import BytesIO

from openai import OpenAI

def converte_text_to_audio(text_user):
    try:
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

        audio_file = 'app/audios/resp_gpt.mp3'

        response = client.audio.speech.create(            
            model='tts-1',
            voice='alloy',
            input=text_user
        )

        response.stream_to_file(audio_file)

        return audio_file
        
    except Exception as e:
        message_error = f'Erro ao converter texto para áudio: {e} '
        print(message_error)
        return message_error