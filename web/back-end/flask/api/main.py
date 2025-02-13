from flask import Flask, jsonify, request
from flask_cors import CORS
#from flask import current_app as app
from flask.json import JSONEncoder
import decimal


app = Flask(__name__)
CORS(app)



#modifing JSON Encoder
class JsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return JSONEncoder.default(self, obj)


@app.route('/api/mmsys/query', methods=['GET'])
def fect_test_response():
    desc = request.args.get('desc') #get query description    return 'flask_api ok'
    message = desc.upper()
    response_data = {
        "message": message,
    }
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)



