import os
import requests
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI

load_dotenv(override=True)
API_KEY= os.getenv('OPENAI_API_KEY')
OpenAI_MODEL=os.getenv("OPENAI_MODEL")
OLLAMA_URL = os.getenv('OLLAMA_URL')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL')

# Call openai
openai = OpenAI()

# call ollama via openai
ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."

system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
        please provide a short summary of this website in markdown. \
            If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

# Messages
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

class Summarize():
    def __init__(self, website):
        self.website = website
    
    def summarize_using_openai(self):
        openai_response=openai.chat.completions.create(
            model=OpenAI_MODEL,
            messages=messages_for(self.website)
        )
        return display(Markdown(openai_response.choices[0].message.content))
    
    def summarize_using_ollama(self):
        ollama_response = ollama_via_openai.chat.completions.create(
            model=OLLAMA_MODEL,
            messages=messages_for(self.website)
        )
        return display(Markdown(ollama_response.choices[0].message.content))


        