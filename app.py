from flask import Flask, send_from_directory
import os

# Flask app initialize
app = Flask(__name__, static_folder='.')

# Home route
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Dynamic route for other files
@app.route('/<path:path>')
def serve_static(path):

    # Agar file exist karti hai to usay bhej do
    if os.path.exists(path):
        return send_from_directory('.', path)

    # Agar file na mile to index page kholo
    return send_from_directory('.', 'index.html')

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
