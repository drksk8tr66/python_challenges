import decimal 
import numpy as np

decimal.getcontext().prec = 30
dec = decimal.Decimal

a0 = 1
b0 = 1 / np.sqrt(dec(2))
t0 = 1 / dec(4)
p0 = 1

while np.abs(a0 - b0) > 10**(-30):

	a1 = (a0 + b0)/2
	b1 = np.sqrt(a0*b0)
	t1 = t0 - p0*(a0 - a1)**2
	p1 = 2 * p0

	pi = (a1 + b1)**2 / (4*t1)

	a0 = a1
	b0 = b1
	t0 = t1
	p0 = p1

print(pi)