
# Flask API for Image Retrieval System

## Overview

This Flask API powers the **AI-powered Image Retrieval System**, allowing users to retrieve images based on natural language descriptions. The backend processes user queries, matches them with relevant images using **NLP techniques (TF-IDF, BERT, etc.)**, and returns the best-matching results.

---

## **Technology Stack**
- **Framework:** Flask (Python)
- **NLP Techniques:** TF-IDF with Cosine Similarity, BERT-based embeddings
- **Computer Vision:** GPT2 Image Captioning Models for annotation

---

## **Installation & Setup**

### **Prerequisites**
Ensure you have the following installed:
- **Python 3.x**
- **pip** (Python package manager)
- **Virtual environment (optional but recommended)**

### **1. Clone the Repository**
```sh
git clone https://github.com/yvesmdev/multimodal_retrieval_system.git
cd multimodal_retrieval_system/web-back-end/flask
```

### **2. Running Flask**
```sh
python api/main.py
