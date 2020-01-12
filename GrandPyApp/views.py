from flask import Flask, render_template, request, jsonify
from .process import grandPyWork


app = Flask(__name__)
app.config.from_object('config')
g_maps_key = app.config["MAPS_API_KEY"]


@app.route('/')
@app.route('/index')
def home():
    return render_template(
            "index.html",
            GOOGLE_API_KEY_MAPS=g_maps_key
        )


@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        input_value = request.form['messageInput']
        print(input_value)
        result = grandPyWork(input_value, app)
        return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
