import numpy as np
from matplotlib import pyplot as plt

side_length = 2
origin = np.array([0,0])
vertices = [origin]	
initial_angle = np.pi/float(6)
rotational_angle = np.pi/float(2)

def point_finder(x1, r, theta):
	x2 = x1 + r*np.array([np.cos(theta), np.sin(theta)])
	return x2
	
a = origin
for i in range(1,4):
	a = point_finder(a, side_length, initial_angle+(i-1)*rotational_angle)
	vertices.append(a)

point_name = ['O', 'W', 'Y', 'Z']

len = 100
lam = np.linspace(0,1,len)
OW = np.zeros((2, len))
WY = np.zeros((2, len))
YZ = np.zeros((2, len))
ZO = np.zeros((2, len))

for i in range(len):
	OW[:,i] = vertices[0] + lam[i]*(vertices[1] - vertices[0])
	WY[:,i] = vertices[1] + lam[i]*(vertices[2] - vertices[1])
	YZ[:,i] = vertices[2] + lam[i]*(vertices[3] - vertices[2])
	ZO[:,i] = vertices[3] + lam[i]*(vertices[0] - vertices[3])
	
plt.plot(OW[0,:], OW[1,:], label='$OW$')
plt.plot(WY[0,:], WY[1,:], label='$WY$')
plt.plot(YZ[0,:], YZ[1,:], label='$YZ$')
plt.plot(ZO[0,:], ZO[1,:], label='$ZO$')

sum_of_x_cor = 0
for j,i in enumerate(vertices):
	plt.plot(i[0], i[1], 'o')
	plt.text(vertices[j][0]*(1), vertices[j][1]*(1), point_name[j]+str(vertices[j].round(3)))
	sum_of_x_cor += vertices[j][0]

print("sum of X coordinates is {}.".format(sum_of_x_cor))
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend(loc='best')
plt.title('plot for question 13')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid(True, which='both')
plt.xlim(-2,3)
plt.ylim(-1, 3)
plt.show()
