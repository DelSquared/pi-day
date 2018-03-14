import numpy as np
from matplotlib import pyplot as plt
 
Total=int(input("Input the number of iterations: "))

Inside=0 #counts the number of darts inside the quarter circle
 
x=np.linspace(0,1,500)
y=np.sqrt(1-x**2) # to draw the quarter circle
 
plt.plot(x, y,'b-') #plots quarter circle
plt.axes().set_aspect('equal') #sets axes to equal scales for a better presentation, this produces a warning but it can be ignored
tt = plt.title(r'$\pi=${}'.format(4*Inside/1)) #displays the current value of "pi" on top of the plot
 
for i in range(Total):
    X = np.random.uniform(0, 1)
    Y = np.random.uniform(0, 1) #Generate dart landing locations
    if X*X+Y*Y<=1:
        Inside+=1 #checks whether dart fell in the centre, the SQRT was omitted to improve performance since SQRT(1)=1
    plt.plot(x, y,'b-') #replots circle to keep it visible in case of large amount of iterations
    plt.plot(X, Y,'r.') #plot dart
    plt.xlim([0, 1])
    plt.ylim([0, 1]) #axes limits
    tt.set_text(r'$\pi=${0:.25f}'.format(4*Inside/(i+1))) #update value of "pi"
    plt.draw()
    plt.pause(0.000001)
print("\nPi = ",4*Inside/Total,"\n") #print final value of "pi"
