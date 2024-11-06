# Main Flask application file
# ├── app.py # Main Flask application file
# ├── templates/ # HTML templates
# │ ├── index.html # Main HTML template
# │ ├── projects.html # Projects page
# │ ├── skills.html # Skills page
# │ └── certificates.html # Certificates page
# ├── static/ # Static files (CSS, JS, images)
# │ ├── css/
# │ │ └── styles.css # Main CSS file
# │ ├── js/
# │ │ └── scripts.js # JavaScript file for interactivity
# │ ├── certificates/ # Certificate images
# │ └── images/ # Project and other images
# ├── venv/ # Virtual environment
# └── Procfile # Required for deployment on Heroku


from flask import Flask, render_template, url_for, request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

@app.route ('/contact', methods = ['POST'])
def contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    print(f"Recieved message from {name} ({email}): {message}")

    return jsonify({"success": True, "message": "Message Recieved!"})

if __name__ == '__main__':
    app.run(debug=True)