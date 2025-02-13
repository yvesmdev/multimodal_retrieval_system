from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
#from flask import current_app as app
from flask.json import JSONEncoder
import decimal
import os
import pandas as pd
import random

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.abspath(os.path.join(os.getcwd(), "../../sample_images"))
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

#modifing JSON Encoder
class JsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return JSONEncoder.default(self, obj)


@app.route('/api/mmsys/query', methods=['GET'])
def fect_test_response():
    desc = request.args.get('desc') #get query description    return 'flask_api ok'
    k = int(request.args.get('k')) #kumber of retrievals
    print("K:",k)
    message = desc.upper()

    img_df = pd.read_csv('../../sample_images/sample_images.csv')
    Ns = len(img_df)
    sample_ids = random.sample(range(0,Ns-1),k)
    sample_df = img_df.iloc[sample_ids,:]#get sample image subset

    image_list = sample_df.file_name.tolist()
    available_images = os.listdir(app.config["UPLOAD_FOLDER"])#read all available images
    filtered_images = [img for img in available_images if img in image_list]
    #generate url for filter images
    image_urls = [f"http://127.0.0.1:5002/api/image/{img}" for img in filtered_images]
    
    response_list = []
    for i in range(len(image_urls)):
        img = {'img_url':image_urls[i], 'score':round(random.uniform(0,1),3)}
        response_list.append(img)

    #print(response_list)
    return jsonify(response_list)

@app.route("/api/image/<filename>")
def serve_image(filename):
    """
    Serves an image from the uploads folder only if it is in ALLOWED_IMAGES.
    """
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)



