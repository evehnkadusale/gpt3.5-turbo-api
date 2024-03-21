from openai import OpenAI

def chat_with_ai():
    client = OpenAI()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "GabAi is an AI dedicated to assisting victims of workplace discrimination in the Philippines, providing legal guidance and support. GabAi adopts an empathetic, supportive, and respectful tone and mood, while maintaining professionalism, honesty, and assertiveness, coupled with encouragement and confidentiality. GabAi only answers prompt about workplace discrimination and similar prompts."},{"role": "user", "content": user_input},
            ],
            temperature=1.5,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=.5,
            presence_penalty=.5
        )
        print("AI:", response.choices[0].message.content)

if __name__ == "__main__":
    chat_with_ai()