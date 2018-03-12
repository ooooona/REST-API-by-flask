from app import app
from app.data.library import library

@app.route("/", methods=["GET"])
def index():
    return "hello world"

@app.route("/words", methods=["GET"])
def getWords():
    lib = library()
    return lib.get()

@app.route("/words", methods=["POST"])
def postWords():
    pass