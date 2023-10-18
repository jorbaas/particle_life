import numpy as np

a = np.array([[42, 53], [294, 410], [102, 12]])
b = np.array([[568, 13], [346, 474], [93, 390]])

# Reshape the arrays to have a third dimension (1x1x2) for broadcasting
a = a[:, np.newaxis, :]
b = b[np.newaxis, :, :]

# Calculate the squared Euclidean distance
distance_squared = np.sum((a - b)**2, axis=2)

# Calculate the Euclidean distance by taking the square root of the squared distances
distance = np.sqrt(distance_squared)

print(distance)