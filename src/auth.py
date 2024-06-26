import requests

def authenticate(email, password, api_key):
    try:
        user_auth_url = "http://127.0.0.1:5000/login"
        user_auth_data = {"email": email, "password": password}
        user_auth_response = requests.post(user_auth_url, json=user_auth_data)

        if user_auth_response.status_code != 200:
            print(f"User authentication failed: {user_auth_response.text}")
            return False, None

        user_data = user_auth_response.json()

        api_key_url = "https://api.openai.com/v1/models"
        headers = {"Authorization": f"Bearer {api_key}"}
        api_key_response = requests.get(api_key_url, headers=headers)

        if api_key_response.status_code != 200:
            print(f"API Key validation failed: {api_key_response.text}")
            return False, None

        models = api_key_response.json().get('data', [])
        has_gpt4 = any(model['id'] == 'gpt-4' for model in models)

        return user_data, has_gpt4

    except Exception as e:
        print(f"Authentication error: {e}")
        return False, None
