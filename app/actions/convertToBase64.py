import base64


def converte_to_base64(file_path):
    try:
        with open(file_path, 'rb') as audio_file:

            audio_data = audio_file.read()

            return base64.b64encode(audio_data).decode('utf-8')
    except Exception as e:

        print(f"Erro ao converter para Base64: {e}")

        return None
