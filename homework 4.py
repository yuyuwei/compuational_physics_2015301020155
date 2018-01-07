import numpy as np
import matplotlib.pyplot as plt  #to import matplotlib's package

v=[]       #velocity
t=[]       #time
a=10       #assign a value to a
b=1        #assign a value to b
det_t=0.05     #time step
v.append(0) #assign a value to first item of v[]
t.append(0) #assign a value to first item of t[]
end_time=15  #total time

for i in range(int(end_time/det_t)):
    tmp=v[i]+(a-b*v[i])*det_t  #Euler method
    v.append(tmp)  #add new value of v to v[]
    t.append(det_t*(i+1)) #add new value of t to t[]
    print t[-1],v[-1] #print the value of v and t on each stap

plt.figure(figsize=(8,6))  #set the size of corresponding figure
plt.plot(t,v,label="v(t)",color="black",linewidth=1) #plot the figure and set label and color and linewidth of the figure
plt.xlabel("t(s)")   #set the label of x axis
plt.ylabel("v(m/s)")  #set the label of y axis
plt.title("a=10,b=1,v=0") #set title
plt.ylim(0,25) #set the range of y axis
plt.legend()  #make it to show everything
plt.show()  #activate
