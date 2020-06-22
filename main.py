# usage: python3 main.py

from functions import *
from plot import *
from datetime import datetime


############################################################################################        
############################ setting up initial parameters #################################
############################################################################################
# MANDATORY: all the next 4 arrays should have same length
theta1_i = np.array([np.pi, np.pi+0.01, np.pi, np.pi+0.1]) # initial values of theta1
theta2_i = np.array([np.pi+0.01, np.pi, np.pi-0.1, np.pi]) # initial values of theta2
p1_i = np.array([0.0, 0.0, 0.0, 0.0])                      # initial values of p1
p2_i = np.array([0.0, 0.0, 0.0, 0.0])                      # initial values of p2

mss = np.array([[1.0, 1.0], [10.0, 1.0]])       # array of mass of links, each row = [m1, m2]
lss = np.array([[1.0, 1.0], [10.0, 1.0]])       # array of length of links, each row = [l1, l2]

stps = [0.001, 0.0005, 0.01]          # incremental time step
ti = 0.0                        # initial time
tf = 5.0                        # final time

# set solvers and store as a list of dictionary 
# "I" if implicit is used
# "E" is explicit is used
# "rk4" if RK4 is used
slvrs = [{"solver": "rk4"}, {"solver": "rk4"}]
for slvr in slvrs:
    if (slvr["solver"] == "I"):             # setting up optional variables
        slvr["rel_err_tol"] = 1e-6          # default value is 1e-6
        slvr["r"] = 0.0                     # default value is 0

# choosing the plotting function plt_lnk2_cm or plt_te
plt_fun = plt_te

# choosing which parameters to iterate over
# CAUTION: for sensible output make sure that only 1 for loop is iterating more than once
# ........ therfore all but 1 or 2 of the following variables should be 1.
I, J, K, L, M = 1, 1, 1, 1, 1

# for plotting  different length and mass ratios in different subplots
# NOTE: set both nrws and ncls = L or M or 1
nrws = L                        # number of rows of subplots
ncls = M                        # number of columns of subplots

# CUSTOMIZED plotting, e.g. for plotting some benchmark curve in all plot(s)
# set do_cust_plot to True for customized plotting and other variables appropriately
do_cust_plot = False
cust_slvr = {"solver": "rk4"}
if (cust_slvr["solver"] == "I"):             # setting up optional variables
    cust_slvr["rel_err_tol"] = 1e-6          # default value is 1e-6
    cust_slvr["r"] = 0.0                     # default value is 0
cust_stp = 0.01
cust_ys_inits = np.array([theta1_i[0], theta2_i[0], p1_i[0], p2_i[0]], dtype=np.float64)



############################################################################################        
############### effect of changing initial conditions, time step and solvers ###############
############################################################################################
ys_inits = np.array([z for z in zip(theta1_i, theta2_i, p1_i, p2_i)], dtype=np.float64)
clrs = ['b', 'm', 'g', 'r', 'y', 'c'] # list of colours to be used for plotting, extend list if needed
lbls0 = [""]*I*J*K*L*M
if plt_fun == plt_lnk2_cm:
    ttl = "Trajectory of the centre of 2nd link"
    xlbl, ylbl = "X-axis", "Y-axis"
    aspct = "equal"
elif plt_fun == plt_te:
    ttl = "Total energy of the system"
    xlbl, ylbl = "time", "Total energy"
    aspct = "auto"
else:
    raise Exception("Invalid plotting function: plt_fun")
fig, axs = plt.subplots(nrows = nrws, ncols = ncls) # change first argument of plt_lnk2_cm based on nrows and ncols
for i in range(0, I):             # iterating over initial conditions, ys_inits
    if I != 1:
        lblsi = [str(ys_inits[i])+" | "+lbl for lbl in lbls0]
    else:
        lblsi = lbls0
    for j in range(0, J):         # iterating over solvers, slvrs
        if J != 0:
            lblsj = [str(slvrs[j]["solver"])+" | "+lbl for lbl in lblsi]
        else:
            lblsj = lblsi
        for k in range(0, K):     # iterating over time steps, stps
            if K != 0:
                lblsk = [str(stps[k])+" | "+lbl for lbl in lblsj]
            else:
                lblsk = lblsj
            for l in range(0, L):     # iterating over lengths, lss
                if L != 1:
                    lblsl = ["L: "+str(lss[l])+" | "+lbl for lbl in lblsk]
                else:
                    lblsl = lblsk
                for m in range(0, M): # iterating over masses, mss
                    if M != 1:
                        lblsm = ["M: "+str(mss[m])+" | "+lbl for lbl in lblsl]
                    else:
                        lblsm = lblsl
                    print("initial conditions: ", ys_inits[i])
                    plt_i = (((i*J + j)*K + k)*L + l)*M + m # index of lbls and clrs
                    states = solve(stps[k], ti, tf, slvrs[j], ys_inits[i], mss[m], lss[l])
                    if nrws == 1 and ncls == 1:
                        plt_fun(axs, states, lss[l], mss[m], lblsm[plt_i], clrs[plt_i])
                    elif nrws == 1 or ncls == 1:
                        if ncls*nrws == L:
                            plt_fun(axs[l], states, lss[l], mss[m], lblsm[plt_i], clrs[plt_i])
                        elif ncls*nrws == M:
                            plt_fun(axs[m], states, lss[l], mss[m], lblsm[plt_i], clrs[plt_i])
                        else:
                            raise Exception("invalid nrws or ncls")
                    elif ncls*nrws == L*M:
                        plt_fun(axs[l, m], states, lss[l], mss[m], lblsm[plt_i], clrs[plt_i])
                    else:
                        raise Exception("invalid nrws or ncls")
                        
if nrws == 1 and ncls == 1:
    if do_cust_plot:
        print("initial conditions: ", cust_ys_inits)
        states = solve(cust_stp, ti, tf, cust_slvr, cust_ys_inits, mss[0], lss[0])
        plt_fun(axs, states, lss[0], mss[0], str(cust_stp)+" | "+cust_slvr["solver"], 'k')
    axs.set_xlabel(xlbl)
    axs.set_ylabel(ylbl)
    axs.legend()
    axs.set_aspect(aspct)
elif nrws == 1 or ncls == 1:
    for i in range(nrws*ncls):
        print("initial conditions: ", cust_ys_inits)
        if do_cust_plot:
            if ncls*nrws == L:
                states = solve(cust_stp, ti, tf, cust_slvr, cust_ys_inits, mss[0], lss[i])
                plt_fun(axs[i], states, lss[i], mss[0], "L: "+str(lss[i])+" | "+str(cust_stp)+" | "+cust_slvr["solver"], 'k')
            else:
                states = solve(cust_stp, ti, tf, cust_slvr, cust_ys_inits, mss[i], lss[0])
                plt_fun(axs[i], states, lss[0], mss[i], "M: "+str(mss[i])+" | "+str(cust_stp)+" | "+cust_slvr["solver"], 'k')                
        axs[i].set_xlabel(xlbl)
        axs[i].set_ylabel(ylbl)
        axs[i].legend()
        axs[i].set_aspect(aspct)
else:
    for l in range(0, L):
        for m in range(0, M):
            if do_cust_plot:
                print("initial conditions: ", cust_ys_inits)
                states = solve(cust_stp, ti, tf, cust_slvr, cust_ys_inits, mss[m], lss[l])
                plt_fun(axs[l, m], states, lss[l], mss[m], "L: "+str(lss[l])+" | M: "+str(mss[m])+" | "+str(cust_stp)+" | "+cust_slvr["solver"], 'k')
            axs[l, m].set_xlabel(xlbl)
            axs[l, m].set_ylabel(ylbl)
            axs[l, m].legend()
            axs[l, m].set_aspect(aspct)
    
fig.suptitle(ttl)
now = datetime.now()
current_time = str(now.strftime("%H:%M:%S"))
fig.savefig("plot_" + current_time.replace(":", "_") + ".png")
plt.show()
