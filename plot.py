import numpy as np
import matplotlib.pyplot as plt

########### for plotting trajectory of centre of mass of 2nd link ################
def plt_lnk2_cm(ax, states, ls, lbl, solver, clr):
    # ax is Axes object
    # states in numpy array, each row = [t, theta1, theta2, theta1_dot, theta2_dot, p1, p2]
    # ls is 1-D numpy array, [l1, l2]
    # stp is float, incremental time step
    # solver is string, "E" or "I" or "rk4"
    # clr is string (1 character), color of curve to be plotted
    print("plotting trajectory of centre of mass of 2nd link")
    X1, X2, Y1, Y2 = [], [], [], []
    for i in range(np.size(states[:,0])):
        X1.append(ls[0]*np.sin(states[i,1])/2)
        Y1.append(-ls[0]*np.cos(states[i,1])/2) 
        X2.append(2*X1[i] + ls[1]*np.sin(states[i,2])/2)
        Y2.append(2*Y1[i] - ls[1]*np.cos(states[i,2])/2)
    ax.plot(X2, Y2, label=lbl, color=clr)
