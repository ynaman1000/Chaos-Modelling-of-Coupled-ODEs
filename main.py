# usage: python3 main.py

from functions import *
from plot import *

############################################################################################        
############################ setting up initial parameters #################################
############################################################################################
theta1_i = np.array([np.pi, np.pi+0.01, np.pi, np.pi+0.1]) # initial values of theta1
theta2_i = np.array([np.pi+0.01, np.pi, np.pi-0.1, np.pi]) # initial values of theta2
p1_i = np.array([0.0, 0.0, 0.0, 0.0])                      # initial values of p1
p2_i = np.array([0.0, 0.0, 0.0, 0.0])                      # initial values of p2

mss = np.array([[1.0, 10.0], [10.0, 1.0]])       # array of mass of links, each row = [m1, m2]
lss = np.array([[1.0, 10.0], [10.0, 1.0]])       # array of length of links, each row = [l1, l2]

stps = [0.0001, 0.001]          # incremental time step
ti = 0.0                        # initial time
tf = 2.0                        # final time

# set solvers and store as a list of dictionary 
# "I" if implicit is used
# "E" is explicit is used
# "rk4" if RK4 is used
slvrs = [{"solver": "rk4"}]
ys_inits = np.array([z for z in zip(theta1_i, theta2_i, p1_i, p2_i)], dtype=np.float64)
for slvr in slvrs:
    if (slvr["solver"] == "I"):             # setting up optional variables
        slvr["rel_err_tol"] = 1e-6                  # default value is 1e-6
        slvr["r"] = 0.0                    # default value is 0


############################################################################################        
############### effect of changing initial conditions, time step and solvers ###############
############################################################################################
clrs = ['b', 'k', 'g', 'r', 'y', 'c'] # list of colours to be used for plotting, extend list if needed
# CAUTION: for sensible output make sure that only 1 for loop is iterating more than once
# ........ therfore all but 1 of the following variables should be 1.
I, J, K, L, M = 1, 1, 1, len(lss), 1
lbls = []                             # data legends, fill accordingly
fig, ax = plt.subplots()
for i in range(0, I):             # iterating over initial conditions, ys_inits
    for j in range(0, J):         # iterating over solvers, slvrs
        for k in range(0, K):     # iterating over time steps, stps
            for l in range(0, L):     # iterating over lengths, lss
                for m in range(0, M): # iterating over masses, mss
                    print("initial conditions: ", ys_inits[i])
                    plt_i = i*len(slvrs)+j*len(stps)+k*lss.shape[0]+l*mss.shape[0]+m # index of lbls and clrs
                    states = solve(stp[k], ti, tf, slvrs[j], ys_inits[i], ms[m], lss[l])
                    plt_lnk2_cm(ax, states, ls, lbls[plt_i], slvrs[j]["solver"], clrs[plt_i])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
ax.set_title("Trajectory of the centre of 2nd link")
fig.savefig("plot1.svg")
# plt.show()
