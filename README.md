# 🏥 Ethiopian Medical Business Data Warehouse  

## 📖 Project Overview  
This project builds a **data warehouse** to store data scraped from Ethiopian medical business Telegram channels. It involves:  
- **Task 1:** Scraping data from Telegram  
- **Task 2:** Cleaning and transforming the data  
- **Task 3:** Object detection using YOLO  
- **Task 4:** Exposing data via FastAPI  

---

## 📂 **Project Structure**  

```plaintext
medical_data_project/
│── data/                    
│   ├── raw_data.json        # Scraped Telegram messages (Task 1 output)
│   ├── cleaned_data.csv     # Processed & cleaned data
│   ├── medical_business.db  # SQLite database
│
│── images/                  # Stores images from Telegram
│
│── dbt_project/             
│   ├── models/
│   │   ├── cleaned_data.sql # SQL transformations
│   ├── dbt_project.yml      # DBT config
│
│── scripts/                 
│   ├── telegram_scraper.py  # Scrapes Telegram data (Task 1)
│   ├── clean_data.py        # Cleans raw data (Task 2)
│   ├── store_data.py        # Stores cleaned data in SQLite (Task 2)
│   ├── run_dbt.py           # Runs DBT transformations (Task 2)
│
│── requirements.txt         # Dependencies
│── README.md                # Documentation
```

---

## 🔥 **Task 1: Data Scraping from Telegram**  
This script scrapes data from Telegram channels using the **Telethon** library.  

### 📜 **How to Run the Scraper**
```bash
python scripts/telegram_scraper.py
```
- The output is stored in `data/raw_data.json`.

---

## 🧹 **Task 2: Data Cleaning & Transformation**  
This task cleans and stores scraped data in an SQLite database.  

### ✅ **Steps**
1️⃣ **Clean Data**
```bash
python scripts/clean_data.py
```
- Removes duplicates, handles missing values, and standardizes formats.  
- Saves cleaned data to `data/cleaned_data.csv`.  

2️⃣ **Store Data in SQLite**
```bash
python scripts/store_data.py
```
- Saves the cleaned data in `data/medical_business.db`.  

3️⃣ **Run DBT Transformations**
```bash
python scripts/run_dbt.py
```
- Runs SQL transformations using **DBT**.

---

## 📦 **Installation**  

### 🛠 **Step 1: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 🛠 **Step 2: Setup DBT**  
```bash
pip install dbt
dbt init dbt_project
```

---


### 📌 **Contributions and Implementation**  

1. **Data Scraping (Task 1)**  
   - Developed a script using **Telethon** to extract messages from Ethiopian medical business Telegram channels.  
   - Stored raw data in `raw_data.json`.  
   - Implemented logging to monitor the scraping process.  

2. **Data Cleaning and Transformation (Task 2)**  
   - Removed duplicates and missing values using **Pandas**.  
   - Standardized date formats and text structure.  
   - Saved cleaned data in `cleaned_data.csv`.  
   - Loaded structured data into an **SQLite** database (`medical_business.db`).  
   - Designed **DBT SQL models** to transform and prepare data for analysis.  

### 🔹 **Challenges and Solutions**  
✅ **Handling empty/missing JSON files** → Implemented checks to prevent crashes.  
✅ **Data inconsistencies** → Used Pandas to clean and validate data before storing it.  
✅ **Performance optimization** → Used SQLite for structured storage, enabling faster queries.  

---

## 🚀 **Next Steps**  
Task 3: Object Detection Using YOLO
Approach
We used YOLOv5 to detect objects in medical-related images (e.g., medical supplies, equipment, etc.).
Implementation
📌 Step 1: Install Dependencies
pip install torch torchvision opencv-python

📌 Step 2: Clone and Set Up YOLOv5
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt

📌 Step 3: Run Object Detection on Images
import torch
from PIL import Image
from yolov5 import detect

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load image
img = Image.open("medical_image.jpg")

# Detect objects
results = model(img)
results.show()

📌 Step 4: Store Detection Results in Database
 We saved detected object bounding box coordinates, confidence scores, and class labels in a database for further analysis.

Task 4: Exposing Data via FastAPI
Approach
We developed a REST API using FastAPI to expose the collected and processed data.
Implementation
📌 Step 1: Install FastAPI
pip install fastapi uvicorn

📌 Step 2: Create API Endpoints (main.py)
from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/medical-data")
def get_medical_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medical_data")
    data = cursor.fetchall()
    conn.close()
    return {"data": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

📌 Step 3: Run the API
uvicorn main:app --reload
 

---

## 🤝 **Contributors**  
- **Amanuel Legesse**  

---
