from flask import Flask
from response import Response

app = Flask("thor")


@app.route("/")
def index():
    return Response(data={"service": app.name, "status": "running"}).as_json()


@app.route("/health")
def health():
    return Response(data={"status": "running"}).as_json()
