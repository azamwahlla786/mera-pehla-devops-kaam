from flask import Flask, send_from_directory
import os

# 1. Flask app initialize karein
app = Flask(__name__, static_folder='.')

# 2. Home route
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# 3. Dynamic route for other HTML files
@app.route('/<path:path>')
def serve_static(path):
    # Agar file exist karti hai toh usay bhej do
    if os.path.exists(path):
        return send_from_directory('.', path)
    # Agar nahi toh index par bhej do (ya 404)
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    # Azure environment variables se port pick karta hai
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
