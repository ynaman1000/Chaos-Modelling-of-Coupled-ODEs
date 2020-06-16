import numpy as np
import matplotlib.pyplot as plt

g = 9.81

def hgh_rel_err(acc, app, rel_err_tol):
    # print("inner_loop_err: ", np.amax(np.divide(np.absolute(acc-app), (acc+1e-12))))
    return np.amax(np.divide(np.absolute(acc-app), (acc+1e-12))) > rel_err_tol

def theta1_dot_fun(theta1, theta2, p1, p2, m, l):
    return (6/(m*(l**2))) * (2*p1 - 3*np.cos(theta1-theta2)*p2) / (16 - 9*(np.cos(theta1-theta2)**2))

def theta2_dot_fun(theta1, theta2, p1, p2, m, l):
    return (6/(m*(l**2))) * (8*p2 - 3*np.cos(theta1-theta2)*p1) / (16 - 9*(np.cos(theta1-theta2)**2))

def p1_dot_fun(theta1, theta2, p1, p2, m, l):
    return ((-m*(l**2))/2) * \
        (theta1_dot_fun(theta1, theta2, p1, p2, m, l)*theta2_dot_fun(theta1, theta2, p1, p2, m, l)*np.sin(theta1-theta2) + (3*g*np.sin(theta1))/l)

def p2_dot_fun(theta1, theta2, p1, p2, m, l):
    return ((-m*(l**2))/2) * \
        (-theta1_dot_fun(theta1, theta2, p1, p2, m, l)*theta2_dot_fun(theta1, theta2, p1, p2, m, l)*np.sin(theta1-theta2) + (g*np.sin(theta2))/l)

def explct(stp, theta1, theta2, p1, p2, m, l):
    theta1 = theta1 + stp*theta1_dot_fun(theta1, theta2, p1, p2, m, l)
    theta2 = theta2 + stp*theta2_dot_fun(theta1, theta2, p1, p2, m, l)
    p1 = p1 + stp*p1_dot_fun(theta1, theta2, p1, p2, m, l)
    p2 = p2 + stp*p2_dot_fun(theta1, theta2, p1, p2, m, l)
    # theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2)
    # theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2)
    return theta1, theta2, p1, p2

def implct(stp, theta1, theta2, p1, p2, m, l, rel_err_tol, r):
    theta1_iter = theta1_prev = theta1
    theta2_iter = theta2_prev = theta2
    p1_iter = p1_prev = p1
    p2_iter = p2_prev = p2
    # theta1_dot_iter = theta1_dot_prev = theta1_dot
    # theta2_dot_iter = theta2_dot_prev = theta2_dot

    theta1 = theta1_prev + stp*theta1_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter, m, l)
    theta2 = theta2_prev + stp*theta2_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter, m, l)
    p1 = p1_prev + stp*p1_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter, m, l)
    p2 = p2_prev + stp*p2_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter, m, l)
    # theta1_dot = theta1_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter, m, l)
    # theta2_dot = theta2_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter, m, l)
    # theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2, m, l)
    # theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2, m, l)

    # while hgh_rel_err(np.array([theta1, theta2, p1, p2, theta1_dot, theta2_dot]),\
        #                   np.array([theta1_iter, theta2_iter, p1_iter, p2_iter, theta1_dot_iter, theta2_dot_iter]),\
        #                   rel_err_tol):
    while hgh_rel_err(np.array([theta1, theta2, p1, p2]),\
                      np.array([theta1_iter, theta2_iter, p1_iter, p2_iter]),\
                      rel_err_tol):
        # print("inner_loop", p1, p1_iter)
        theta1_iter = theta1_prev*r + theta1*(1-r)
        theta2_iter = theta2_prev*r + theta2*(1-r)
        p1_iter = p1_prev*r + p1*(1-r)
        p2_iter = p2_prev*r + p2*(1-r)
        # theta1_dot_iter = theta1_dot_prev*r + theta1_dot*(1-r)
        # theta2_dot_iter = theta2_dot_prev*r + theta2_dot*(1-r)

        theta1 = theta1_prev + stp*theta1_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter, m, l)
        theta2 = theta2_prev + stp*theta2_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter, m, l)
        p1 = p1_prev + stp*p1_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter, m, l)
        p2 = p2_prev + stp*p2_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter, m, l)
        # theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2, m, l)
        # theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2, m, l)

    return theta1, theta2, p1, p2

def solve(theta1, theta2, p1, p2, m, l, stp, ti, tf, solver, rel_err_tol=1e-6, r=0.0):
    states_arr = []
    
    # theta1_dot = theta1_dot_i[j]
    # theta2_dot = theta2_dot_i[j]
    t = ti

    while (t < tf):
        # print(t)
        theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2, m, l)
        theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2, m, l)
        states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
        t += stp
        if solver == "E":
            theta1, theta2, p1, p2 = explct(stp, theta1, theta2, p1, p2, m, l)
        elif solver == "I":
            theta1, theta2, p1, p2 = implct(stp, theta1, theta2, p1, p2, m, l, rel_err_tol, r)
        # elif solver == "RK4":
        #     theta1, theta2, p1, p2 = rk4(stp, theta1, theta2, p1, p2)
        # elif solver == "RK6":
        #     theta1, theta2, p1, p2 = rk6(stp, theta1, theta2, p1, p2)
        theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2, m, l)
        theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2, m, l)
        states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
        # print(states_arr)
        # print(len(states_arr), len(states_arr[0]))
        states = np.asarray(states_arr)
        # print(states.shape)

    return states

# f = open("out.txt", "r")
# dat = []
# while True:
# 	line = f.readline()
# 	if line == '':
# 		break
# 	else:
# 		dat.extend([[float(i) for i in line.split(' ')]])
# dat = np.array(dat)
# # print(dat[3:, 0])
# plt.plot(dat[3:, 0], dat[3:, 1])
# plt.plot(dat[0:3, 0], dat[0:3, 1], 'ko')
# # plt.plot(dat[:, 0], dat[:, 1], 'ko')
# for r in dat[0:3, :]:
# 	plt.text(r[0], r[1], '({}, {})'.format(r[0], r[1]))
# plt.xlabel('x')
# plt.ylabel('y')
# plt.savefig('chain_py.png')
# plt.show()
