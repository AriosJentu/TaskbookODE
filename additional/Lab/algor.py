import math

def f(t):
	return math.cos(t-1)**2 / (t**2 + 1)
	# return complex(math.exp(-t)/(t+2*math.pi*1j)).imag
	# return math.sin(t)

def integrate(a, b, n, f):
	
	res = 0
	h = (b-a)/n

	for i in range(n):
		res += f(a+h*i)*h

	return res

s = integrate(0, math.pi, 1000, f)



def fourier(a, b, n, n2, m, f):
	resSin = []
	resCos = []
	x = []

	ds = m/n2
	
	coeff = 2*math.pi
	# coeff = 1

	for i in range(n2):

		g = lambda t: f(t)*math.sin(i*ds*t*coeff)
		h = lambda t: f(t)*math.cos(i*ds*t*coeff)

		s = integrate(a, b, n, g)
		c = integrate(a, b, n, h)

		x.append(i*ds)
		resSin.append(s)
		resCos.append(c)
		print(i*ds, s, c)

	return x, resSin, resCos

a = 0
b = 1
m = 3
x, si, co = fourier(a, b, 1000, 500, m, f)
# x, si, co = fourier(0, math.pi, 1000, 1000, 2, f)
print(max(si), min(si))
print(max(co), min(co))

import matplotlib.pyplot as plt
plt.plot(x, co, label="Cosine wave")
plt.plot(x, si, label="Sine wave")
plt.legend()
plt.grid(True)
# plt.plot(co)
plt.show()


def func(entity, *params):
	entity.move(params[1])
