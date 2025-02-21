#https://www.youtube.com/watch?v=vsjC4dxpS3g
#https://www.youtube.com/watch?v=ncua01HTxis
#https://www.youtube.com/watch?v=fOjuwecPgfY
#pip install pipreqs
#pipreqs /path/to/your/project --force
#sudo rm -r /tmp/*
#scp requirements.txt root@159.223.47.49:ms-server/web-back-end/flask/
#pip install -r requirements.txt 

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
#from flask import current_app as app
from flask.json import JSONEncoder
import decimal
import os
import pandas as pd
#--model imports
import dill as pickle 
from nltk.corpus import stopwords
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity 
#------------------------------------------------------->

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.abspath(os.path.join(os.getcwd(), "../../sample_imagesv2"))
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

import gensim.downloader
# Show all available models in gensim-data
gensim_pretrains = list(gensim.downloader.info()['models'].keys())
word2vec_model = gensim.downloader.load(gensim_pretrains[3]) #load word embedding model

with open('../../analytics/models/image_recommender_model_florence_long_word2vectfidf_files.pkl', 'rb') as f:
        system_image_recommender = pickle.load(f)
        sys_tagged_sample_df = pickle.load(f)
        text_preprocess = pickle.load(f)
        sys_X_emb = pickle.load(f)
        sys_text2emb = pickle.load(f)

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

    text = desc
    tagger = 'florence_long'
    output_df = system_image_recommender(sys_tagged_sample_df,tagger,[],sys_X_emb,text,
                                     sys_text2emb,thr_=0.0,top_n=k)

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

@app.route("/api/test/")
def api_test():
    return "flask ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)



