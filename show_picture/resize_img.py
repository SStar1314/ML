import scipy.misc 
import matplotlib.pyplot as plt 
import numpy as np

lena = scipy.misc.ascent()

LENA_X = 512 
LENA_Y = 512

np.testing.assert_equal((LENA_Y, LENA_X), lena.shape)

yfactor = 2 
xfactor = 3

resized = lena.repeat(yfactor, axis=0).repeat(xfactor, axis=1)

np.testing.assert_equal((yfactor * LENA_Y, xfactor * LENA_Y), resized.shape)

plt.subplot(211) 
plt.title("Lena") 
plt.axis("off") 
plt.imshow(lena)

plt.subplot(212) 
plt.title("Resized") 
plt.axis("off") 
plt.imshow(resized) 
plt.show()
