from openai import OpenAI

def chat_with_ai():
    client = OpenAI()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a workplace discrimination legal assistant in the Philippines."},
                {"role": "user", "content": user_input},
            ]
        )
        print("AI:", response.choices[0].message.content)

if __name__ == "__main__":
    print("AI: Hi! I'm a workplace discrimination legal assistant. How can I help you today?")
    chat_with_ai()
