from flask import Flask

app = Flask(__name__)


app.route("/")
app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    pass