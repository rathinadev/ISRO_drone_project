import open3d as o3d
import numpy as np

# Load the PCD file (replace with actual path)
pcd = o3d.io.read_point_cloud("terrain/samp52-utm-ground.pcd")

# Downsample point cloud to reduce density and speed up processing
pcd = pcd.voxel_down_sample(voxel_size=0.05)  # Adjust voxel size if needed

# Remove outliers (optional but useful)
pcd, _ = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

# Visualize the cleaned point cloud
#o3d.visualization.draw_geometries([pcd], window_name="Filtered Point Cloud")


# Extract the largest plane (ground)
plane_model, inliers = pcd.segment_plane(distance_threshold=0.1, ransac_n=3, num_iterations=3000)

# Separate ground and non-ground points
ground_pcd = pcd.select_by_index(inliers)
non_ground_pcd = pcd.select_by_index(inliers, invert=True)

# Colorize for visualization
ground_pcd.paint_uniform_color([0, 1, 0])  # Green for ground
non_ground_pcd.paint_uniform_color([1, 0, 0])  # Red for obstacles

# Visualize the ground vs obstacles
o3d.visualization.draw_geometries([ground_pcd, non_ground_pcd], window_name="Ground Segmentation")

