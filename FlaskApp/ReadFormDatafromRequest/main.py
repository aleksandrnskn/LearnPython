from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validate-user", methods=["POST"])
def validate_user():
    if request.method == "POST":
        print(request.form)
        print(request.form['userid'])
        print(request.form['password'])
    return 'Hello ' + request.form['userid']

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)