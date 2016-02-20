import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy
from numpy import loadtxt
import sys

class DistributionPlotter:
	def __init__(self, name):
		disArr = loadtxt(name, comments="#", delimiter="\n", unpack=False)
		n, bins, patches = plt.hist(disArr, 20, normed=1, facecolor='green', alpha=0.75)
		sigma = numpy.std(bins)
		mean = sum(bins) / float(len(bins))
		y = mlab.normpdf(bins, mean, sigma)
		l = plt.plot(bins, y, 'r--', linewidth=1)
		plt.show()


a = DistributionPlotter(str(sys.argv[1]))
