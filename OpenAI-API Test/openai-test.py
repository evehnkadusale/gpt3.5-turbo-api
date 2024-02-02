from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an assistant for AI-powered web application for legal guides against workplace discrimination in the Philippines."},
    {"role": "user", "content": "Help me to find out the laws and regulations that apply to my case. My case is about workplace discrimination against women in the Philippines."},
  ]
)

print(completion.choices[0].message)