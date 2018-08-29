import numpy as np
import matplotlib.pyplot as plt

# func = x ** 3 + 2 * x ** 2 + 3 * x + 4
func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
x = np.linspace(-10, 10, 40)
y = func(x)

func1 = func.deriv(m=1)
y1 = func1(x)

plt.plot(x, y, 'ro', x, y1, 'g--')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()


