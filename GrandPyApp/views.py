from flask import Flask, render_template, request, jsonify
from .process import grandPyWork


app = Flask(__name__)
app.config.from_object('config')
g_maps_key = app.config['API_PASS_FRONT']


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
        all_inputs_session = []
        if input_value not in all_inputs_session:
            all_inputs_session.append(input_value)
            result = grandPyWork(input_value, app)
            return jsonify(result)
        else:
            message = {
                "messages": [
                    "He garçon, tu m'a dejà demande celà..." +
                    " paresseux vas voir plus haut dans la conversation",
                    "Tu croyais que je dormait non?",
                    "T'as pas honte? Alors quelle adresse ou lieu" +
                    " veux-tu découvrir?"
                ]}
            return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
