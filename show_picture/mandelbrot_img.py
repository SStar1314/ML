import numpy as np
import matplotlib.pyplot as plt 
from scipy.misc import ascent

ITERATIONS = 10 
lena = ascent() 
SIZE = lena.shape[0] 
MAX_COLOR = 255. 
x_min, x_max = -2.5, 1 
y_min, y_max = -1, 1

x, y = np.meshgrid(np.linspace(x_min, x_max, SIZE),
                   np.linspace(y_min, y_max, SIZE)) 
c = x + 1j * y 
z = c.copy() 
fractal = np.zeros(z.shape, dtype=np.uint8) + MAX_COLOR 

for n in range(ITERATIONS):
    mask = np.abs(z) <= 4
    z[mask] = z[mask] ** 2 +  c[mask]
    fractal[(fractal == MAX_COLOR) & (~mask)] = (MAX_COLOR - 1) * n / ITERATIONS

plt.subplot(211) 
plt.imshow(fractal) 
plt.title('Mandelbrot') 
plt.axis('off')

plt.subplot(212) 

plt.imshow(np.choose(fractal < lena, [fractal, lena])) 
plt.axis('off') 
plt.title('Mandelbrot + Lena')
plt.show()
