import openai
from dotenv import dotenv_values


class Chatbot:
    def __init__(self):
        config = dotenv_values(".env")
        openai.api_key = config['OPENAI_API_KEY']

    def get_response(self, user_input):
        completion = openai.completions.create(
            model="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return completion


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a dirty joke about fisherman")
    print(response)
