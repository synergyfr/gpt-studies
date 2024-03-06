from openai import OpenAI
client = OpenAI(api_key='')

chat_messages = []

while True:

    user_message = input("You: ")

    chat_messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=chat_messages,
      temperature=0
    )

    ai_response = response.choices[0].message.content
    chat_messages.append({"role": "assistant", "content": ai_response})
    print("AI: ", ai_response)
