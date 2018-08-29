import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import image 
img = image.imread('./scientist.jpeg') 
gray_img = np.dot(img[:,:,:3], [.21, .72, .07]) 
gray_img.shape 
# (317L, 661L) 
plt.imshow(gray_img, cmap = plt.get_cmap('gray')) 
plt.show()
