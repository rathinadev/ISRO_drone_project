import open3d as o3d
import numpy as np


# Load PCD file
pcd = o3d.io.read_point_cloud("/drone/data/terrain/CSite1_orig-utm.pcd")

# Convert to numpy array
points = np.asarray(pcd.points)
print(points[:15])  # Print first 5 points

# Visualize
o3d.visualization.draw_geometries([pcd])
