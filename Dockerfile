# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose Render port (Render auto-assigns PORT)
EXPOSE 10000

# Run the Flask app via Gunicorn
CMD gunicorn api.index:app --bind 0.0.0.0:$PORT
