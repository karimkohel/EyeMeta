# gather x,y coordinates for (with pyautogui) the entire run (after 30 seconds of starting or after finding a match for a game start flag)
# write it all down with pandas
# generate heatmap with seaborn sns.kdeplot


import pyautogui as pag
import csv, time
from datetime import datetime

startDateTime = datetime.now().strftime("%d-%m-%Y_%H.%M")
fieldNames = ['x', 'y', 'time']

# buffer to give the user enough time to start the game
time.sleep(5)

csvFile = open(f'gazeData_{startDateTime}.csv', mode='w', newline='')
writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
writer.writeheader()

while True:
    try:
        time.sleep(0.5)
        row = {
            fieldNames[0]: pag.position().x,
            fieldNames[1]: pag.position().y,
            fieldNames[2]: datetime.now().strftime("%H:%M:%S"),
        }
        writer.writerow(row)
    except KeyboardInterrupt:
        break

csvFile.close()