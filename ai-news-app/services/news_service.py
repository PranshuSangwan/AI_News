import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
if not NEWSAPI_KEY:
    raise RuntimeError("NEWSAPI_KEY is not set in .env")


def fetch_real_news(topic="artificial intelligence", page_size=5):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "apiKey": NEWSAPI_KEY,
        "pageSize": page_size,
        "sortBy": "publishedAt",
        "language": "en"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()

    articles = []
    for article in data.get("articles", []):
        articles.append({
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "url": article.get("url", "")
        })

    return articles
