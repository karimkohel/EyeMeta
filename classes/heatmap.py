import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pyautogui as pag


class HeatMapGenerator():
    
    def __init__(self, csvFile: str, screenshotFile: str) -> None:

        self.csvFile = csvFile
        self.saveDir = f'{self.csvFile.strip(".csv")}-Heatmap.png'
        self.df = pd.read_csv(csvFile)
        self.fig, self.ax = plt.subplots()
        self.img = mpimg.imread(screenshotFile)

        self.ax.set_xlim(pag.size().width)
        self.ax.set_ylim(pag.size().height)
        self.ax.invert_xaxis()

    def generateHeatMap(self):
        self.kde = sns.kdeplot(
            x=self.df['x'],
            y=self.df['y'],
            fill=True,
            thresh=0.05,
            alpha=0.7,
            n_levels=25,
            cmap='magma',
            # cbar=True,
            ax=self.ax
        )
        self.ax.set_aspect('equal')
        plt.axis('off')
        plt.imshow(self.img,
                aspect = self.kde.get_aspect(),
                extent = self.kde.get_xlim() + self.kde.get_ylim(),
                zorder = 0)

        plt.savefig(self.saveDir, bbox_inches='tight', dpi=600, pad_inches=0.04)

if __name__ == "__main__":
    generator = HeatMapGenerator('data/filename.csv', 'data/screen.PNG')
    generator.generateHeatMap()