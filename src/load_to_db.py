import sqlite3
import pandas as pd

def load_csv_to_sqlite(csv_path, db_path="customers.db"):
    df = pd.read_csv(csv_path, encoding="ISO-8859-1")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Rename columns to match our SQL query
    df.rename(columns={
        "Customer ID": "CustomerID",
        "Invoice": "InvoiceNo",
        "Price": "UnitPrice"
    }, inplace=True)

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    conn = sqlite3.connect(db_path)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()

    print("✅ Data loaded into SQLite database successfully!")
