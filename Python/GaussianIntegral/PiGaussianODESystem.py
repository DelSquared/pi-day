import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

L=int(input("Input evolutiontermination point: "))
#Evolution termination
x=np.linspace(0,L,50*L)
#Solution parameter to a very high degree of accuracy

def GaussianODE (y, x):
    u, v = y
    duv = [v, -2*x*v]
    return duv
#Transforms the Gaussian (y=e^-x^2) into a system of linear, homogeneous, ordinary differential eqns
#Let y=u'=v, y=e^-x^2 becomes u'=v and v'=-2xv. The limiting value of u as x->oo should be sqrt(Pi)/2
#since integrating the Gaussian over [0,oo) gives that exact result

y=odeint(GaussianODE, [0,1], x)
#Solving the system of ODEs with initial conditions u(0)=0, v(0)=1

pie=y[y.shape[0]-1,0]
#Extracting a potential value for "pi"

plt.plot(x,y[:,0], label=r'$u(x)$')
plt.plot(x,y[:,1], label=r'$v(x)$')
plt.legend(loc='best')
plt.show()
#Plotting the evolution of the solutions. We expect v to be half a Gaussian and u to be asymptotic to sqrt(Pi)/2

print(4*pie*pie)
#The calculated value of "pi"
