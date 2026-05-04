# AI News Aggregator API

A small backend that fetches real news from NewsAPI, summarizes and ranks it using OpenAI, stores results in SQLite, exposes a FastAPI endpoint, and sends daily email digests.

## Setup

1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
2. Add required keys to `.env`:
   - `OPENAI_API_KEY`
   - `NEWSAPI_KEY`
   - `EMAIL_SENDER`
   - `EMAIL_PASSWORD`
   - `EMAIL_RECEIVER`
3. Run the API server:
   ```powershell
   uvicorn api:app --reload
   ```
4. Open:
   ```text
   http://127.0.0.1:8000/news
   ```

## Docker Run

1. Build the image:
   ```powershell
   docker build -t ai-news-app .
   ```
2. Run the container:
   ```powershell
   docker run -p 8000:8000 --env-file .env ai-news-app
   ```
3. Open:
   ```text
   http://127.0.0.1:8000/news
   ```

## Local run

```powershell
python main.py
```

## What changed

- `services/news_service.py` fetches real news from NewsAPI
- `services/ai_service.py` summarizes and ranks articles via OpenAI
- `db/database.py` stores summaries in SQLite
- `services/email_service.py` sends the digest by email
- `api.py` exposes `/news` as a backend API

## 🚀 Features
- Real-time news ingestion (NewsAPI)
- LLM-based ranking & summarization (OpenAI GPT-4o-mini)
- REST API using FastAPI
- SQLite database for storage
- Email automation via SMTP
- Dockerized for deployment

## 🛠️ Tech Stack
- Python, FastAPI
- OpenAI API
- SQLite
- Docker
