# gather x,y coordinates for (with pyautogui) the entire run (after 30 seconds of starting or after finding a match for a game start flag)
# write it all down as csv
# read with pandas
# generate heatmap with seaborn sns.kdeplot
# figure out what more statistics do we need

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pyautogui as pag

df = pd.read_csv('data/gazeData_23-03-2023_17.23_1920x1080.csv')
fig, ax = plt.subplots()
img = mpimg.imread('data/screen.PNG')

ax.set_xlim(pag.size().width)
ax.set_ylim(pag.size().height)
ax.invert_xaxis()

kde = sns.kdeplot(
    x=df['x'],
    y=df['y'],
    fill=True,
    thresh=0.05,
    alpha=0.4,
    n_levels=15,
    cmap='magma',
    cbar=True,
    ax=ax
)

plt.imshow(img,
          aspect = kde.get_aspect(),
          extent = kde.get_xlim() + kde.get_ylim(),
          zorder = 0)
plt.show()