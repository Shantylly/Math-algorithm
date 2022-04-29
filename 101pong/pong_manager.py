import sys
import math
from math import *

# ----------------------------------------------------------------------- #

def check_args():
    i = 1
    while i < 8:
        if (sys.argv[i].isnumeric() is False and sys.argv[i].isdecimal is False):
            exit(84)
        i = i + 1

# ---------------------------------------------------------------------- #

def calculate_coords(ball, vector, time):
    x = vector.x * time + ball.x1
    y = vector.y * time + ball.y1
    z = vector.z * time + ball.z1
    show_coords(x, y, z)

# ---------------------------------------------------------------------- #

def check_coords(ball, vector1, result):
    if (result < 0 or result > 90):
        print("The ball won't reach the paddle.")
        exit(0)
    if (vector1.z == 0 and ball.z1 != 0):
        print("The ball won't reach the paddle.")
        exit(0)
    if (-ball.z1 / (ball.z1 - ball.z0) < 0):
        print("The ball won't reach the paddle.")
        exit(0)
    if (vector1.x == 0 or vector1.y == 0 or vector1.z == 0):
        print("The ball won't reach the paddle.")
        exit(0)

# ---------------------------------------------------------------------- #

def help():
    print("USAGE\n     ./101pong x0 y0 z0 x1 y1 z1 n\n")
    print("DESCRIPTION")
    print("    x0  ball abscissa at time t - 1")
    print("    y0  ball ordinate at time t - 1")
    print("    z0  ball altitude at time t - 1")
    print("    x1  ball abscissa at time t")
    print("    y1  ball ordinate at time t")
    print("    z1  ball altitude at time t")
    print("    n   time shift (greater than or equal to zero, integer)")

# ---------------------------------------------------------------------- #

def show_result(ball, vector1, time):
    print("The velocity vector of the ball is:")
    show_coords(vector1.x, vector1.y, vector1.z)
    print("At time t + " + str(time) + ", ball coordinates will be:")
    calculate_coords(ball, vector1, time)
    nvx = pow(ball.x1 - ball.x0, 2)
    nvy = pow(ball.y1 - ball.y0, 2)
    nvz = pow(ball.z1 - ball.z0, 2)
    result = 90 - (acos(abs(ball.z1 - ball.z0) / sqrt(nvx + nvy + nvz))) * 180 / pi
    check_coords(ball, vector1, result)
    print("The incidence angle is:\n%.2f degrees" % result)

# ---------------------------------------------------------------------- #

def show_coords(x, y, z):
    print("(%.2f, %.2f, %.2f)" % (x, y, z))

# ---------------------------------------------------------------------- #