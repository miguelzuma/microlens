import numpy,pylab
from scipy.integrate import odeint

def Rhalf(Rp,Rn,a,b):

	r = numpy.linspace(0.001,Rp,100)

	def pmthr(area,r):
		c = (a**2 + b**2)**0.5
		ctheta = (r**2 + c**2 - Rn**2)/(2*c*r)
		if ctheta < -1:
			return 0
		if ctheta > 1:
			return numpy.pi*r
		return (numpy.pi - numpy.arccos(ctheta))*r


	area = odeint(pmthr,[0],r)

	for i in range(1,len(r)):
		if area[i-1] < 0.5*area[-1] and area[i] > 0.5*area[-1]:
			return r[i]

print Rhalf(25.0,0.0,15.0,10.0)



