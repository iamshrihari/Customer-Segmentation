# Customer Segmentation using SQL + Python (RFM + KMeans)

## 📌 Project Overview
This project performs customer segmentation using **RFM Analysis** (Recency, Frequency, Monetary) and applies **KMeans Clustering** to group customers into meaningful segments.

Dataset used for this project: https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci?resource=download

This helps businesses identify:
- High value customers
- Loyal customers
- Churn risk customers
- Low engagement customers

---

## 🛠 Tech Stack
- Python (Pandas, NumPy)
- SQL (SQLite)
- Scikit-learn (KMeans)
- Matplotlib / Seaborn

---

## 📂 Folder Structure

Customer-Segmentation/
│── data/
│ └── OnlineRetail.csv
│── sql/
│ └── rfm_queries.sql
│── src/
│── output/
│── main.py
│── requirements.txt
│── README.md

📊 Output

Results are saved inside the output/ folder:

rfm_table.csv → RFM values for each customer

customer_segments.csv → final cluster assignment

cluster_plot.png → visualization of clusters

📌 Key Concepts Used

SQL aggregation queries

RFM Analysis

StandardScaler normalization

KMeans clustering

Data visualization

⭐ Future Improvements

Auto-detect best K using Elbow Method

Build Streamlit dashboard for segmentation

Add cluster naming (VIP, Loyal, Risk, etc.)

👨‍💻 Author

Shrihari
