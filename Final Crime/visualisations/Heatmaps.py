__author__ = 'navya'


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('../data/train.csv', header=0)
rows = len(data.axes[0])
data = pd.crosstab(data.Category, data.Resolution)

heat_map = sns.heatmap(data, square=True, linewidths=1, label='tiny')
plt.show()
