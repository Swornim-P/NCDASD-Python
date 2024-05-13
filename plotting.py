import matplotlib.pyplot as plt
import numpy as np



def projectile (u, theta):
    theta = theta*(np.pi/180)
    g     = 9.8
    theta = theta * np.pi/180
    T     = 2*u*np.sin(theta)/g
    R     = u**2*np.sin(2*theta)/g
    H     = u**2*(np.sin(theta))**2/(2*g)
    return [T, R, H]

proj = projectile(100, 45)
print(proj)
u=100
theta=np.arange(0, 30, 10) 

print(theta)
plt.plot(theta, proj)
plt.xlabel('Angle')
plt.ylabel('Max. height')
plt.title('Projectile')
plt.savefig('proj2.png')
plt.show()