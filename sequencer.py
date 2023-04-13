import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN, KMeans, OPTICS


class Sequencer():
	def __init__(self, csvFile: str) -> None:
		self.csvFile = csvFile
		self.df = pd.read_csv(self.csvFile)

	def generate(self):

		# Generate example data
		x = self.df['x'].to_list()
		y = self.df['y'].to_list()


		fig, ax = plt.subplots()
		ax.plot(x, y, '-o')

		# add labels and title
		ax.set_xlabel('X-axis')
		ax.set_ylabel('Y-axis')
		ax.set_title('Points on a Graph')

		plt.show()


seq = Sequencer('data/gazeData_13-04-2023_16.02_1920x1080/gazeData_13-04-2023_16.02_1920x1080.csv')
seq.generate()