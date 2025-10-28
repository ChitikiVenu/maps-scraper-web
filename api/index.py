from flask import Flask, request, send_file, jsonify, send_from_directory
import pandas as pd
import io
import os
from datetime import datetime

# Tell Flask where your static folder is (one level up)
app = Flask(__name__, static_folder="../static", static_url_path="/static")

# -----------------------------
# Root route (homepage)
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    """Serve the frontend HTML"""
    return send_from_directory(app.static_folder, "index.html")

# -----------------------------
# Scraper API route
# -----------------------------
@app.route("/api/scrape", methods=["POST"])
def scrape():
    try:
        data = request.get_json(force=True)
        keywords = data.get("keywords", [])

        # Dummy scraper logic (replace this later with real scraping)
        results = [{"Keyword": k, "Result": f"Scraped data for {k}"} for k in keywords]

        # Generate Excel file in memory
        df = pd.DataFrame(results)
        output = io.BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)

        filename = f"maps_results_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
        return send_file(output, download_name=filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# Health check route
# -----------------------------
@app.route("/api/health", methods=["GET"])
def health():
    """Simple health check"""
    return jsonify({"status": "ok"}), 200

# -----------------------------
# Local run (for development)
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
