# AI-Powered Image Retrieval System (First Prototype - In Active Improvement)

## Overview

This project leverages **natural language processing (NLP)** and **image processing** to allow users to search for images using descriptive queries. Bonus: Extending the system (or providing an architectural design) to show what the system would look like if it catered for disabled people, including blind people.

## **System Preview**

<img width="1419" alt="design screenshot" src="https://github.com/user-attachments/assets/ed368971-95bd-4fb3-859e-89566c04315e" />

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
  - Word embedding and BERT-based sentence embeddings (To be tested)

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
