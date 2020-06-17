import numpy as np
import matplotlib.pyplot as plt

########### for plotting trajectory of centre of mass of 2nd link ################
def plt_lnk2_cm(ax, states, ls, ms, lbl, clr):
    # ax is Axes object
    # states in numpy array, each row = [t, theta1, theta2, theta1_dot, theta2_dot, p1, p2]
    # ls is 1-D numpy array, [l1, l2]
    # stp is float, incremental time step
    # clr is string (1 character), color of curve to be plotted
    print("plotting trajectory of centre of mass of 2nd link")
    X1 = ls[0]*np.sin(states[:,1])/2
    Y1 = -ls[0]*np.cos(states[:,1])/2
    X2 = 2*X1 + ls[1]*np.sin(states[:,2])/2
    Y2 = 2*Y1 - ls[1]*np.cos(states[:,2])/2
    ax.plot(X2, Y2, label=lbl, color=clr)


############## for plotting total energy of system ##################    
def plt_te(ax, states, ls, ms, lbl, clr):
    # states in numpy array, each row = [t, theta1, theta2, theta1_dot, theta2_dot, p1, p2]
    # ls is 1-D numpy array, [l1, l2]
    # ms is 1-D numpy array, [m1, m2]
    print("plotting total energy of the system")
    g = 9.81
    Is = [(ms[i]*(ls[i]**2))/12 for i in range(2)]
    y1 = -(ls[0]*np.cos(states[:, 1]))/2
    y2 = -ls[0]*np.cos(states[:, 1]) - (ls[1]*np.cos(states[:, 2]))/2
    x1_dot = (ls[0]*np.cos(states[:, 1])*states[:, 3])/2
    y1_dot = (ls[0]*np.sin(states[:, 1])*states[:, 3])/2
    x2_dot = (ls[0]*np.cos(states[:, 1])*states[:, 3]) + (ls[1]*np.cos(states[:, 2])*states[:, 4])/2
    y2_dot = (ls[0]*np.sin(states[:, 1])*states[:, 3]) + (ls[1]*np.sin(states[:, 2])*states[:, 4])/2
    pe = g*(ms[0]*y1 + ms[1]*y2)
    ke = (1/2)*(ms[0]*(x1_dot**2 + y1_dot**2) + ms[1]*(x2_dot**2 + y2_dot**2) + Is[0]*(states[:, 3]**2) + Is[1]*(states[:, 4]**2))
    ax.plot(states[:, 0], ke+pe, label=lbl, color=clr)
