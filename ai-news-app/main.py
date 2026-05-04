import sys
from services.news_service import fetch_real_news
from services.ai_service import summarize_articles
from services.email_service import send_email
from db.database import init_db, save_news_summary


def run_news_pipeline(topic="artificial intelligence"):
    init_db()
    articles = fetch_real_news(topic=topic)
    summary = summarize_articles(articles)

    print("\n📰 DAILY NEWS DIGEST\n")
    print(summary)

    save_news_summary(topic, summary)
    send_email(summary)


if __name__ == "__main__":
    topic = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "artificial intelligence"
    run_news_pipeline(topic)
