import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree

# Load and clean point cloud
pcd = o3d.io.read_point_cloud("terrain/samp52-utm-ground.pcd")
pcd = pcd.voxel_down_sample(voxel_size=0.05)  # Increased voxel size for better coverage
pcd, _ = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

# Segment ground points
plane_model, inliers = pcd.segment_plane(distance_threshold=0.1, ransac_n=3, num_iterations=3000)
ground_pcd = pcd.select_by_index(inliers)
non_ground_pcd = pcd.select_by_index(inliers, invert=True)

# Convert ground points to NumPy array
ground_points = np.asarray(ground_pcd.points)
x_coords, y_coords = ground_points[:, 0], ground_points[:, 1]

# Define grid resolution (30 cm per cell)
grid_size = 0.3  # Adjusted for better detection
min_x, max_x = np.min(x_coords), np.max(x_coords)
min_y, max_y = np.min(y_coords), np.max(y_coords)

# Create grid
grid_x = np.arange(min_x, max_x, grid_size)
grid_y = np.arange(min_y, max_y, grid_size)
grid = np.zeros((len(grid_x), len(grid_y)))

# KDTree for fast lookup
tree = KDTree(np.column_stack((x_coords, y_coords)))

# Fill grid with safe spots
for i, gx in enumerate(grid_x):
    for j, gy in enumerate(grid_y):
        indices = tree.query_ball_point([gx, gy], r=grid_size)  # Larger radius
        if len(indices) > 5:  # More points required to be "safe"
            grid[i, j] = 1  

# Sliding window for 2x2 safe areas (60cm x 60cm)
landing_spots = []
for i in range(len(grid_x) - 1):
    for j in range(len(grid_y) - 1):
        if grid[i, j] == 1 and grid[i+1, j] == 1 and grid[i, j+1] == 1 and grid[i+1, j+1] == 1:
            landing_spots.append((grid_x[i], grid_y[j])) 

# Debug print (check if we found any landing spots)
print(f"Total landing spots found: {len(landing_spots)}")

# Plot grid
plt.imshow(grid.T, origin='lower', cmap='Greens', extent=[min_x, max_x, min_y, max_y])
plt.colorbar(label="Safe (1) / Unsafe (0)")

# Plot landing zones
for (x, y) in landing_spots:
    plt.scatter(x, y, color='blue', marker='o', s=100)

plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Safe Landing Zones (Green) with 60x60cm Areas (Blue)")
plt.show()
