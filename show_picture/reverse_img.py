import scipy.misc 
import matplotlib.pyplot as plt

lena = scipy.misc.ascent()

plt.subplot(221) 
plt.title('Original') 
plt.axis('off') 
plt.imshow(lena)

plt.subplot(222) 
plt.title('Flipped') 
plt.axis('off') 
plt.imshow(lena[:,::-1])

plt.subplot(223)
plt.title('Sliced') 
plt.axis('off') 
plt.imshow(lena[:lena.shape[0]/2,:lena.shape[1]/2])

mask = lena % 2 == 0 
masked_lena = lena.copy() 
masked_lena[mask] = 0 

plt.subplot(224) 
plt.title('Masked') 
plt.axis('off') 
plt.imshow(masked_lena)
plt.show()
