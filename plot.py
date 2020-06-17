<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ea70cb7... completed implementatiion of rk6 and reformatted code
import numpy as np
import matplotlib.pyplot as plt

########### for plotting trajectory of centre of mass of 2nd link ################
def plt_lnk2_cm(ax, states, ls, stp, solver, clr):
    # ax is Axes object
    # states in numpy array, each row = [t, theta1, theta2, theta1_dot, theta2_dot, p1, p2]
    # ls is 1-D numpy array, [l1, l2]
    # stp is float, incremental time step
    # solver is string, "E" or "I" or "rk4"
    # clr is string (1 character), color of curve to be plotted
    print("plotting trajectory of centre of mass of 2nd link")
    X1, X2, Y1, Y2 = [], [], [], []
<<<<<<< HEAD
    for i in range(np.size(states[:,0])):
        X1.append(ls[0]*np.sin(states[i,1])/2)
        Y1.append(-ls[0]*np.cos(states[i,1])/2) 
        X2.append(2*X1[i] + ls[1]*np.sin(states[i,2])/2)
        Y2.append(2*Y1[i] - ls[1]*np.cos(states[i,2])/2)
    ax.plot(X2, Y2, label=solver+": stp="+str(stp), color=clr)

    
=======
from functions import *

ni = 4
theta1_i = np.array([np.pi, np.pi+0.01, np.pi, np.pi+0.1])
theta2_i = np.array([np.pi+0.01, np.pi, np.pi-0.1, np.pi])
p1_i = np.array([0.0, 0.0, 0.0, 0.0])
p2_i = np.array([0.0, 0.0, 0.0, 0.0])

stp = 0.001
ti = 0.0
tf = 2

#set solver to 
#"I" if implicit is used
#"E" is explicit is used
#"rk4" if RK4 is used
#"rk6" if RK6 is used
solver = "E"
if (solver == "I"):             # setting up optional variables
    rel_err_tol = 1e-6                  # default value is 1e-4
    r = 0.0                    # default value is 0

for j in range (ni):
    print("initial conditions: ", j+1, "/", ni)
    states_arr = []
    theta1 = theta1_i[j]
    theta2 = theta2_i[j]
    p1 = p1_i[j]
    p2 = p2_i[j]
    # theta1_dot = theta1_dot_i[j]
    # theta2_dot = theta2_dot_i[j]
    t = ti
    
    while (t < tf):
        # print(t)
        theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2)
        theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2)
        states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
        t += stp
        if solver == "E":
            theta1, theta2, p1, p2 = explct(stp, theta1, theta2, p1, p2)
        elif solver == "I":
            theta1, theta2, p1, p2 = implct(stp, theta1, theta2, p1, p2, rel_err_tol, r)
        elif solver == "RK4":
            theta1, theta2, p1, p2 = rk4(stp, theta1, theta2, p1, p2)
        elif solver == "RK6":
            theta1, theta2, p1, p2 = rk6(stp, theta1, theta2, p1, p2)
    theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2)
    theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2)
    states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
    # print(states_arr)
    # print(len(states_arr), len(states_arr[0]))
    states = np.asarray(states_arr)
    # print(states.shape)

    print("plotting...")
    X1 = []
    X2 = []
    Y1 = []
    Y2 = []
    
    for i in range(np.size(states[:,0])):
        X1.append(l*np.sin(states[i,1])/2)
        Y1.append(-l*np.cos(states[i,1])/2) 
        X2.append(2*X1[i] + l*np.sin(states[i,2])/2)
        Y2.append(2*Y1[i] - l*np.cos(states[i,2])/2)
        
    # fig, ax1 = plt.subplots()   
    # fig, ax2 = plt.subplots()
    # print(len(X1), len(X2), len(Y1), len(Y2))
    # ax1.plot(states[:,1], states[:,2], label=str(j+1))
    # ax1.plot(X1,Y1,label=str(j+1))
    plt.plot(X2,Y2,color="green")
plt.plot(X2,Y2, label="0.001 sec",color="green")

stp = 0.005
for j in range (ni):
    print("initial conditions: ", j+1, "/", ni)
    states_arr = []
    theta1 = theta1_i[j]
    theta2 = theta2_i[j]
    p1 = p1_i[j]
    p2 = p2_i[j]
    # theta1_dot = theta1_dot_i[j]
    # theta2_dot = theta2_dot_i[j]
    t = ti
    
    while (t < tf):
        # print(t)
        theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2)
        theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2)
        states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
        t += stp
        if solver == "E":
            theta1, theta2, p1, p2 = explct(stp, theta1, theta2, p1, p2)
        elif solver == "I":
            theta1, theta2, p1, p2 = implct(stp, theta1, theta2, p1, p2, rel_err_tol, r)
        elif solver == "RK4":
            theta1, theta2, p1, p2 = rk4(stp, theta1, theta2, p1, p2)
        elif solver == "RK6":
            theta1, theta2, p1, p2 = rk6(stp, theta1, theta2, p1, p2)
    theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2)
    theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2)
    states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
    # print(states_arr)
    # print(len(states_arr), len(states_arr[0]))
    states = np.asarray(states_arr)
    # print(states.shape)

    print("plotting...")
    X1 = []
    X2 = []
    Y1 = []
    Y2 = []
    
=======
>>>>>>> ea70cb7... completed implementatiion of rk6 and reformatted code
    for i in range(np.size(states[:,0])):
        X1.append(ls[0]*np.sin(states[i,1])/2)
        Y1.append(-ls[0]*np.cos(states[i,1])/2) 
        X2.append(2*X1[i] + ls[1]*np.sin(states[i,2])/2)
        Y2.append(2*Y1[i] - ls[1]*np.cos(states[i,2])/2)
    ax.plot(X2, Y2, label=solver+": stp="+str(stp), color=clr)

    
<<<<<<< HEAD
    for i in range(np.size(states[:,0])):
        X1.append(l*np.sin(states[i,1])/2)
        Y1.append(-l*np.cos(states[i,1])/2) 
        X2.append(2*X1[i] + l*np.sin(states[i,2])/2)
        Y2.append(2*Y1[i] - l*np.cos(states[i,2])/2)
        
    # fig, ax1 = plt.subplots()   
    # fig, ax2 = plt.subplots()
    # print(len(X1), len(X2), len(Y1), len(Y2))
    # ax1.plot(states[:,1], states[:,2], label=str(j+1))
    # ax1.plot(X1,Y1,label=str(j+1))
    plt.plot(X2,Y2,color="blue")
plt.plot(X2,Y2,label="0.01 sec",color="blue")

stp = 0.04
for j in range (ni):
    print("initial conditions: ", j+1, "/", ni)
    states_arr = []
    theta1 = theta1_i[j]
    theta2 = theta2_i[j]
    p1 = p1_i[j]
    p2 = p2_i[j]
    # theta1_dot = theta1_dot_i[j]
    # theta2_dot = theta2_dot_i[j]
    t = ti
    
    while (t < tf):
        # print(t)
        theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2)
        theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2)
        states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
        t += stp
        if solver == "E":
            theta1, theta2, p1, p2 = explct(stp, theta1, theta2, p1, p2)
        elif solver == "I":
            theta1, theta2, p1, p2 = implct(stp, theta1, theta2, p1, p2, rel_err_tol, r)
        elif solver == "RK4":
            theta1, theta2, p1, p2 = rk4(stp, theta1, theta2, p1, p2)
        elif solver == "RK6":
            theta1, theta2, p1, p2 = rk6(stp, theta1, theta2, p1, p2)
    theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2)
    theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2)
    states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
    # print(states_arr)
    # print(len(states_arr), len(states_arr[0]))
    states = np.asarray(states_arr)
    # print(states.shape)

    print("plotting...")
    X1 = []
    X2 = []
    Y1 = []
    Y2 = []
    
    for i in range(np.size(states[:,0])):
        X1.append(l*np.sin(states[i,1])/2)
        Y1.append(-l*np.cos(states[i,1])/2) 
        X2.append(2*X1[i] + l*np.sin(states[i,2])/2)
        Y2.append(2*Y1[i] - l*np.cos(states[i,2])/2)
        
    # fig, ax1 = plt.subplots()   
    # fig, ax2 = plt.subplots()
    # print(len(X1), len(X2), len(Y1), len(Y2))
    # ax1.plot(states[:,1], states[:,2], label=str(j+1))
    # ax1.plot(X1,Y1,label=str(j+1))
    plt.plot(X2,Y2,color="yellow")
plt.plot(X2,Y2,label="0.04 sec",color="yellow")

# ax1.xlabel("X-axis")
# ax2.xlabel("X-axis")
# ax1.ylabel("Y-axis")
# ax2.ylabel("Y-axis")
# ax1.title("trajectory of 1st rod center")
# ax2.title("trajectory of 2nd rod center")
# ax1.show()
# ax2.show()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.title("Trajectory of the centre of 2nd link")
plt.show()
>>>>>>> bebeb27... plotting code
=======
>>>>>>> ea70cb7... completed implementatiion of rk6 and reformatted code
