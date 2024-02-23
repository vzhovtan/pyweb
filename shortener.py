from flask import Flask, request, redirect
from hashlib import sha256

app = Flask(__name__)

urlMap = {}


@app.post("/shorten")
def createShort():
    print("shortening...")
    original = request.json["url"]
    short = f'/s/{(sha256(original.encode('utf-8')).hexdigest())[-10:]}'
    if short not in urlMap:
        urlMap[short] = original
        return short
    else:
        return "ServerError 500"


@app.get("/s/<id>")
def red(id):
    print("redirecting...")
    original = urlMap.get(f'/s/{id}')
    if original:
        return redirect(original)
    else:
        return "Not found"


if __name__ == "__main__":
    app.run(debug=True)