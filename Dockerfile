# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Google Cloud Speech
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy server directory
COPY server/ ./server/

# Copy any configuration files needed
COPY start_backend.py .

# Expose port (Render will set PORT env variable)
EXPOSE 4000

# Set environment variable for production
ENV FLASK_ENV=production

# Use gunicorn to run the Flask app
CMD gunicorn --bind 0.0.0.0:$PORT --workers 4 --timeout 120 server.proxy:app
