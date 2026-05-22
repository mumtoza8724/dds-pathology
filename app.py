from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/google7836419afd22a9e3.html')
def google_verification():
    return send_from_directory('.', 'google7836419afd22a9e3.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)