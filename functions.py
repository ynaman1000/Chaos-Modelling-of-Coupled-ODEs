import numpy as np

g = 9.81

# ys, ms, ls are numpy arrays
# ys is 1-D array with 4 elements, [theta1, theta2, p1, p2]
# ms is 1-D array with 2 elements, [m1, m2]
# ls is 1-D array with 2 elements, [l1, l2]


################# defining PDEs to be solved #################
def h1(ys, ms, ls):
    return (ys[2] * ys[3] * np.sin(ys[0]-ys[1])) / \
        (ls[0]*ls[1] * (ms[0]+ms[1]*(np.sin(ys[0]-ys[1])**2)))

def h2(ys, ms, ls):
    return (ms[1]*(ls[1]**2)*(ys[2]**2) + (ms[0]+ms[1])*(ls[0]**2)*(ys[3]**2) - 2*ms[1]*ls[0]*ls[1]*ys[2]*ys[3]*np.cos(ys[0]-ys[1])) / \
        (2*(ls[0]**2)*(ls[1]**2) * ((ms[0]+ms[1]*(np.sin(ys[0]-ys[1])**2))**2))

def theta1_dot_fun(ys, ms, ls):
    return (ls[1]*ys[2] - ls[0]*ys[3]*np.cos(ys[0]-ys[1])) / \
        ((ls[0]**2)*ls[1] * (ms[0]+ms[1]*(np.sin(ys[0]-ys[1])**2)))

def theta2_dot_fun(ys, ms, ls):
    return (-ms[1]*ls[1]*ys[2]*np.cos(ys[0]-ys[1]) + (ms[0]+ms[1])*ls[0]*ys[3]) / \
        (ms[1]*ls[0]*(ls[1]**2) * (ms[0]+ms[1]*(np.sin(ys[0]-ys[1])**2)))

def p1_dot_fun(ys, ms, ls):
    return -(ms[0]+ms[1])*g*ls[0]*np.sin(ys[0]) - h1(ys, ms, ls) + h2(ys, ms, ls)*np.sin(2*(ys[0]-ys[1]))

def p2_dot_fun(ys, ms, ls):
    return -ms[1]*g*ls[1]*np.sin(ys[1]) + h1(ys, ms, ls) - h2(ys, ms, ls)*np.sin(2*(ys[0]-ys[1]))

fs = [theta1_dot_fun, theta2_dot_fun, p1_dot_fun, p2_dot_fun]


################ defining explicit solver #####################
def explct(stp, ys, ms, ls):
    return np.array([(ys[i] + stp*fs[i](ys, ms, ls)) for i in range(4)], dtype=np.float64)


################ defining implicit solver #####################
# helper function for convergence condition of inner loop in implicit solver
def hgh_rel_err(act, app, rel_err_tol):
    # act, app are numpy arrays with actual and approximate values respectively
    # rel_err_tol is float
    # print("inner_loop_err: ", np.amax(np.divide(np.absolute(acc-app), (acc+1e-12))))
    return np.amax(np.divide(np.absolute(act-app), (act+1e-12))) > rel_err_tol

def implct(stp, ys, ms, ls, rel_err_tol, r):
    y_iters = y_prevs = ys
    ys = [(y_prevs[i] + stp*fs[i](y_iters, ms, ls)) for i in range(4)]
    while hgh_rel_err(np.array(ys, dtype=np.float64), y_iters, rel_err_tol):
        y_iters = [(y_prevs[i]*r + ys[i]*(1-r)) for i in range(4)]
        ys = [(y_prevs[i] + stp*fs[i](y_iters, ms, ls)) for i in range(4)]
    return np.array(ys, dtype=np.float64)


############ defining Runge-Kutta 4th order solver #############
def rk4(stp, ys, ms, ls):
    K1 = np.array([stp*fs[i](ys, ms, ls) for i in range(4)], dtype=np.float64)
    K2 = np.array([stp*fs[i](ys+K1/2, ms, ls) for i in range(4)], dtype=np.float64)
    K3 = np.array([stp*fs[i](ys+K2/2, ms, ls) for i in range(4)], dtype=np.float64)
    K4 = np.array([stp*fs[i](ys+K3, ms, ls) for i in range(4)], dtype=np.float64)
    return np.array([(ys[i] + (K1[i]+2*K2[i]+2*K3[i]+K4[i])/6) for i in range(4)], dtype=np.float64)


########## for solving PDEs, using one of the solver defined above #########
def solve(stp, ti, tf, slvr, ys, ms, ls):
    t = ti
    states = [[t, ys[0], ys[1], theta1_dot_fun(ys, ms, ls), theta2_dot_fun(ys, ms, ls), ys[2], ys[3]]]
    while (t < tf+stp):
        # print(t)
        t += stp
        if slvr["solver"] == "E":
            ys = explct(stp, ys, ms, ls)
        elif slvr["solver"] == "I":
            ys = implct(stp, ys, ms, ls, slvr["rel_err_tol"], slvr["r"])
        elif slvr["solver"] == "rk4":
            ys = rk4(stp, ys, ms, ls)
        states.append([t, ys[0], ys[1], theta1_dot_fun(ys, ms, ls), theta2_dot_fun(ys, ms, ls), ys[2], ys[3]])
    # print(len(states), len(states[0]))
    return np.array(states, dtype=np.float64)
