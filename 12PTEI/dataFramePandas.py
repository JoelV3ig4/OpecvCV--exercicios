import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

height = [3, 12, 5, 18, 45]
bars = ['A, B, C, D, E']
plt.bar(bars, height, color='aquamarine')
plt.xlabel('bars')
plt.ylabel('height')
plt.show()
