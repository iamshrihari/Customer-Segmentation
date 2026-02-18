import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def apply_kmeans(rfm, n_clusters=4):
    features = rfm[["Recency", "Frequency", "Monetary"]]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    rfm["Cluster"] = kmeans.fit_predict(scaled_features)

    print("✅ KMeans clustering applied successfully!")
    return rfm


def label_clusters(rfm):
    cluster_summary = rfm.groupby("Cluster")[["Recency", "Frequency", "Monetary"]].mean()

    labels = {}

    # Sort clusters by Monetary (highest spenders = VIP)
    sorted_clusters = cluster_summary.sort_values("Monetary", ascending=False).index.tolist()

    if len(sorted_clusters) >= 4:
        labels[sorted_clusters[0]] = "VIP Customers"
        labels[sorted_clusters[1]] = "Loyal Customers"
        labels[sorted_clusters[2]] = "Regular Customers"
        labels[sorted_clusters[3]] = "At Risk Customers"
    else:
        for c in sorted_clusters:
            labels[c] = f"Segment {c}"

    rfm["Segment"] = rfm["Cluster"].map(labels)

    print("✅ Clusters labeled into business segments!")
    return rfm
