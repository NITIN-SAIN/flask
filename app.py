from flask import Flask

app=Flask(__name__)

@app.route("/")

def home():
    return "hello from Flask deployed via jenkins & Docker!"

if__name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

