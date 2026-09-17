import numpy as np

def driver():

    # Original equation: roots satisfy F(x) = 0
    F = lambda x: x - 4*np.sin(2*x) - 3

    # Fixed-point iteration given by the problem
    g = lambda x: -np.sin(2*x) + (5/4)*x - 3/4

    Nmax = 1000
    tol = 1e-11

    x0 = -0.8

    [xstar, ier] = fixedpt(g, x0, tol, Nmax)

    print('the approximate fixed point is:', xstar)
    print('F(xstar):', F(xstar))
    print('Error message reads:', ier)


def fixedpt(f, x0, tol, Nmax):

    count = 0

    while count < Nmax:
        count = count + 1
        x1 = f(x0)

        if abs(x1 - x0) < tol:
            xstar = x1
            ier = 0
            return [xstar, ier]

        x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]


driver()
