from dotenv import load_dotenv
from openai import OpenAI
import os
import gradio as gr

load_dotenv()

apikey= os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=apikey)


def generate_response(prompt,response):
    response = client.completions.create(model="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=60,
    n=1,
    stop=None,
    temperature=0.5)
    message = response.choices[0].text.strip()
    return message

iface = gr.ChatInterface(
    fn=generate_response,
    type="messages"
)

iface.launch()