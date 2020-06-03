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
              explct(stp)
    states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
  
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
    states_arr.append([t, theta1, theta2, theta1_dot, theta2_dot, p1, p2])
    return states_arr
