# todo.Try this narx network: http://nullege.com/codes/search/pyneurgen.recurrent.NARXRecurrent
# todo.Official documentation for this: http://pyneurgen.sourceforge.net/api/recurrent_api.html#NARXRecurrent

import neurolab as nl
import numpy as np

# Create train samples

Prodovolstvennye_tovary_i_syre_dlja_ih_proizvodstva = [1824.36776, 1824.36776, 1824.36776, 1824.36776, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427, 1964.54427]

usd = [68.43460, 67.78070, 68.75490, 67.60760, 67.85520, 67.14100, 67.14100, 67.14100, 68.67530, 68.89010, 68.52150, 67.79600, 67.46620, 67.46620, 67.46620, 67.12500, 66.34560, 65.76620, 66.49540, 66.04520, 66.04520, 66.04520, 68.27240, 65.64740, 66.03640, 65.02540, 66.21980, 66.21980, 66.21980, 66.62950, 66.45590, 65.16180, 65.11330, 64.33340]
euro = [76.40040, 75.69750, 76.86110, 76.53860, 76.92070, 76.42660, 76.42660, 76.42660, 78.16620, 78.27980, 77.81300, 77.36880, 76.68880, 76.68880, 76.68880, 76.49570, 75.85290, 74.65780, 74.79400, 74.34050, 74.34050, 74.34050, 77.12730, 74.37190, 75.01070, 73.45920, 74.69590, 74.69590, 74.69590, 74.95150, 74.90240, 73.80230, 73.91660, 73.30150]
GDP_bln = [18027.59435, 18027.59435, 18027.59435, 18027.59435, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841, 17847.31841]
inflation = [0.46000, 0.46000, 0.46000, 0.46000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000, 0.44000]
polarity = [0.50247, 0.73083, 0.37046, 1.50028, 1.50028, 1.51409, 0.29517, 0.26568, 0.53846, 1.47701, 0.50898, 1.50898, 1.68444, 1.61913, 1.36386, 2.41493, 0.96846, 1.84761, 0.28239, -0.05523, 1.02625, 0.92479, 1.78421, 0.39273, 1.07146, 1.20649, 1.20649, 1.40350, 1.84777, 0.35050, 0.42621, 1.48681, 0.19668, 0.14155]

usd_sample = [65.81688571]
euro_sample = [75.133]
GDP_bln_sample = [17490.3720418]
inflation_sample = [0.42]
polarity_sample = [0.60129]

Prodovolstvennye_tovary_i_syre_dlja_ih_proizvodstva = np.asarray(Prodovolstvennye_tovary_i_syre_dlja_ih_proizvodstva)
usd = np.asarray(usd)
euro = np.asarray(euro)
GDP_bln = np.asarray(GDP_bln)
inflation = np.asarray(inflation)
polarity = np.asarray(polarity)

usd_sample = np.asarray(usd_sample)
euro_sample = np.asarray(euro_sample)
GDP_bln_sample = np.asarray(GDP_bln_sample)
inflation_sample = np.asarray(inflation_sample)
polarity_sample = np.asarray(polarity_sample)

size = len(Prodovolstvennye_tovary_i_syre_dlja_ih_proizvodstva)

inp = np.vstack((usd, euro, GDP_bln, inflation, polarity)).T
tar = Prodovolstvennye_tovary_i_syre_dlja_ih_proizvodstva.reshape(size, 1)
smp = np.vstack((usd_sample, euro_sample, GDP_bln_sample, inflation_sample, polarity_sample)).T

# Create network with 2 layers and random initialized
net = nl.net.newelm(
        [[min(inp[:, 0]), max(inp[:, 0])],
         [min(inp[:, 1]), max(inp[:, 1])],
         [min(inp[:, 2]), max(inp[:, 2])],
         [min(inp[:, 3]), max(inp[:, 3])],
         [min(inp[:, 4]), max(inp[:, 4])],
         ],
        [16, 1],
        [nl.trans.TanSig(), nl.trans.PureLin()]
                )
# Set initialized functions and init
net.layers[0].initf = nl.init.InitRand([-0.1, 0.1], 'wb')
net.layers[1].initf = nl.init.InitRand([-0.1, 0.1], 'wb')
net.init()
# Train network
error = net.train(inp, tar, epochs=1500, show=100, goal=0.02)

# Simulate network
out = net.sim(smp)
print(out)