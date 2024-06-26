import requests

def get_gpt_list(api_key):
    try:
        response = requests.get(
            "https://api.openai.com/v1/models",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        response_json = response.json()
        return [{"name": model['id']} for model in response_json['data']]
    except Exception as e:
        return [{"name": f"Error: {e}"}]

def send_message_to_gpt(message, api_key, has_gpt4):
    try:
        engine = "gpt-4" if has_gpt4 else "davinci-codex"
        response = requests.post(
            f"https://api.openai.com/v1/engines/{engine}/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "prompt": message,
                "max_tokens": 150,
                "n": 1,
                "stop": None,
                "temperature": 0.5,
            }
        )
        response_json = response.json()
        return response_json['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error: {e}"
