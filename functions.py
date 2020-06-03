import numpy as np
import matplotlib.pyplot as plt

m = 1
l = 1
g = 9.81
ti = 0
tf = 10
tol = 1e-6
r = 0.01

def hgh_rel_err(acc, app):
    return np.amax(np.divide(np.absolute(acc-app), acc)) > tol

def theta1_dot_fun(theta1, theta2, p1, p2):
    return (6/(m*(l**2))) * (2*p1 - 3*cos(theta1-theta2)*p2) / (16 - 9*(cos(theta1-theta2)**2))

def theta2_dot_fun(theta1, theta2, p1, p2):
    return (6/(m*(l**2))) * (8*p2 - 3*cos(theta1-theta2)*p1) / (16 - 9*(cos(theta1-theta2)**2))

def p1_dot_fun(theta1, theta2, theta1_dot, theta2_dot):
    return ((-m*(l**2))/2) * (theta1_dot*theta2_dot*sin(theta1-theta2) + (3*g*sin(theta1))/l)

def p2_dot_fun(theta1, theta2, p1, p2):
    return ((-m*(l**2))/2) * (-theta1_dot*theta2_dot*sin(theta1-theta2) + (g*sin(theta2))/l)

def explct(stp, theta1, theta2, p1, p2):
            theta1 = theta1 + stp*theta1_dot_fun(theta1, theta2, p1, p2)
            theta2 = theta2 + stp*theta2_dot_fun(theta1, theta2, p1, p2)
            p1 = p1 + stp*p1_dot_fun(theta1, theta2, p1, p2)
            p2 = p2 + stp*p2_dot_fun(theta1, theta2, p1, p2)
            theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2)
            theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2)
            return theta1, theta2, p1, p2, theta1_dot, theta2_dot

def implct(stp):
        theta1_iter = theta1_prev = theta_1
        theta2_iter = theta2_prev = theta_2
        p1_iter = p1_prev = p_1
        p2_iter = p2_prev = p_2

        theta1 = theta_1_prev + stp*theta1_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter)
        theta2 = theta_2_prev + stp*theta2_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter)
        p1 = p_1_prev + stp*p1_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter)
        p2 = p_2_prev + stp*p2_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter)

        while hgh_rel_err([theta1, theta2, p1, p2], [theta1_iter, theta2_iter, p1_iter, p2_iter]):
            theta1_iter = theta_1*r + theta1*(1-r)
            theta2_iter = theta_2*r + theta2*(1-r)
            p1_iter = p_1*r + p1*(1-r)
            p2_iter = p_2*r + p2*(1-r)

            theta1 = theta_1_prev + stp*theta1_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter)
            theta2 = theta_2_prev + stp*theta2_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter)
            p1 = p_1_prev + stp*p1_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter)
            p2 = p_2_prev + stp*p2_dot_fun(theta1_iter, theta2_iter, p1_iter, p2_iter)

        theta1_dot = theta1_dot_fun(theta1, theta2, p1, p2)
        theta2_dot = theta2_dot_fun(theta1, theta2, p1, p2)
        return theta1, theta2, p1, p2, theta1_dot, theta2_dot

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
