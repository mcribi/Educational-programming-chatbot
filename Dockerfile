# Use slim Python base image
FROM python:3.11-slim

# System dependencies for runtime 
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
  && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Install Python dependencies first
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the source code
COPY . /app

# Default environment variables (can be overridden by compose)
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/bot:/app

# Run the Telegram bot
CMD ["python", "-m", "bot.main"]

