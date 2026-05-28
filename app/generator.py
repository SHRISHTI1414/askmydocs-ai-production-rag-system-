from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_answer(query, context):

    prompt =f"""
You are an AI document analyst.

Answer ONLY from the provided context.

Rules:
- Do not hallucinate.
- Do not make up information.
- If information is unclear, say:
  "The document does not clearly mention this."
- Keep answers concise and structured.

If the user asks:
- "help me understand the document"
- "what is this document about"
- "summarize this pdf"

Then answer in this format:

Main Topic:
- ...

Key Subjects:
- ...
- ...
- ...

Important Concepts:
- ...
- ...

Summary:
- ...

Context:
{context}

Question:
{query}
"""

    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content