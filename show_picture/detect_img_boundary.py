import scipy 
import scipy.ndimage 
import matplotlib.pyplot as plt

lena = scipy.misc.ascent()

plt.subplot(221) 
plt.imshow(lena) 
plt.title('Original') 
plt.axis('off')


sobelx = scipy.ndimage.sobel(lena, axis=0, mode='constant')
plt.subplot(222) 
plt.imshow(sobelx) 
plt.title('Sobel X') 
plt.axis('off')

sobely = scipy.ndimage.sobel(lena, axis=1, mode='constant')
plt.subplot(223) 
plt.imshow(sobely) 
plt.title('Sobel Y') 
plt.axis('off')

default = scipy.ndimage.sobel(lena)
plt.subplot(224) 
plt.imshow(default) 
plt.title('Default Filter') 
plt.axis('off')
plt.show()
