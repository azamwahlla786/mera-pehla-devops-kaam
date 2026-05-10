from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# 1. Main Page (Index) ke liye
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# 2. Baaqi HTML pages ke liye (about, portfolio, etc.)
@app.route('/<string:page_name>.html')
def render_static(page_name):
    return send_from_directory('.', f'{page_name}.html')

# 3. Static files (Images, CSS, JS) ke liye
@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    # Azure environment variables se port leta hai
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
