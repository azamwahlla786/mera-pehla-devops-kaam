from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# 1. Home Page (index.html)
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# 2. Saare HTML Pages (about.html, portfolio.html, etc.)
@app.route('/<path:filename>')
def serve_static(filename):
    if filename.endswith('.html'):
        return send_from_directory('.', filename)
    return send_from_directory('.', filename)

if __name__ == "__main__":
    # Azure automatically assigns a PORT, humein usey pick karna hota hai
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
