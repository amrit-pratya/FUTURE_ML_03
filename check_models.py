import os
import google.generativeai as genai

try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except:
    print("Error: Could not find the GOOGLE_API_KEY in your environment.")
    print("Please set the environment variable and try again.")
    exit()

print("--- Available Models for your API Key ---")

for m in genai.list_models():
  # Check if the model supports the 'generateContent' method
  if 'generateContent' in m.supported_generation_methods:
    print(f"Model Name: {m.name}")

print("-----------------------------------------")
print("Find a model name from the list above and update your test_bot.py file.")