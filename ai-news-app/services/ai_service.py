import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set in .env")

client = OpenAI(api_key=OPENAI_API_KEY)


def summarize_articles(articles):
    text = "\n".join([
        f"{article['title']} - {article['description']}" for article in articles
    ])

    prompt = f"""
    Summarize and rank the following news based on importance:

    {text}

    Give the top {len(articles)} items with short summaries.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
