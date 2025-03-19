# converter for PCD to CSV
# written, used by rathinadevan 

import open3d as o3d
import numpy as np
import pandas as pd

# Load PCD file
pcd = o3d.io.read_point_cloud("drone/data/terrain/CSite1_orig-utm.pcd")

# Convert to NumPy array
points = np.asarray(pcd.points)

# Save as CSV using NumPy
np.savetxt("output.csv", points, delimiter=",", header="x,y,z", comments='')

# Alternatively, using Pandas for better formatting
df = pd.DataFrame(points, columns=["x", "y", "z"])
df.to_csv("output.csv", index=False)

print("PCD converted to CSV successfully!")
