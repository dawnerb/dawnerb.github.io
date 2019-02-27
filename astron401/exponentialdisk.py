import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fontsize = 12
plt.rc('font',**{'family':'sans-serif','serif':['Arial']})
plt.rc('xtick',labelsize=fontsize)
plt.rc('ytick',labelsize=fontsize)

# make and plot a 2D exponential disk
# i.e. a disk galaxy seen face-on
# 2D exponential disk profile, symmetric in x and y
# all units are arbitrary

a = 5 # central surface brightness (flux per pixel)
h = 10 # scale length
b = 0 # background level

rms = 0.1 # standard deviation of gaussian noise added to image

# define 2d exponential profile
def expdisk(xygrid, a, h, b):
        x, y = xygrid
        return a * np.exp(-np.sqrt(x**2 + y**2) / h) + b

x, y = np.mgrid[-50:50,-50:50]
xygrid = (x,y)
z = expdisk(xygrid,a,h,b)

# add gaussian noise
zn = z + np.random.normal(0,rms,(100,100))

plt.figure(num=1)
# clear figure window
plt.clf()

# plot disk
p = plt.pcolor(x, y, zn, cmap='Greys')
# set range of plot to range of data
plt.axis([x.min(), x.max(), y.min(), y.max()])

# label axes
plt.xlabel('x',fontsize=fontsize)
plt.ylabel('y',fontsize=fontsize)
# make colorbar
cb = plt.colorbar(p)
cb.set_label('Flux per pixel', size=fontsize, labelpad=10)

plt.tight_layout()
plt.show()

# save to PDF file
plt.savefig('exponentialdisk.pdf')
