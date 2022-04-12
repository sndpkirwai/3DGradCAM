import numpy as np
fin = open('GradCAM_outputs/Examples/inouts/1.raw')
img = np.fromfile(fin)

print("Dimension of the old image array: ", img.ndim)
print("Size of the old image array: ", img.size)