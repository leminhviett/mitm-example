from flask import Flask, request

app = Flask(__name__)

@app.route("/secret")
def secret():
    secret = request.args.get('secret')
    return "Confirm secret"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")