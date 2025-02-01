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

## 📑 **Interim Documentation**  

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
- **Task 3:** Object detection using YOLO  
- **Task 4:** Exposing data via FastAPI  

---

## 🤝 **Contributors**  
- **Amanuel Legesse**  

---
