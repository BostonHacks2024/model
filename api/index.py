from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from api.urls import image_urls
from api.smoke_dispersion import simulate_smoke_dispersion
from api.Location import Location
from api.run_model import predict_img
import random 

# aa
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return jsonify({"message": "Server is running..."})
  

@app.route('/simulate', methods=['POST'])
@cross_origin()
def simulate():
    try:
        data = request.get_json()
        x0 = data.get('latitude')
        y0 = data.get('longitude')
        radius = data.get('radius', 3)
        delta = data.get('separation', 0.2)

       


        if x0 is None or y0 is None:
            return jsonify({'error': 'Missing latitude or longitude'}), 400

        source = Location(x0, y0)
        
        grid = simulate_smoke_dispersion(source, radius, delta)

        wildfire_images = []
        for index, image in enumerate(random.sample(image_urls, 6)):
            if predict_img(image) == "Wildfire" and index < len(grid):
                wildfire_images.append((image, grid[index][0].x, grid[index][0].y))
        
        result = [{"chunk": index + 1, 'latitude': element[0].x, 'longitude': element[0].y, "dispersion": element[1]} for index, element in enumerate(grid)]
        
        response = {"data": result}

        # comment
        return jsonify(response)
       
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
