from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)


@app.route('/get_locations')
def get_location():
    response = jsonify({
        'locations': util.get_locations()
    })
    response.headers.add('Access control allow origin', '*')
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    data = request.get_json()
    total_sqft = float(data.get('total_sqft', 0))
    location = data.get('location', '')
    bhk = int(data.get('bhk', 0))
    bath = int(data.get('bath', 0))

    response = jsonify({
        'price': util.predict_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access control allow origin', '*')
    return response


if __name__ == '__main__':
    print("Starting python flask Server for Home price prediction")
    app.run(port=5001)
