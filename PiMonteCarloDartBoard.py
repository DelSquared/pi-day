import numpy as np
from matplotlib import pyplot as plt

Total=int(input("Input the number of iterations: "))
Inside=0

x=np.linspace(0,1,500)
y=np.sqrt(1-x**2)

X = np.random.uniform(0, 1,(Total))
Y = np.random.uniform(0, 1,(Total))
plt.plot(x, y,'b-')
plt.axes().set_aspect('equal')
tt = plt.title(r'$\pi=${}'.format(4*Inside/1))

for i in range(Total):
    if X[i]*X[i]+Y[i]*Y[i]<=1:
        Inside+=1
    plt.plot(x, y,'b-')
    plt.plot(X[i], Y[i],'r.')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    tt.set_text(r'$\pi=${0:.25f}'.format(4*Inside/(i+1)))
    plt.draw()
    plt.pause(0.000001)
print("\nPi = ",4*Inside/Total,"\n")
