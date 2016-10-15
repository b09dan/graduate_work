# todo.Try this narx network: http://nullege.com/codes/search/pyneurgen.recurrent.NARXRecurrent
# todo.Official documentation for this: http://pyneurgen.sourceforge.net/api/recurrent_api.html#NARXRecurrent

import neurolab as nl
import numpy as np

# Create train samples
MICEX = [42.108, 45.544, 43.03, 48.4, 51.517, 46.885, 48.473, 51.471, 55.172, 59.109, 64.464, 56.178, 53.54, 53.484, 50.281, 54.928, 61.103, 63.297, 57.076, 55.222, 57.574, 63.538, 59.804, 59.388, 60.389, 63.998, 70.065, 78.428, 89.25, 84.252, 94.455, 101.1, 117.144, 132.083, 129.919, 148.685, 128.15, 133.139, 138.024, 144.872, 136.724, 142.683, 155.071, 169.347, 165.697, 165.519, 169.808, 169.728, 157.034, 166.596, 173.442, 167.702, 175.944, 187.473, 185.064, 188.886, 157.433, 166.042, 162.843, 166.735, 192.524, 175.367, 149.533, 134.892, 102.766, 73.196, 61.132, 61.953, 62.49, 66.605, 77.293, 92.035, 112.338, 97.155, 105.33, 109.198, 119.72, 123.718, 128.495, 137.001, 141.942, 133.264, 145.015, 143.604, 133.262, 130.931, 139.712, 136.89, 144.03, 152.339, 156.552, 168.799, 172.342, 177.784, 181.359, 174.184, 166.63, 166.659, 170.518, 154.605, 136.654, 149.86, 149.962, 140.202, 151.091, 159.432, 151.829, 147.414, 131.224, 138.689, 140.636, 142.238, 145.901, 142.346, 140.519, 147.787, 154.718, 148.746, 144.002, 138.669, 134.399, 133.124, 137.76, 136.454, 146.313, 150.962, 147.935, 150.339, 145.405, 144.471, 136.929, 130.601, 143.203, 147.638, 137.961, 140.071, 141.107, 148.847, 153.368, 139.661, 164.769]

Brent =[26.8, 28.16, 28.59, 30.05, 28.34, 27.94, 28.76, 30.48, 29.51, 33.01, 32.36, 35.12, 36.98, 33.51, 41.6, 39.33, 47.08, 48.78, 44.03, 40.24, 45.87, 50.14, 53.05, 49.33, 49.83, 54.85, 59.7, 66.68, 62.56, 58.35, 53.41, 58.87, 65.43, 60.05, 64.94, 72, 69, 73.28, 75.16, 69.64, 61.37, 56.97, 64.42, 60.13, 57.21, 60.66, 68.42, 67.28, 68.82, 73.26, 78.05, 73.53, 81.75, 91.14, 88, 93.85, 91.98, 100.04, 100.51, 112.71, 128.27, 140.3, 123.96, 115.17, 98.96, 65.6, 53.49, 45.59, 45.93, 45.84, 48.68, 50.64, 65.8, 69.42, 71.52, 69.32, 68.92, 75.09, 78.36, 77.93, 71.18, 78.03, 82.17, 87.35, 74.6, 74.66, 78.26, 74.42, 82.11, 83.26, 85.45, 94.59, 100.56, 112.1, 117.17, 126.03, 116.68, 111.8, 117.54, 114.49, 102.15, 109.19, 110.37, 107.22, 111.16, 123.04, 122.8, 119.47, 101.62, 97.57, 104.62, 114.92, 112.14, 108.4, 111.17, 111.11, 114.56, 111, 109.89, 101.74, 100.15, 101.5, 107.7, 114.45, 108.2, 108.9, 110.11, 110.9, 105.79, 108.65, 107.7, 108.14, 109.49, 112.4, 105.52, 103.11, 94.8, 85.96, 68.34, 57.54, 52.95]
DJIA = [88.5026, 89.8544, 92.338, 94.1582, 92.7506, 98.0112, 97.8246, 104.5392, 104.8807, 105.8392, 103.577, 102.2557, 101.8845, 104.3548, 101.3971, 101.7392, 100.8027, 100.2747, 104.2802, 107.8301, 104.8994, 107.6623, 105.0376, 101.9251, 104.6748, 102.7497, 106.4091, 104.816, 105.687, 104.4007, 108.0587, 107.175, 108.6486, 109.9341, 111.0932, 113.6714, 111.6831, 111.5022, 111.8568, 113.8115, 116.7907, 120.8073, 122.2193, 124.6315, 126.2169, 122.6863, 123.5435, 130.6291, 136.2764, 134.0862, 132.1199, 133.5774, 138.9563, 139.3001, 133.7172, 132.6482, 126.5036, 122.6639, 122.6289, 128.2013, 126.3832, 113.5001, 113.7802, 115.4396, 108.5066, 93.2501, 88.2904, 87.7639, 80.0086, 70.6293, 76.0892, 81.6812, 85.0033, 84.47, 91.7161, 94.9628, 97.1228, 97.1273, 103.4484, 104.2805, 100.6733, 103.2526, 108.5663, 110.0861, 101.3663, 97.7402, 104.6594, 100.1472, 107.8805, 111.1849, 110.0602, 115.7751, 118.9193, 122.2634, 123.1973, 128.1054, 125.6979, 124.1434, 121.4324, 116.1353, 109.1338, 119.5501, 120.4568, 122.1756, 126.3291, 129.5207, 132.1204, 132.1363, 123.9345, 128.8009, 130.0868, 130.9084, 134.3713, 130.9646, 130.2558, 131.0414, 138.6058, 140.5449, 145.7854, 148.398, 151.1557, 149.096, 154.9954, 148.1031, 151.2967, 155.4575, 160.8641, 165.7666, 156.9885, 163.2171, 164.5766, 165.8084, 167.1717, 168.266, 165.633, 170.9845, 170.429, 173.9052, 178.2824, 178.2307, 171.6495]
CAC_40 =[29.9175, 30.841, 32.1027, 33.1142, 31.3499, 33.732, 34.2479, 35.579, 36.3844, 37.2544, 36.2523, 36.7428, 36.6963, 37.3299, 36.471, 35.9428, 36.4061, 37.0682, 37.5375, 38.2116, 39.1369, 40.2716, 40.6778, 39.0893, 41.2073, 42.2935, 44.5174, 43.9936, 46.0002, 44.3645, 45.6741, 47.1523, 49.4799, 50.0045, 52.2085, 51.884, 49.3018, 49.6596, 50.0942, 51.6504, 52.5001, 53.4873, 53.2764, 55.4176, 56.0831, 55.1632, 56.3416, 59.3077, 61.04, 60.5493, 57.5108, 56.627, 57.1569, 58.4108, 56.675, 56.1408, 48.718, 47.9066, 47.0707, 49.9654, 50.1428, 44.2561, 43.9236, 44.8564, 40.2715, 34.8707, 32.6268, 32.1797, 29.6237, 26.9396, 28.0394, 31.5985, 32.7355, 31.3893, 34.2627, 36.5772, 37.9496, 36.0143, 36.8475, 39.3633, 37.3719, 37.088, 39.7401, 38.1699, 35.0756, 34.4289, 36.4314, 34.7618, 37.1518, 38.335, 36.1044, 38.0478, 40.055, 41.1035, 39.8918, 41.0692, 40.0694, 39.8078, 36.7277, 32.5676, 29.8196, 32.4284, 31.5462, 31.5981, 32.9855, 34.4794, 34.2381, 32.128, 30.0548, 31.9665, 32.9166, 34.1307, 33.5482, 34.2927, 35.5728, 36.4107, 37.326, 37.23, 37.3142, 38.5675, 39.4859, 37.3891, 39.9269, 39.3378, 41.4344, 42.9989, 42.9521, 42.9595, 41.6572, 44.0808, 43.915, 44.8739, 45.1957, 44.2284, 42.4614, 43.8104, 44.2676, 42.3309, 43.9018, 42.6355, 46.0425]
SSEC = [15.7626, 14.8602, 14.7674, 14.2198, 13.6716, 13.483, 13.9722, 14.9704, 15.9073, 16.7507, 17.4162, 15.9559, 15.5591, 13.9916, 13.862, 13.4206, 13.967, 13.2054, 13.4077, 12.665, 11.9182, 13.06, 11.8124, 11.5915, 10.6074, 10.8094, 10.8303, 11.628, 11.5561, 10.9282, 10.9926, 11.6106, 12.5805, 12.9903, 12.983, 14.4022, 16.413, 16.7221, 16.1273, 16.5864, 17.5242, 18.3799, 20.9929, 26.7547, 27.8634, 28.8107, 31.8398, 38.4127, 41.0965, 38.207, 44.7103, 52.1882, 55.523, 59.5477, 48.7178, 52.6156, 43.8339, 43.4854, 34.7271, 36.9311, 34.3335, 27.361, 27.7572, 23.9737, 22.9378, 17.2879, 18.7116, 18.2081, 19.9066, 20.8285, 23.7321, 24.7757, 26.3293, 29.5936, 34.1206, 26.6774, 27.7943, 29.9585, 31.953, 32.7714, 29.8929, 30.5194, 31.0911, 28.7061, 25.9215, 23.9837, 26.375, 26.388, 26.5566, 29.7883, 28.2018, 28.0808, 27.9069, 29.0505, 29.2811, 29.1151, 27.4347, 27.6208, 27.0173, 25.6734, 23.5922, 24.6825, 23.3341, 21.9942, 22.9261, 24.2849, 22.6279, 23.9632, 23.7223, 22.2543, 21.0363, 20.4752, 20.8617, 20.6888, 19.8012, 22.6913, 23.8542, 23.6559, 22.3662, 21.7791, 23.0059, 19.7921, 19.938, 20.9838, 21.7466, 21.4161, 22.205, 21.1598, 20.3308, 20.563, 20.3331, 20.2636, 20.3921, 20.4833, 22.0156, 22.172, 23.6387, 24.2018, 26.8283, 32.3468, 32.1036]


Brent_sample = [62.48, 55.1, 66.8, 65.19, 63.14, 51.85, 53.12, 48.44, 49.5, 44.5]
DJIA_sample = [181.327, 177.7612, 178.4052, 180.1068, 176.1951, 176.8986, 165.2803, 162.847, 176.6354, 177.1992]
CAC_40_sample = [49.2299, 50.3147, 50.4284, 50.8408, 48.1224, 50.8173, 46.5234, 44.5391, 48.8018, 49.5183]
SSEC_sample = [33.103, 37.479, 44.4166, 46.1174, 42.7722, 36.6373, 32.0599, 30.5278, 33.8256, 34.454]



MICEX = np.asarray(MICEX)
Brent = np.asarray(Brent)
DJIA = np.asarray(DJIA)
CAC_40 = np.asarray(CAC_40)
SSEC = np.asarray(SSEC)

Brent_sample = np.asarray(Brent_sample)
DJIA_sample = np.asarray(DJIA_sample)
CAC_40_sample = np.asarray(CAC_40_sample)
SSEC_sample = np.asarray(SSEC_sample)

size = len(MICEX)

inp = np.vstack((Brent, DJIA, CAC_40, SSEC)).T
tar = MICEX.reshape(size, 1)
smp = np.vstack((Brent_sample, DJIA_sample, CAC_40_sample, SSEC_sample)).T

# Create network with 2 layers and random initialized
net = nl.net.newelm(
        [[min(inp[:, 0]), max(inp[:, 0])],
         [min(inp[:, 1]), max(inp[:, 1])],
         [min(inp[:, 2]), max(inp[:, 2])],
         [min(inp[:, 3]), max(inp[:, 3])]
         ],
        [25, 1],
        [nl.trans.TanSig(), nl.trans.PureLin()]  # SatLinPrm(0.00000001, 421.08, 1925.24)
                )
# Set initialized functions and init
net.layers[0].initf = nl.init.InitRand([min(MICEX), max(MICEX)], 'wb')
net.layers[1].initf = nl.init.InitRand([min(MICEX), max(MICEX)], 'wb')
net.init()
# Changing train finction
# net.trainf = nl.train.train_bfgs
# Train network
error = net.train(inp, tar, epochs=10000, show=10, goal=1700, rr=0.1)


# Simulate network
out = net.sim(smp)
print('MICEX predictions for the next 10 periods:\n', out)

# answer:
