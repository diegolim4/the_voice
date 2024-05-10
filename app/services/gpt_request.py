import requests
import os

def gpt_request(ask):
    try:
        token = os.getenv('OPENAI_API_KEY')
        base_url = os.getenv('OPENAI_API_BASE_URL')
        instructions_path = "app/services/instruction_prompt/instructions.txt"

        with open(instructions_path, 'r', encoding='utf-8') as file:
            instructions = file.read()

        url = f'{base_url}chat/completions'
        headers = {
            "Authorization": f"Bearer {token}"
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": instructions},
                {"role": "user", "content": ask}
            ],
            "max_tokens": 150,
            "temperature": 0,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": [" Human:", " AI:"]
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["choices"][0]

    except Exception as e:
        print(f"Erro gpt-request: {e}")
        return e
