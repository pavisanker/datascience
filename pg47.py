import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

dataset = pd.read_csv('data_income.csv')

x = dataset.iloc[:,:].values

kmeans = KMeans(n_clusters=2, init='k-means++', random_state=42, n_init=10)

y_predict = kmeans.fit_predict(x)

centroids = kmeans.cluster_centers_

cluster1_points = []
cluster2_points = []

for i in range(len(y_predict)):
    if y_predict[i] == 0:
        cluster1_points.append(x[i])
    else:
        cluster2_points.append(x[i])

cluster1_points = np.array(cluster1_points)
cluster2_points = np.array(cluster2_points)

print("Cluster 1 Points:")
print(cluster1_points)
print("Centroid for Cluster 1:")
print(centroids[0])

print("\nCluster 2 Points:")
print(cluster2_points)
print("Centroid for Cluster 2:")
print(centroids[1])

