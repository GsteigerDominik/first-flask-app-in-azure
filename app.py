from flask import Flask, request, jsonify
from flask.helpers import send_file

app = Flask(__name__, static_url_path='/', static_folder='web')

@app.route("/")
def indexPage():
     return send_file("web/index.html")  


@app.route("/quersumme")
def sum_even():
    n = request.args.get('n', default=1)

    result = 0

    for digit in n:
        result += int(digit)
    # return result as json
    return jsonify(quersumme=result)