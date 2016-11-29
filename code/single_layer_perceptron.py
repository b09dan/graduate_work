import neurolab as nl

input = [[0, 0], [0, 1], [1, 0], [1, 1]]
target = [[0], [0], [0], [1]]

# Create net with 2 inputs and 1 neuron
net = nl.net.newp([[0, 1],[0, 1]], 1)

# train with delta rule
# see net.trainf
error = net.train(input, target, epochs=1000, show=10, lr=0.1)

# Plot results



import tkinter

import matplotlib.pyplot as pl
pl.plot(error)
pl.xlabel('Epoch number'+str(error))
pl.ylabel('Train error')
pl.grid()
pl.show()