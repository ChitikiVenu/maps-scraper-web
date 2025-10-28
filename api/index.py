from flask import Flask, request, send_file, jsonify
import pandas as pd
import io
from datetime import datetime

app = Flask(__name__)

# -----------------------------
# Root route (homepage)
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    return """
    <h2>Google Maps Scraper – Online</h2>
    <p>✅ Backend is live and working!</p>
    <p>Go to <a href="/static/index.html">Click here to open the Web App</a>.</p>
    """

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
# Local run (ignored by Render)
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
