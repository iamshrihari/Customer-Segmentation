import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(rfm, output_path="output/cluster_plot.png"):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=rfm,
        x="Recency",
        y="Monetary",
        hue="Cluster",
        palette="viridis"
    )
    plt.title("Customer Segmentation (Recency vs Monetary)")
    plt.savefig(output_path)
    plt.close()

    print(f"📊 Cluster plot saved at {output_path}")
