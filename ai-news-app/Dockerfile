# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
EXPOSE 8000

# Default command (runs API)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]