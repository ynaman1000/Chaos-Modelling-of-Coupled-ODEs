import numpy as np
import matplotlib.pyplot as plt
from functions import *

theta1_i = np.array([np.pi, np.pi+0.01, np.pi, np.pi+0.1])
theta2_i = np.array([np.pi+0.01, np.pi, np.pi-0.1, np.pi])
p1_i = np.array([0.0, 0.0, 0.0, 0.0])
p2_i = np.array([0.0, 0.0, 0.0, 0.0])
ni = theta1_i.size

ms = np.array([1.0])
ls = np.array([1.0])

stp = 0.001
ti = 0.0
tf = 2.0

#set solver to 
#"I" if implicit is used
#"E" is explicit is used
#(not implemented) "rk4" if RK4 is used
#(not implemented) "rk6" if RK6 is used
solver = "E"
if (solver == "I"):             # setting up optional variables
    rel_err_tol = 1e-6                  # default value is 1e-6
    r = 0.0                    # default value is 0


for j in range(ms.size):
    for k in range(ls.size):
        for i in range (ni):
            print("initial conditions: ", i+1, "/", ni)
            states = solve(theta1_i[i], theta2_i[i], p1_i[i], p2_i[i], ms[j], ls[k], stp, ti, tf, solver)

            print("plotting...")
            X1 = []
            X2 = []
            Y1 = []
            Y2 = []

            # print(np.size(states[:, 0]))
            for xi in range(np.size(states[:,0])):
                X1.append(ls[k]*np.sin(states[xi,1])/2)
                Y1.append(-ls[k]*np.cos(states[xi,1])/2) 
                X2.append(2*X1[xi] + ls[k]*np.sin(states[xi,2])/2)
                Y2.append(2*Y1[xi] - ls[k]*np.cos(states[xi,2])/2)

            # fig, ax1 = plt.subplots()   
            # fig, ax2 = plt.subplots()
            # print(len(X1), len(X2), len(Y1), len(Y2))
            # ax1.plot(states[:,1], states[:,2], label=str(i+1))
            # ax1.plot(X1,Y1,label=str(i+1))
            # print(X2, Y2)
            plt.plot(X2,Y2,label=str(i+1))
    
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
        plt.title("trajectory of the centre of 2nd link")
        plt.show()
