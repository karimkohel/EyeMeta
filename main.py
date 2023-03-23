# gather x,y coordinates for (with pyautogui) the entire run (after 30 seconds of starting or after finding a match for a game start flag)
# write it all down as csv
# read with pandas
# generate heatmap with seaborn sns.kdeplot
# figure out what more statistics do we need

# params to adjust by testing with tracker:
#   - Sample resolution: the amount of samples we get per second in the logger
#   - get the image of gameplay to overlay under heatmap
#   - location of ai tool vs game space to divide the screen


if __name__ == "__main__":
    
    from logger import CSVLogger
    from heatmap import HeatMapGenerator
    import time

    logger = CSVLogger(5)
    # buffer to give the user enough time to start the game
    time.sleep(1)

    while True:
        try:
            logger.logCoordinates()
        except KeyboardInterrupt:
            logger.closeFile()
            break

    mapper = HeatMapGenerator(logger.filepath, 'data/screen.PNG')
    mapper.generateHeatMap()