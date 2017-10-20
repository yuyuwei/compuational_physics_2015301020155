#coding:utf-8
#initial value
import math
t=[]
dt=0.01    #B/m=4*10-5 realy count
g=9.8
end_time=120
t.append(0)
w=4000*math.pi
v_1=7   #initial volocity
v_2=70
S=4.1*10**-4
#define variable
x_1=[]
v_x_1=[]
y_1=[]
v_y_1=[]
z_1=[]
v_z_1=[]
x_1.append(0)
y_1.append(0)
z_1.append(0)
v_x_1.append(v_1)  #initial speed equal 700m/s
v_y_1.append(v_2)
v_z_1.append(0)
x_2=[]
v_x_2=[]
y_2=[]
v_y_2=[]
z_2=[]
v_z_2=[]
x_2.append(0)
y_2.append(0)
z_2.append(0)
v_x_2.append(v_1)  #initial speed equal 700m/s
v_y_2.append(v_2)
v_z_2.append(0)
#caulate the coordinate
for i in range(int(end_time/dt)):
      d=x_1[i]+v_x_1[i]*dt
      x_1.append(d)
      e=v_x_1[i]-dt*(0.0039+0.0058/(1+math.e**(((v_x_1[i]**2+v_y_1[i]**2+v_z_1[i]**2)**0.5-35)/5)))*((v_x_1[i]**2+v_y_1[i]**2+v_z_1[i]**2)**0.5)*v_x_1[i]
      v_x_1.append(e)
      f=y_1[i]+v_y_1[i]*dt
      y_1.append(f)
      h=v_y_1[i]-g*dt
      v_y_1.append(h)
      z_1.append(0)
      v_z_1.append(0)
      j=x_2[i]+v_x_2[i]*dt
      x_2.append(j)
      p=v_x_2[i]-dt*(0.0039+0.0058/(1+math.e**(((v_x_2[i]**2+v_y_2[i]**2+v_z_2[i]**2)**0.5-35)/5)))*((v_x_2[i]**2+v_y_2[i]**2+v_z_2[i]**2)**0.5)*v_x_2[i]
      v_x_2.append(p)
      l=y_2[i]+v_y_2[i]*dt
      y_2.append(l)
      m=v_y_2[i]-g*dt
      v_y_2.append(m)
      n=z_2[i]+v_z_2[i]*dt
      z_2.append(n)
      o=v_z_2[i]-dt*S*v_x_2[i]*w
      v_z_2.append(o)
#draw the picture
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x_1, y_1, z_1, label='no spin')
ax.plot(x_2,y_2,z_2,   label='spin')
ax.legend()
plt.show()
