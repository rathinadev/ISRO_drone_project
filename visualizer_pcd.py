import open3d as o3d
import numpy as np

# Load the point cloud directly from your PCD file
pcd = o3d.io.read_point_cloud("drone/data/terrain/CSite1_orig-utm.pcd")

# Create an offscreen renderer (set image size as needed)
width, height = 640, 480
renderer = o3d.visualization.rendering.OffscreenRenderer(width, height)

# Create a scene and add the point cloud geometry
material = o3d.visualization.rendering.MaterialRecord()
material.shader = "defaultUnlit"  # Use an unlit shader for simplicity

renderer.scene.add_geometry("pcd", pcd, material)

# Set up the camera view: specify field of view, look-at point, and up vector.
# Here we set the camera to look at the center of the point cloud.
center = pcd.get_center()
camera = renderer.scene.camera
fov = 60.0  # degrees
eye = [center[0] + 5, center[1] + 5, center[2] + 5]  # A point offset from the center
up = [0, 0, 1]
camera.setup(fov, center, eye, up)

# Render the scene to an image
img = renderer.render_to_image()

# Save the image
o3d.io.write_image("output.png", img)
print("Offscreen rendering complete. Saved to output.png")
