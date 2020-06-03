import numpy as np
import matplotlib.pyplot as plt
from functions import *

theta1_i = np.array([1,1,1.0012,1,1,1,1,1.0012])*np.pi/2
theta2_i = np.array([1,0.9988,1,1,1,1,1,0.9988])*np.pi/2
p1_i = np.array([0,0,0,0.01,0,-0.01,0,0.01])
p2_i = np.array([0,0,0,0,0.01,0,-0.01,-0.01])
stp = 0.01

#set solver to 
#"I" if implicit is used
#"E" is explicit is used
#"rk4" if RK4 is used
#"rk6" if RK6 is used
solver = "I"

for j in range (0,8):
    states_arr = [[]]
    theta1 = theta1_i[j]
    theta2 = theta2_i[j]
    p1 = p1_i[j]
    p2 = p2_i[j]
    t = ti
    theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2)
    theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2)
    while (t < tf):
            states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
            t = ti+stp
            if solver == "E":
              theta1, theta2, p1, p2, theta1_dot, theta2_dot = explct(stp, theta1, theta2, p1, p2)
            if solver == "I":
              theta1, theta2, p1, p2, theta1_dot, theta2_dot = implct(stp, theta1, theta2, p1, p2)
            if solver == "RK4":
              theta1, theta2, p1, p2, theta1_dot, theta2_dot = rk4(stp, theta1, theta2, p1, p2)
            if solver == "RK6":
              theta1, theta2, p1, p2, theta1_dot, theta2_dot = rk6(stp, theta1, theta2, p1, p2)
    states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
    states = np.asarray(states_arr) 
    X1 = []
    X2 = []
    Y1 = []
    Y2 = []
    for i in np.size(states[:,0]): #size of a column of states
        X1.append(l*cos(states[i,1])/2) 
        Y1.append(-l*sin(states[i,1])/2)
        X2.append(2*X1 + l*cos(states[i,1])/2)
        Y2.append(-2*Y1 - l*sin(states[i,1])/2)
    fig, ax1 = plt.subplots()   
    fig, ax2 = plt.subplots()    
    ax1.plot(X1,Y1,label=str(j))
    ax2.plot(X2,Y2,label=str(j))
ax1.xlabel("X-axis")
ax2.xlabel("X-axis")
ax1.ylabel("Y-axis")
ax2.ylabel("Y-axis")
ax1.title("trajectory of 1st rod center")
ax2.title("trajectory of 2nd rod center")
ax1.show()
ax2.show()
