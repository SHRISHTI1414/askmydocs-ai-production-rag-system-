import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def generate_answer(query, context):

    prompt = f"""
    You are a helpful AI assistant.

    Answer the question ONLY from the provided context.

    Context:
    {context}

    Question:
    {query}
    """

    response = model.generate_content(prompt)

    return response.text