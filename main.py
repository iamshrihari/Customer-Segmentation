from src.load_to_db import load_csv_to_sqlite
from src.rfm_analysis import generate_rfm_table
from src.clustering import apply_kmeans, label_clusters
from src.visualize import plot_clusters
from src.utils import ensure_dir

def main():
    ensure_dir("output")

    csv_path = "data/OnlineRetail.csv"

    # Step 1: Load data into SQLite
    load_csv_to_sqlite(csv_path)

    # Step 2: Generate RFM Table
    rfm = generate_rfm_table()
    rfm.to_csv("output/rfm_table.csv", index=False)

    # Step 3: Apply KMeans clustering
    segmented = apply_kmeans(rfm, n_clusters=4)

    # Step 4: Add business segment labels
    segmented = label_clusters(segmented)

    # Step 5: Save final customer segments
    segmented.to_csv("output/customer_segments.csv", index=False)

    # Step 6: Plot clusters
    plot_clusters(segmented)

    print("\n🔥 Project Completed Successfully!")
    print("Check output/ folder for results.")

if __name__ == "__main__":
    main()
