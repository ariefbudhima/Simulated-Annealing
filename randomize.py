import random
import math

x1 = random.uniform(-10,10)	
x2 = random.uniform(-10,10)
Ta = 1000000
Tb = 0.000000001
alph = 0.99
cstate = ((4-(2.1*x1**2)+((x1**4)/3))*(x1**2))+(x1*x2)+((-4+4*(x2**2))*(x2**2))

print 'state awal = ',cstate
print 'x1 awal = ',x1
print 'x2 awal = ',x2
print ' '

while Ta>Tb :
	x1b = random.uniform(-10,10)
	x2b = random.uniform(-10,10)
	nstate = ((4-(2.1*x1b**2)+((x1b**4)/3))*(x1b**2))+(x1b*x2b)+((-4+4*(x2b**2))*(x2b**2))
	

	if cstate>nstate:
		cstate = nstate
		x1 = x1b
		x2 = x2b

	else:
		deltaE = nstate-cstate
		p = math.exp(-deltaE/Ta)
		r = random.uniform(0,1)
		if r<p :
			cstate = nstate
			x1 = x1b
			x2 = x2b
	
	Ta = Ta*alph

print 'Temperature sekarang = ',Ta
print 'Temperature minimum = ',Tb
print ''
print 'state akhir = ',cstate
print 'x1 akhir = ',x1
print 'x2 akhir = ',x2
