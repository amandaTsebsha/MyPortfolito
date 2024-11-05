# Main Flask application file
# ├── app.py                # Main Flask application file
# ├── templates/            # HTML templates
# ├── static/               # CSS, JavaScript, and images
# ├── certificates/         # Certificate images
# ├── venv/                 # Virtual environment
# └── Procfile              # Required for deployment on Heroku

from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)