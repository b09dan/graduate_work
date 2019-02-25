import neurolab as nl
import numpy as np

# Create train samples
x = np.linspace(-7, 7, 50)
y = np.sin(x) * 0.5

inp = x.reshape(len(x),1)
tar = y.reshape(len(x),1)
# Create network with 2 layers and random initialized
net = nl.net.newff([[min(x), max(x)]],[4, 1])

# Train network
error = net.train(inp, tar, epochs=1000, show=100, goal=0.01)

# Simulate network
out = net.sim(inp)
out_4_plot = out.reshape(len(x))
# Plot result
import pylab as pl

size = len(x)
abscissa_4_ideal_output = np.linspace(-7,7,150)
ordinate_4_ideal_output = np.sin(abscissa_4_ideal_output) * 0.5


pl.plot(abscissa_4_ideal_output, ordinate_4_ideal_output, '-',x , out_4_plot, '->r')
pl.legend(['train target', 'net output'])
pl.show()