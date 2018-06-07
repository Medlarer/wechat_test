from flask import Flask,render_template

app = Flask(__name__)


@app.route("/index", methods=['GET', 'POST'])
def login():
    return render_template("index.html")


@app.route("/register")
def register():
    return "Please enter information"


if __name__ == '__main__':
    app.run(host="192.168.1.121", port=6000)

