# Analytics for Text Query Image Recommender Model

## Overview

This folder contains **three Jupyter notebooks** used to build a **pickle-based image recommender model**. The process involves **sampling real images, tagging them with captions, and developing a text-image matching model** using **TF-IDF/WordEmbedding/BERT and Cosine Similarity**. The final trained model is serialized into a **pickle file (`image_recommender_model_vitgpt2_tidf_files.pkl`)**, which will be used by the Flask API for image retrieval.

---

## **Tasks Performed**

### **1. Image Sampling**
- **Notebook**: `NonAI_Images_Dataset_Sampling.ipynb`
- **Objective**: Extract **500 real images** from a database containing a mix of **AI-generated and real images**.
- **Process**:
  - Analyzes metadata to distinguish real vs AI-generated images.
  - Randomly select 500 real images for the recommender model.
  - Saves the selected dataset for further processing.

### **2. Image Tagging**
- **Notebook**: `Captioning_ModelsBased_Image_Tagging.ipynb`
- **Objective**: Generate **textual descriptions** for the sampled images using the **GPT-2 captioning model**.
- **Process**:
  - Uses a **pre-trained GPT-2 model** to generate image captions.
  - Cleans and normalizes the captions for improved consistency.
  - Stores image-caption pairs for further analysis.

### **3. Text-Image Matching & Model Training**
- **Notebook**: `Text2Text_Semantic_Matching_Algorithms.ipynb`
- **Objective**: Implement **TF-IDF/WordEmbedding/BERT and Cosine Similarity** for text-based image retrieval and save a **pickle model**.
- **Process**:
  - Converts image captions into vectorized representations using **TF-IDF/WordEmbedding/BERT**.
  - Uses **Cosine Similarity** to measure query-image relevance.
  - Trains a **lightweight recommendation model** for real-time query matching.
  - Serializes the trained model as **`image_recommender_model_vitgpt2_tidf_files`** for Flask API integration.

---

## **Installation & Setup**
### **1. Install Required Dependencies**
Run the following command to install the required Python packages:
```sh
pip install -r requirements.txt
