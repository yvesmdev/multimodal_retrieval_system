
# Flask API for Image Retrieval System

## Overview

This Flask API powers the **AI-powered Image Retrieval System**, allowing users to retrieve images based on natural language descriptions. The backend processes user queries, matches them with relevant images using **NLP techniques (TF-IDF + Semantic Word Embedding - Cosine Similarity)**, and returns the best-matching results. To save during the installation process you can use the Python environment **flask_venv** which contains all the project <a href="https://github.com/yvesmdev/multimodal_retrieval_system/blob/florence_embedding/web-back-end/flask/requirements.txt" target="_blank">Python dependencies</a>.

---

## **Technology Stack**
- **Framework:** Flask (Python)
- **NLP Techniques:** Hybrid TFIDF - Semantic Word Embedding with Cosine Similarity
- **Computer Vision:** Florence2 Image Captioning Models for annotation

---

## **Installation & Setup**

### **Prerequisites**
Ensure you have the following installed:
- **Python 3.x** + <a href="https://github.com/yvesmdev/multimodal_retrieval_system/blob/florence_embedding/web-back-end/flask/requirements.txt" target="_blank">requirements</a>
- **pip** (Python package manager)
- **Virtual environment (flask_venv)**

### **1. Clone the Repository**
```sh
git clone https://github.com/yvesmdev/multimodal_retrieval_system.git
cd multimodal_retrieval_system/web-back-end/flask
```

### **2. Running Flask**
```sh
python api/main.py
