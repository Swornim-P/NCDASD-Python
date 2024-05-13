import numpy as np
import projectile as pjt
import matplotlib.pyplot as plt

def proj (u, theta):
    theta = theta*(np.pi/180)
    g     = 9.8
    theta = theta * np.pi/180
    T     = 2*u*np.sin(theta)/g
    R     = u**2*np.sin(2*theta)/g
    H     = u**2*(np.sin(theta))**2/(2*g)
    return [T, R, H]



#Projectile
    
# print("range: ", pjt.range(25, 45))

# print("height: ",pjt.height(50, 30))

# print("time of flight: ", pjt.time(100, 30))



# print("Projectile: ", pjt.proj(100, 30))
# p=pjt.proj(100, 30)

# print('Time of flight=',p[0])
# print('Range=',p[1])
# print('Max.height=',p[2])
p=proj(100, 30)
print('Time of flight=',p[0])
print('Range=',p[1])
print('Max.height=',p[2])

angle = np.arange(0, 91, 5)

theta = 30
plt.plot(angle, p[0] )
plt.plot(theta, proj[0])
plt.xlabel('Angle')
plt.ylabel('Time of flight')
plt.title('Projectile')
plt.savefig('proj1.png')
plt.show()
