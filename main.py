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
    
    from classes.logger import CSVLogger
    from classes.heatmap import HeatMapGenerator
    from classes.sequencer import Sequencer
    import time

    logger = CSVLogger(10)
    # buffer to give the user enough time to start the game

    while True:
        try:
            logger.logCoordinates()
        except KeyboardInterrupt:
            logger.closeFile()
            break

    #### To generate heatmap
    mapper = HeatMapGenerator(logger.filepath, 'data/screen.jpg')
    mapper.generateHeatMap()

    # #### To Generate fixation sequences
    # # TODO
    # seq = Sequencer(logger.filepath, 'data/screen.PNG')
    # seq.generate()