# coding: utf-8
import matplotlib.pyplot as plt

import numpy as np

import random

import seaborn as sns

import sys


#Rolling the Die and Calculating Die Frequencies


rolls = [ random.randrange(1, 7) for i in range(int(sys.argv[1])) ]

values, frequencies = np.unique(rolls, return_counts = True)

#Creating the Initial Bar Plot

title = f'Rolling a Six-Sided Die {len(rolls):,} Times'

sns.set_style('whitegrid')

axes = sns.barplot(x = values, y = frequencies, palette = 'bright')


#Setting the Window Title and Labeling the x- and y-Axes

axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')


#Finalizing the Bar Plot

axes.set_ylim(top=max(frequencies)*1.10)

for bar, frequencies in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequencies:,}\n{frequencies / len(rolls):.3%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='center', va='bottom')

#Rolling Again and Updating the Bar Plot—Introducing IPython Magics

plt.show()