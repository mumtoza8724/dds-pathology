from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import send_from_directory
@app.route('/google7836419afd22a9e3.html')
def google_verification():
    return send_from_directory('', 'google7836419afd22a9e3.html')