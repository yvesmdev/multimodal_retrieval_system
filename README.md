# AI-Powered Image Retrieval System (In Active Improvement)

## Overview

This project leverages **natural language processing (NLP)** and **image processing** to allow users to search for images using descriptive queries. Bonus: Extending the system (or providing an architectural design) to show what the system would look like if it catered for disabled people, including blind people.

## **System Architecture**

![system](https://github.com/user-attachments/assets/5794c03c-6d08-45f1-a7e3-0f13ee09d4cb)

## **System Preview**

<img width="1380" alt="Screenshot 2025-02-21 at 15 35 45" src="https://github.com/user-attachments/assets/63a5028e-380a-4b16-aa65-8e543c6f3c64" />


## **Technology Stack**

### Front-end
- **React.js** – Interactive user interface.

### Back-end
- **Flask (Python)** – API handling requests.

### Data Processing & AI
- **Random Dataset Sampling** – Uses a 500 image dataset sample extracted from test_data_v2 (https://www.kaggle.com/datasets/alessandrasala79/ai-vs-human-generated-dataset/data?select=test_data_v2).
- **Image Captioning Models** – Assigns text labels to images using **Florence2 pre-training captioning** model.
- **Text Similarity Matching**:
  - TF-IDF with Cosine Similarity
  - Word embedding and BERT-based sentence embeddings
  - Final Matching Algorithm: **Hybrid TF-IDF-Word2Vec Embedding**

---

## **Installation & Setup**

### **Prerequisites**
- Python 3.x + requirements.txt
- Node.js & npm
- Flask
- React.js dependencies
  
## Analytics Test
Click on the following <a href="https://github.com/yvesmdev/multimodal_retrieval_system/tree/florence_embedding/analytics" target="_blank"> README file</a>

## Backend Setup
Click on the following <a href="https://github.com/yvesmdev/multimodal_retrieval_system/tree/florence_embedding/web-back-end" target="_blank"> README file</a>

## Frontend Setup
Click on the following <a href="https://github.com/yvesmdev/multimodal_retrieval_system/tree/florence_embedding/web-front-end" target="_blank"> README file</a>

### **Clone the Repository**
```sh
git clone https://github.com/yvesmdev/multimodal_retrieval_system.git
**default_branch: florence_embedding**
cd multimodal_retrieval_system
