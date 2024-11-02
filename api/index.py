from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from api.smoke_dispersion import simulate_smoke_dispersion
from api.Location import Location

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def simulate():
    return jsonify({"Server is running..."})
  

@app.route('/simulate', methods=['POST'])
@cross_origin()
def simulate():
    try:
        data = request.get_json()
        x0 = data.get('latitude')
        y0 = data.get('longitude')
        
        if x0 is None or y0 is None:
            return jsonify({'error': 'Missing latitude or longitude'}), 400

        source = Location(x0, y0)
        
        grid = simulate_smoke_dispersion(source)
        
        result = [{"chunk": index + 1, 'latitude': element[0].x, 'longitude': element[0].y, "dispersion": element[1]} for index, element in enumerate(grid)]
        
        return jsonify({'data': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

app = app
