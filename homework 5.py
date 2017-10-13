import math
import numpy as np
import matplotlib.pyplot as plt
t=[]
dt=0.01
g=9.8
end_time = 200
a=30*math.pi/180
b=45*math.pi/180
c=60*math.pi/180
angle = [a,b,c]
t.append(0)
x_1=[]
v_x_1=[]
y_1=[]
v_y_1=[]
x_1.append(0)
y_1.append(0)
v_x_1.append(700*math.cos(angle[0]))
v_y_1.append(700*math.sin(angle[0]))
for i in range(int(end_time/dt)):
	m=x_1[i]+v_x_1[i]*dt
	x_1.append(m)
	n=v_x_1[i]
	v_x_1.append(n)
	o=y_1[i]+v_y_1[i]*dt
	y_1.append(o)
	p=v_y_1[i]-g*dt
	v_y_1.append(p)
	#print x_1[-1],y_1[-1]
    	if o <= 0 :
    		break
print x_1[-1],y_1[-1]

x_2=[]
v_x_2=[]
y_2=[]
v_y_2=[]
x_2.append(0)
y_2.append(0)
v_x_2.append(700*math.cos(angle[1]))
v_y_2.append(700*math.sin(angle[1]))
for i in range(int(end_time/dt)):
	m=x_2[i]+v_x_2[i]*dt
	x_2.append(m)
	n=v_x_2[i]
	v_x_2.append(n)
	o=y_2[i]+v_y_2[i]*dt
	y_2.append(o)
	p=v_y_2[i]-g*dt
	v_y_2.append(p)
	#print x_2[-1],y_2[-1]
    	if o <= 0 :
    		break
print x_2[-1],y_2[-1]
		
x_3=[]
v_x_3=[]
y_3=[]
v_y_3=[]
x_3.append(0)
y_3.append(0)
v_x_3.append(700*math.cos(angle[2]))
v_y_3.append(700*math.sin(angle[2]))
for i in range(int(end_time/dt)):
	m=x_3[i]+v_x_3[i]*dt
	x_3.append(m)
	n=v_x_3[i]
	v_x_3.append(n)
	o=y_3[i]+v_y_3[i]*dt
	y_3.append(o)
	p=v_y_3[i]-g*dt
	v_y_3.append(p)
	#print x_3[-1],y_3[-1]
    	if o <= 0 :
    		break
print x_3[-1],y_3[-1]

plt.figure(figsize=(8,6))
plt.plot(x_1,y_1,label="$30^\circ$",color="red",linewidth=2)
plt.plot(x_2,y_2,label="$45^\circ$",color="green",linewidth=2)
plt.plot(x_3,y_3,label="$60^\circ$",color="black",linewidth=2)
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.ylim(0,20000)
plt.legend()
plt.show()
