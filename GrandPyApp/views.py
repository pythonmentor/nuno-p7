from flask import Flask, render_template, request, jsonify
from .process import grandPyWork


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html")


@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        input_value = request.data.decode("utf-8")
        return jsonify({"phrase_user": grandPyWork(input_value, app)})


if __name__ == "__main__":
    app.run(debug=True)
