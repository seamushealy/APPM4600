def fixedpt(f, x0, tol, Nmax):
    import numpy as np
    '''x0 = initial guess'''
    '''Nmax = max number of iterations'''
    '''tol = stopping tolerance'''

    count = 0
    phat = np.array([])
    while count < Nmax:
        count = count + 1
        x1 = f(x0)
        phat = np.append(phat, x1)
        if abs(x1 - x0) < tol:
            xstar = x1
            ier = 0
            return [xstar, ier, count, phat]

        x0 = x1
        
    xstar = x1
    ier = 1
    count = 0
    return [xstar, ier, count, phat]