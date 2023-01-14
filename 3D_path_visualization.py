import os
from mayavi import mlab
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.cm as cm
path = '/Users/your directory/bar/'

# read all csv files, this can draw morw than one csv file, 
dfs = []
for file in os.listdir(path):
    if file.endswith('.csv'):
        df = pd.read_csv(path+file)
        dfs.append(df)
# concatenate all dataframes and select specific columns, if you like to have several animal path
df = pd.concat(dfs)
df2 = df[['X', 'Y', 'Frame']]
# make a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#create a different color for earch subzone in the cube
location_mapping = {'c1': 1,'c2': 2, 'c3': 3, 'c4': 4, 'b1': 5, 'b2': 6, 'b3': 7, 'b4':8, 'center': 9,
                    'b1_center': 4, 'b2_center': 4, 'b3_center': 4, 'b4_center': 4, 
                    'c1_b1': 2, 'c1_b4': 2, 'c4_b4': 2, 'c4_b3': 2, 'c3_b3': 2, 'c3_b2': 2, 'c2_b2': 2, 'c2_b1': 2}
# string values to integers with  mapping method
z = df['ROI_location'].map(location_mapping).values
# create a colormap from the integer values
cmap = cm.ScalarMappable(cmap='tab10')
colors = cmap.to_rgba(z)

ax.scatter(df2['X'], df2['Y'], df2['Frame'], c= colors, alpha=0.9, s=z*3, marker='.')
#labels to the axes should be added
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Frame')
plt.savefig('CUBIC_PATH.png', dpi=300)
plt.show()
#z = df['ROI_location'].map(location_mapping).values
for i in range(len(z)):
    mlab.points3d(df2['X'], df2['Y'], df2['Frame'], color=(0.8, 0.5, 0.3), scale_factor=5)
mlab.show()
