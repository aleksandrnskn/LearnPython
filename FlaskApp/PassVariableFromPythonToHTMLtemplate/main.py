from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello-world")
def hello_world():
    return render_template("page-1.html", title="Hello World")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)