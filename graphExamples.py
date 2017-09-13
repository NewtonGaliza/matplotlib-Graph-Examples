import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''example1
plt.plot([0,10,20,30])
plt.show()
'''

'''example2
plt.plot([10,20,30,40], [15,40,75,90], linestyle='--',
 color='r', marker='s', linewidth=3.0)
plt.axis([0,50,0,100])
plt.show()
'''

#graph bar
y_axis = [20,50,30]
x_axis = range(len(y_axis))
width_n = 0.4
bar_color = 'red'

plt.bar(x_axis, y_axis, width = width_n, color = bar_color)
plt.show()
