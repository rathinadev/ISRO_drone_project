import open3d as o3d

# Read the PCD file directly
pcd = o3d.io.read_point_cloud("drone/data/terrain/CSite1_orig-utm.pcd")

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])
