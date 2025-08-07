# imports
import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

# Call this function to load the API key from your .env file
load_dotenv()

# Initialize the OpenAI client
# It will now find the OPENAI_API_KEY from your environment
client = OpenAI() 

draft = input("Add your draft here! : \n")

system_prompt = """You are an assistant who excels in reviewing and making changes to emails. 
Analyze the contents of the email and provide your suggestions in a clear, well-formatted response using Markdown. 
The response should include:
- A bolded, suggested subject line.
- A bulleted list of suggested grammatical or content changes.
- A fully revised email with the changes implemented.
"""
user_prompt = draft

# Step 2: Make the messages list
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# Step 3: Call OpenAI
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

# Step 4: print the result
print(response.choices[0].message.content)