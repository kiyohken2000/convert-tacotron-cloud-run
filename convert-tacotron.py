import os
from flask import Flask, request
import pyopenjtalk

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post_response():
    request_dict = request.get_json()
    req_data = str(request_dict['data'])
    romaji = pyopenjtalk.g2p(req_data)

    result = {}
    result['origin'] = req_data
    result['converted'] = romaji
    return result

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
