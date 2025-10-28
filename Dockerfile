# Use an older, stable Python base image
FROM python:3.10.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Render
EXPOSE 8000

# Start the Flask app with Gunicorn
CMD ["gunicorn", "api.index:app", "--bind", "0.0.0.0:8000"]
