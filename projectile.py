import numpy as np
g=9.8
def range(u, t):  #u is speed in m/s, t is angle in degree
    theta = t*(np.pi/180)
    x= u**2
    y=(np.sin(2*theta))/g
    rng=x*y
    return rng


def height(u, theta):
    theta =  theta*(np.pi/180)
    h=u**2*(np.sin(theta))**2/(2*g)
    return h

def time (u, theta):
    theta =  theta*(np.pi/180)
    T= 2*u*np.sin(theta)/g    
    return T

def proj (u, theta):
    theta = theta*(np.pi/180)
    g     = 9.8
    theta = theta * np.pi/180
    T     = 2*u*np.sin(theta)/g
    R     = u**2*np.sin(2*theta)/g
    H     = u**2*(np.sin(theta))**2/(2*g)
    return [T, R, H]

    