from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)


class ChatBot:

    def __init__(self):
        pass

    def get_response(self, user_input):
        response = client.completions.create(model="gpt-3.5-turbo-instruct",
                                             prompt=user_input,
                                             max_tokens=3000,
                                             temperature=0.7).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = ChatBot()
    response_g = chatbot.get_response("Write a joke about birds.")
    print(response_g)
