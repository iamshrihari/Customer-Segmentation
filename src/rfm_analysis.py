import sqlite3
import pandas as pd

def generate_rfm_table(db_path="customers.db"):
    conn = sqlite3.connect(db_path)

    query = """
    SELECT 
        CustomerID,
        MAX(InvoiceDate) AS LastPurchaseDate,
        COUNT(DISTINCT InvoiceNo) AS Frequency,
        SUM(Quantity * UnitPrice) AS Monetary
    FROM sales
    WHERE CustomerID IS NOT NULL
    GROUP BY CustomerID;
    """

    rfm = pd.read_sql(query, conn)
    conn.close()

    rfm["LastPurchaseDate"] = pd.to_datetime(rfm["LastPurchaseDate"])

    # Reference date = last purchase date + 1 day
    reference_date = rfm["LastPurchaseDate"].max() + pd.Timedelta(days=1)

    # Recency calculation
    rfm["Recency"] = (reference_date - rfm["LastPurchaseDate"]).dt.days

    # Drop date column
    rfm.drop(columns=["LastPurchaseDate"], inplace=True)

    # Remove invalid customers
    rfm = rfm[(rfm["Monetary"] > 0) & (rfm["Frequency"] > 0)]

    print("✅ RFM Table generated successfully!")
    return rfm
