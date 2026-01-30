rom flask import Flask
app = Flask(__my-app__)

@app.route("/")
def home():
    return "Flask app deployed using GitHub Actions!"

if name == "__main__":
    app.run(host="0.0.0.0", port=5
