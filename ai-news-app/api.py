from fastapi import FastAPI, Query
from services.news_service import fetch_real_news
from services.ai_service import summarize_articles
from db.database import init_db, save_news_summary

app = FastAPI()
init_db()

@app.get("/news")
def get_news(topic: str = Query("artificial intelligence", description="Search topic for news")):
    articles = fetch_real_news(topic=topic)
    summary = summarize_articles(articles)
    save_news_summary(topic, summary)
    return {
        "topic": topic,
        "article_count": len(articles),
        "summary": summary
    }
