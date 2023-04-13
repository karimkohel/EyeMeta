import pandas as pd
import numpy as np
import pyautogui as pag
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Sequencer():
	def __init__(self, csvFile: str,  screenshotFile: str) -> None:
		self.csvFile = csvFile
		self.df = pd.read_csv(self.csvFile)
		self.saveDir = f'{self.csvFile.strip(".csv")}-Sequence.png'
		self.fig, self.ax = plt.subplots()
		self.ax.invert_xaxis()
		self.img = mpimg.imread(screenshotFile)
		self.ax.imshow(self.img, extent=[0, pag.size().width, 0, pag.size().height],)

	def generate(self):

		# Generate example data
		points = self.df[['x', 'y']].to_numpy()
		centers = []
		sampelsPerCenter = 20
		for i in range(0, len(points), sampelsPerCenter):
			if i+sampelsPerCenter >= len(points)-1:
				break

			center = np.mean(points[:i+sampelsPerCenter], axis=0)
			centers.append(center)

		centers = np.array(centers)

		self.plot = self.ax.plot(centers[:, :1], centers[:, 1:2], '-o')
		
		self.ax.set_aspect('equal')
		plt.axis('off')

		plt.savefig(self.saveDir, bbox_inches='tight', dpi=600, pad_inches=0.04)