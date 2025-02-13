from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
#from flask import current_app as app
from flask.json import JSONEncoder
import decimal
import os
import pandas as pd

#--model imports
import dill as pickle 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

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
   
    with open('../../analytics/image_recommender_model_vitgpt2_tidf_files.pkl', 'rb') as f:
        system_image_recommender = pickle.load(f)
        tagged_sample_df = pickle.load(f)
        tfidf = pickle.load(f)
        X_matrix = pickle.load(f)
    
    text = desc
    tagger = 'tagging_vitgpt2'
    output_df = system_image_recommender(tagged_sample_df,tagger,tfidf,
                                X_matrix,text,thr_=0.0,top_n=k)


    image_list = output_df.file_name.tolist() #get imagelist
    score_list = output_df.sim.tolist() #get similarity list

    available_images = os.listdir(app.config["UPLOAD_FOLDER"])#read all available images
    filtered_images = [img for img in available_images if img in image_list]
    #generate url for filter images
    image_urls = [f"http://127.0.0.1:5002/api/image/{img}" for img in filtered_images]
    
    response_list = []
    for i in range(len(image_urls)):
        img = {'img_url':image_urls[i], 'score':round(score_list[i],3)}
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



