import pyautogui as pag
import csv, time, os
from datetime import datetime


class CSVLogger():
    def __init__(self, sps: int = 2) -> None:
        """Start the logger class to log coordinates in csv file with time stamp

        Parameters:
        -----------
        sps: optional, samples per second will default to 2 per second, the amount of coordinate samples to gather per second
        
        """
        self.startDateTime = datetime.now().strftime("%d-%m-%Y_%H.%M")
        self.fieldNames = ['x', 'y', 'time']
        self.sps = sps

        self.folderName = f'data/data_folder{self.startDateTime}_{pag.size().width}x{pag.size().height}'
        self.filepath = f'{self.folderName}/gazeData_{self.startDateTime}_{pag.size().width}x{pag.size().height}.csv'
        try:
            os.mkdir(self.folderName)
        except FileExistsError:
            pass

        self.csvFile = open(self.filepath, mode='w', newline='')
        self.writer = csv.DictWriter(self.csvFile, fieldnames=self.fieldNames)
        self.writer.writeheader()

    def logCoordinates(self) -> None:
        time.sleep(1/self.sps)
        row = {
            self.fieldNames[0]: pag.position().x,
            self.fieldNames[1]: pag.position().y,
            self.fieldNames[2]: datetime.now().strftime("%H:%M:%S.%f")
        }
        self.writer.writerow(row)

    def closeFile(self) -> None:
        self.csvFile.close()
        

if __name__ == "__main__":
    logger = CSVLogger(5)
    # buffer to give the user enough time to start the game
    time.sleep(1)
    logger.startLogger()

    while True:
        try:
            logger.logCoordinates()
        except KeyboardInterrupt:
            break
