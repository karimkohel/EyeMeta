# gather x,y coordinates for (with pyautogui) the entire run (after 30 seconds of starting or after finding a match for a game start flag)
# write it all down as csv
# read with pandas
# generate heatmap with seaborn sns.kdeplot
# figure out what more statistics do we need

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gazeData_23-03-2023_16.40.csv')

kde = sns.kdeplot(
    x=df['x'],
    y=df['y'],
    fill=True,
    thresh=0.05,
)
kde.invert_yaxis()
plt.show()