图1代码
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

图二代码
import math
import matplotlib.pyplot as plt
x=[];y=[];v_x=[];v_y=[];t=[];i=[];theta_list=[];x_list=[]
dt=0.01;g=-9.8;v_init=700

for theta in range(30,61):
    i.append(0)
    v_x.append(v_init*math.cos(theta*math.pi/180))
    v_y.append(v_init*math.sin(theta*math.pi/180))
    x.append(0.0)
    y.append(0.0)
    t.append(0.0)
    while y[-1]>=0.0:
        x_tmp=x[-1]+dt*v_x[-1]
        x.append(x_tmp)
        v_x_tmp=v_x[-1]
        v_x.append(v_x_tmp)
        y_tmp=y[-1]+dt*v_y[-1]
        y.append(y_tmp)
        v_y_tmp=v_y[-1]+dt*g
        v_y.append(v_y_tmp)
        i_tmp=i[-1]+1
        i.append(i_tmp)
        t.append(dt*i[-1])        
     
    theta_list.append(theta);x_list.append(x[-1])
    
	print theta,t[-1],x[-1],v_x[-1],y[-1],v_y[-1]
plt.plot(theta_list,x_list,'or' , label="(theta,shoot range)",color = "g")
plt.xlabel("theta/$\circ$")
plt.ylabel("shoot range/m")
plt.title('the relationship bewteen Theta and shoot range of a cannon shell')
plt.legend()
plt.show()

图三代码
import math
import numpy as np
import matplotlib.pyplot as plt
t=[]
dt=0.01
B_2_m=4*10**(-5)
g=9.8
end_time = 200
a=22.5*math.pi/180
b=45*math.pi/180
c=67.5*math.pi/180
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
	n=v_x_1[i]-B_2_m*((v_x_1[i]**2+v_y_1[i]**2)**0.5)*v_x_1[i]*dt
	v_x_1.append(n)
	o=y_1[i]+v_y_1[i]*dt
	y_1.append(o)
	p=v_y_1[i]-g*dt-B_2_m*((v_x_1[i]**2+v_y_1[i]**2)**0.5)*v_y_1[i]*dt
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
	n=v_x_2[i]-B_2_m*((v_x_2[i]**2+v_y_2[i]**2)**0.5)*v_x_2[i]*dt
	v_x_2.append(n)
	o=y_2[i]+v_y_2[i]*dt
	y_2.append(o)
	p=v_y_2[i]-g*dt-B_2_m*((v_x_2[i]**2+v_y_2[i]**2)**0.5)*v_y_2[i]*dt
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
	n=v_x_3[i]-B_2_m*((v_x_3[i]**2+v_y_3[i]**2)**0.5)*v_x_3[i]*dt
	v_x_3.append(n)
	o=y_3[i]+v_y_3[i]*dt
	y_3.append(o)
	p=v_y_3[i]-g*dt-B_2_m*((v_x_3[i]**2+v_y_3[i]**2)**0.5)*v_y_3[i]*dt
	v_y_3.append(p)
	#print x_3[-1],y_3[-1]
    	if o <= 0 :
    		break
print x_3[-1],y_3[-1]

plt.figure(figsize=(8,6))
plt.plot(x_1,y_1,label="$22.5^\circ$",color="red",linewidth=2)
plt.plot(x_2,y_2,label="$45^\circ$",color="green",linewidth=2)
plt.plot(x_3,y_3,label="$67.5^\circ$",color="black",linewidth=2)
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.ylim(0,15000)
plt.legend()
plt.show()

图四代码
import math
import matplotlib.pyplot as plt
x=[]
y=[]
v_x=[]
v_y=[]
t=[]
i=[]
theta_list=[]
x_list=[]
v=[]
dt=0.01
g=-9.8
v_init=700
B=0.00004

for theta in range(30,61):
    i.append(0);v.append(v_init)
    v_x.append(v_init*math.cos(theta*math.pi/180))
    v_y.append(v_init*math.sin(theta*math.pi/180))
    x.append(0.0)
    y.append(0.0)
    t.append(0.0)
    while y[-1]>=0.0:
        v.append(math.sqrt(v_x[-1]**2+v_y[-1]**2))
        x_tmp=x[-1]+dt*v_x[-1]
        x.append(x_tmp)
        v_x_tmp=v_x[-1]-B*v[-1]*v_x[-1]*dt
        v_x.append(v_x_tmp)
        y_tmp=y[-1]+dt*v_y[-1]
        y.append(y_tmp)
        v_y_tmp=v_y[-1]+dt*g-B*v[-1]*v_y[-1]*dt
        v_y.append(v_y_tmp)
        i_tmp=i[-1]+1
        i.append(i_tmp)
        t.append(dt*i[-1])
        
     
    theta_list.append(theta);x_list.append(x[-1])
    print theta,t[-1],x[-1],v_x[-1],y[-1],v_y[-1]
plt.plot(theta_list,x_list,'or' , label="(theta,shoot range)",color = "r")
plt.xlabel("theta/$\circ$")
plt.ylabel("shoot range/m")
plt.title('the relationship bewteen Theta and shoot range \n of a cannon shell with air drag')
plt.legend()
plt.show()

图五代码
import math
import matplotlib.pyplot as plt
x=[]
y=[]
v_x=[]
v_y=[]
t=[]
i=[]
theta_list=[]
x_list=[]
v=[]
dt=0.01
g=-9.8
v_init=700
B=0.00004
y_0 = 0.0001
for theta in range(30,61):
    i.append(0);v.append(v_init)
    v_x.append(v_init*math.cos(theta*math.pi/180))
    v_y.append(v_init*math.sin(theta*math.pi/180))
    x.append(0.0)
    y.append(0.0)
    t.append(0.0)
    while y[-1]>=0.0:
        v.append(math.sqrt(v_x[-1]**2+v_y[-1]**2))
        x_tmp=x[-1]+dt*v_x[-1]
        x.append(x_tmp)
        v_x_tmp=v_x[-1]-math.e**(-y[-1]*y_0)*B*v[-1]*v_x[-1]*dt
        v_x.append(v_x_tmp)
        y_tmp=y[-1]+dt*v_y[-1]
        y.append(y_tmp)
        v_y_tmp=v_y[-1]+dt*g-math.e**(-y[-1]*y_0)*B*v[-1]*v_y[-1]*dt
        v_y.append(v_y_tmp)
        i_tmp=i[-1]+1
        i.append(i_tmp)
        t.append(dt*i[-1])     
     
    theta_list.append(theta);x_list.append(x[-1])
    print theta,x[-1],v_x[-1],y[-1],v_y[-1]
plt.plot(theta_list,x_list,'or' , label="(theta,shoot range)",color = "r")
plt.xlabel("theta/$\circ$")
plt.ylabel("shoot range/m")
plt.title('the relationship bewteen Theta and shoot range \n of a cannon shell with air drag')
plt.legend()
plt.show()

图六代码
import math
import matplotlib.pyplot as plt
x=[]
y=[]
v_x=[]
v_y=[]
t=[]
i=[]
theta_list=[]
x_list=[]
v=[]
dt=0.01
g=-9.8
v_init=700
B=0.00004
y_0 = 0.0001
a = 6.5*10**(-3)
b =2.5
T_0 = 300
for theta in range(30,60):
    i.append(0);v.append(v_init)
    v_x.append(v_init*math.cos(theta*math.pi/180))
    v_y.append(v_init*math.sin(theta*math.pi/180))
    x.append(0.0)
    y.append(0.0)
    t.append(0.0)
    while y[-1]>=0.0:
        v.append(math.sqrt(v_x[-1]**2+v_y[-1]**2))
        x_tmp=x[-1]+dt*v_x[-1]
        x.append(x_tmp)
        v_x_tmp=v_x[-1]-((1-a*y[-1]/T_0)**b)*B*v[-1]*v_x[-1]*dt
        v_x.append(v_x_tmp)
        y_tmp=y[-1]+dt*v_y[-1]
        y.append(y_tmp)
        v_y_tmp=v_y[-1]+dt*g-((1-a*y[-1]/T_0)**b)*B*v[-1]*v_y[-1]*dt
        v_y.append(v_y_tmp)
        i_tmp=i[-1]+1
        i.append(i_tmp)
        t.append(dt*i[-1])     
     
    theta_list.append(theta);x_list.append(x[-1])
    print theta,t[-1],x[-1],v_x[-1],y[-1],v_y[-1]
plt.plot(theta_list,x_list,'or' , label="(theta,shoot range)",color = "r")
plt.xlabel("theta/$\circ$")
plt.ylabel("shoot range/m")
plt.title('the relationship bewteen Theta and shoot range \n of a cannon shell with air drag under adiabatic approximation')
plt.legend()
plt.show()

图七代码
import math
coordinate=(300,400)
def calculation(angle,T):
    x=0
    y=0
    ax=-4*10**(-5)*700**2*cos(angle)
    ay=-4*10**(-5)*700**2*sin(angle)
    vx=700*cos(angle)
    vy=700*sin(angle)
    v=700
    dt=T
    t=0
    while x<=coordinate[0]:
        x=x+vx*dt
        y=y+vy*dt
        ax=-4*10**(-5)*(1-2.18*10**(-5)*y)**2.5*v*vx
        ay=-4*10**(-5)*(1-2.18*10**(-5)*y)**2.5*v*vy
        vx=vx+ax*dt
        vy=vy-9.8*dt+ay*dt
        v=(vx**2+vy**2)**(0.5)
        t=t+T
    return x,y,t

def correction():
    a=0    
    while abs(calculation(a*pi/180,0.01)[1]-coordinate[1])>=100:
        a=a+1
    return a
def furthercorrection():
    A=correction()-1
    while abs(calculation(A*pi/180,0.0001)[1]-coordinate[1])>=1:
        A=A+0.1
    return A,calculation(A*pi/180,0.0001)

print furthercorrection()
