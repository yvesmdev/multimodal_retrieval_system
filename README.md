# AI-Powered Image Retrieval System (First Prototype - In Active Improvement)

## Overview

This project leverages **natural language processing (NLP)** and **image processing** to allow users to search for images using descriptive queries. The system uses **text similarity techniques** and **pre-trained image captioning models** to match user inputs with relevant images.

## Features

- Retrieve images using natural language queries.
- Implements **TF-IDF Cosine Similarity, BERT**, and other NLP techniques.
- Uses **image captioning models** to label and categorize images.
- Supports **real-time search** with efficient retrieval mechanisms.
- Built with **React.js for the front-end** and **Flask API for the back-end**.

---

## **Technology Stack**

### Front-end
- **React.js** – Interactive user interface.

### Back-end
- **Flask (Python)** – API handling requests.

### Data Processing & AI
- **Random Dataset Sampling** – Uses a non-AI-generated image dataset extracted from test_data_v2 (https://www.kaggle.com/datasets/alessandrasala79/ai-vs-human-generated-dataset/data?select=test_data_v2).
- **Image Captioning Models** – Assigns text labels to images using pre-training captioning models.
- **Text Similarity Matching**:
  - TF-IDF with Cosine Similarity
  - BERT-based sentence embeddings
  - Other NLP-based retrieval methods

---

## **Installation & Setup**

### **Prerequisites**
- Python 3.x (Anaconda distribution)
- Node.js & npm
- Flask
- React.js dependencies

### **Clone the Repository**
```sh
git clone https://github.com/yvesmdev/multimodal_retrieval_system.git
cd multimodal_retrieval_system
