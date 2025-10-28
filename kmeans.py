import numpy as np
import matplotlib.pyplot as plt

#  Step 1: Data points
X = np.array([[1,1], [2,1], [4,3], [5,4]])

# Step 2: Choose initial centroids (from data)
centroids = np.array([[1,1], [2,1]])  # k = 2

# Step 3: Define helper functions
def get_clusters(X, centroids):
    # Find distance from each point to each centroid
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    # Assign each point to the nearest centroid
    return np.argmin(distances, axis=1)

def get_new_centroids(X, labels, k):
    # Find new centroid as mean of all points in each cluster
    return np.array([X[labels == i].mean(axis=0) for i in range(k)])

#  Step 4: Run K-Means
for i in range(10):  # max 10 iterations
    labels = get_clusters(X, centroids)
    new_centroids = get_new_centroids(X, labels, len(centroids))
    
    # Plot the clusters
    colors = ['r', 'g']
    plt.scatter(X[labels == 0, 0], X[labels == 0, 1], color='r', label='Cluster 1')
    plt.scatter(X[labels == 1, 0], X[labels == 1, 1], color='g', label='Cluster 2')
    plt.scatter(new_centroids[:, 0], new_centroids[:, 1], color='black', marker='X', s=200, label='Centroids')
    plt.title(f'Iteration {i+1}')
    plt.legend()
    plt.show()
    
    print(f"Iteration {i+1}:")
    print("Cluster assignments:", labels)
    print("Centroids:\n", new_centroids, "\n")
    
    # Stop if centroids don’t move
    if np.allclose(centroids, new_centroids):
        break
    centroids = new_centroids

#  Final output
print("✅ Final Centroids:\n", centroids)
