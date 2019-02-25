import numpy as np  # Linear library dependency

# sigmoid function
def sigmoid_function(x, derivative = False):
    if derivative  == True:
        return x * (1 - x)
    elif derivative == False:
        return 1 / (1 + np.exp(-x))
# input dataset
X = np.array([  [0,0,0, 0, 1, 0, 0, 0, 0, 0],#each row is a training example, and each column (only one) is an output node
                [0,1,1, 0, 0, 1, 1, 0, 0, 0],
                [1,0,1, 1, 0, 0, 1, 1, 1, 0],
                [1,1,1, 0, 0, 1, 1, 1, 1, 0] ])

# output dataset
y = np.array([[1,0, 1,1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed() #fixing a way the numbers are distributed

# initialize weights randomly with mean 0
syn0 = 2* np.random.random((len(X[0]), 1)) - 1

for iter in range(1000):

    # forward propagation
    l0 = X
    l1 = sigmoid_function(np.dot(l0, syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * sigmoid_function(l1, True)

    # update weights
    syn0 += np.dot(l0.T, l1_delta)

print("Output After Training:")
print(l1)

# http://iamtrask.github.io/2015/07/12/basic-python-network/
