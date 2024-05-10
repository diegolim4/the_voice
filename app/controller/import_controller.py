from flask import jsonify, send_file

from ..actions.get_voice import catch_audio
from ..actions.transcribe_audio import transcribe_audio
from ..actions.text_to_audio import converte_text_to_audio
from ..actions.convertToBase64 import converte_to_base64

from ..services.gpt_request import gpt_request

import time

def insert_voice_controller():
    try:
        catch_audio()

        audio_file_path = "app/audios/audio_gravado.wav"

        transcript = transcribe_audio(audio_file_path)

        response_ask = gpt_request(transcript)
        
        converte_text_to_audio(response_ask['message']['content'])

        time.sleep(1)
        resp_gpt_audio_path = 'audios/resp_gpt.mp3'

        return send_file(resp_gpt_audio_path, mimetype='audio/mp3'), 200


    except Exception as e:
        print('insert_voice_controller - error: ', e)
        return jsonify({'error': str(e)}), 500
