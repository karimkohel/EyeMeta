# gather x,y coordinates for (with pyautogui) the entire run (after 30 seconds of starting or after finding a match for a game start flag)
# write it all down as csv
# read with pandas
# generate heatmap with seaborn sns.kdeplot
# figure out what more statistics do we need

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyautogui as pag

df = pd.read_csv('gazeData_23-03-2023_16.40.csv')
fig, ax = plt.subplots()

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
    cbar=True
)
plt.show()