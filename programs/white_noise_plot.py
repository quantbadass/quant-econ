"""
Origin: QE by John Stachurski and Thomas J. Sargent
Filename: white_noise_plot.py
Authors: John Stachurski, Thomas J. Sargent
LastModified: 11/08/2013

"""
import scipy, matplotlib, pandas, pylab as pyl, numpy as np
x = np.linspace(0, 20, 1000)
y = np.sin (x)
pyl.plot(x, y)
pyl.title('plot')
pyl.xlim(5, 15)
pyl.ylim(-1.2, 1.2)
pyl.plot(x, y)
pyl.xlabel('This is X')
pyl.ylabel('This is Y')
pyl.legend()
pyl.show()