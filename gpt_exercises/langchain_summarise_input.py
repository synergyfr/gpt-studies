from openai import OpenAI
client = OpenAI(api_key='')

chat_messages = []

input_text = input('Enter text that should be summarized: ')

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {'role': 'system', 'content': 'You are a text summarizer chat bot. Your goal is to summarize the text that is given to you by the user.'},
        {'role': 'user', 'content': input_text}
    ],
    temperature=0
)

ai_response = response.choices[0].message.content
print("Summarized text:\n\n ", ai_response)