import openai

openai.api_key = ' '

def ask_gpt3(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150


    )
    return response.choices[0].text.strip()
while True:
    question = input("Posez votre question : ")
    print(ask_gpt3(question))
