import pyautogui as pag
import csv, time
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

    def startLogger(self) -> None:
        self.csvFile = open(f'gazeData_{self.startDateTime}.csv', mode='w', newline='')
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

    def __del__(self) -> None:
        self.csvFile.close()
        