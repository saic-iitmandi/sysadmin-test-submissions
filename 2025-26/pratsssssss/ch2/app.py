from flask import Flask
import logging
import sys

app = Flask(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

@app.route("/")
def index():
    app.logger.info("OK request")
    return "Hello\n"

@app.route("/error")
def error():
    app.logger.critical("Critical issue")
    return "Critical logged\n", 500

@app.route("/crash")
def crash():
    app.logger.error("Intentional crash")
    raise Exception("Simulated crash")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
