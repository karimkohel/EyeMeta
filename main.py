# gather x,y coordinates for (with pyautogui) the entire run (after 30 seconds of starting or after finding a match for a game start flag)
# write it all down as csv
# read with pandas
# generate heatmap with seaborn sns.kdeplot
# figure out what more statistics do we need

# params to adjust by testing with tracker:
#   - Sample resolution: the amount of samples we get per second in the logger
#   - get the image of gameplay to overlay under heatmap
#   - location of ai tool vs game space to divide the screen


# if __name__ == "__main__":
    
#     from logger import CSVLogger
#     from heatmap import HeatMapGenerator
#     import time

#     logger = CSVLogger(5)
#     # buffer to give the user enough time to start the game
#     time.sleep(1)

#     while True:
#         try:
#             logger.logCoordinates()
#         except KeyboardInterrupt:
#             logger.closeFile()
#             break

#     mapper = HeatMapGenerator(logger.filepath, 'data/screen.PNG')
#     mapper.generateHeatMap()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Load the data from a CSV file
df = pd.read_csv('data/data_folder29-03-2023_17.11_1920x1080/gazeData_29-03-2023_17.11_1920x1080.csv')

# Specify the minimum distance between points to be considered part of the same cluster
eps = 100

# Specify the minimum number of points required to form a cluster
min_samples = 2

# Apply DBSCAN clustering to group the points into clusters
dbscan = DBSCAN(eps=eps, min_samples=min_samples)
clusters = dbscan.fit_predict(df[['x', 'y']])

# Plot the sequence of clusters with lines between each cluster
fig, ax = plt.subplots(figsize=(8, 6))
for i in np.unique(clusters):
    cluster_points = df.loc[clusters == i, ['x', 'y']].values
    ax.plot(cluster_points[:, 0], cluster_points[:, 1], '-o', label=f'Cluster {i}')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sequence of clusters')
plt.legend()
plt.show()


# ASK FAWZY