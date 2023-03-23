# gather x,y coordinates for (with pyautogui) the entire run (after 30 seconds of starting or after finding a match for a game start flag)
# write it all down with pandas
# generate heatmap with seaborn sns.kdeplot

from logger import CSVLogger
import time

logger = CSVLogger()
# buffer to give the user enough time to start the game
time.sleep(5)
logger.startLogger()

while True:
    try:
        logger.logCoordinates()
    except KeyboardInterrupt:
        break
