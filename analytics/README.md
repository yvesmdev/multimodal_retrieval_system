# Analytics for Text Query Image Recommender Model

## Overview

This folder contains **three key Jupyter notebooks** used to build a **pickle-stored image recommender model**. The process involves **sampling images, tagging images with text captions, and developing a text-image matching model** using **TFIDF features, Semantic WordEmbedding and Cosine Similarity**. The final trained model is serialized into a **pickle file**, used with a Flask Python back-end that services images to a React Front end **(`models/image_recommender_model_florence_long_word2vectfidf_files.pkl`)**.

The analytics can be tested in the following Notebook, <a href="https://github.com/yvesmdev/multimodal_retrieval_system/blob/florence_embedding/analytics/Text2Text_Semantic_Matching_Algorithms-Solution-Test.ipynb" target="_blank"> Click here </a> and the analytics design can be found <a href="https://github.com/yvesmdev/multimodal_retrieval_system/blob/florence_embedding/analytics/Text2Text_Semantic_Matching_Algorithms-FinalModel.ipynb" target="_blank"> here </a>.

---

## **Tasks Performed**

### **1. Image Sampling**
- **Notebook**: `Images_Dataset_Sampling.ipynb`
- **Objective**: Extract **500 images** from a database of test images (https://www.kaggle.com/datasets/alessandrasala79/ai-vs-human-generated-dataset/data?select=test_data_v2)
- **Process**:
  - Randomly select 500 real images for the recommender model.
  - Saves the selected dataset for further processing.

### **2. Image Tagging**
- **Notebook**: `Captioning_Models_based_Image_Tagging_Google_Collab.ipynb`
- **Objective**: Generate **textual descriptions** for the sampled images using the **Florence-2 high accuracy captioning model**  or optionally using a **pretrained GPT-2 low accuracy captioning model.**.
- **Process**:
  - Uses a **Florence-2 high accuracy captioning model** to generate image captions.
  - Cleans and normalizes the captions for improved consistency.
  - Stores image-caption pairs for further analysis.

### **3. Text-Image Matching & Model Training**
- **Notebook**: `Text2Text_Semantic_Matching_Algorithms-FinalModel.ipynb`
- **Test Notebook**: `Text2Text_Semantic_Matching_Algorithms-Solution-Test.ipynb`
- **Objective**: Implement **TF-IDF-Semantic WordEmbedding and Cosine Similarity** for text-based image retrieval and save the model files using **pickle** for export.
- **Process**:
  - Converts image captions into vectorized representations using **TF-IDF-Semantic-WordEmbedding**.
  - Uses **Cosine Similarity** to measure query-image relevance.
  - Trains a **lightweight recommendation model** for real-time query matching.
  - Serializes the trained model as **`models/image_recommender_model_florence_long_word2vectfidf_files.pkl`** for Flask API integration.

---

## **Installation & Setup**
### **1. Install Required Dependencies**
Run the following command to install the required Python packages:
```sh
pip install -r requirements.txt
