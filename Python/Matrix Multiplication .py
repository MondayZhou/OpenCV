import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

A0 = np.array([
    [0],
    [0],
    [1]
])
B0 = np.array([
    [0],
    [1],
    [1]
])
C0 = np.array([
    [1],
    [0],
    [1]
])
D0 = np.array([
    [1],
    [1],
    [1]
])

def get_rotation(angle):
    angle = np.radians(angle)
    return np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle),  np.cos(angle), 0],
        [0, 0, 1]
    ])
def get_translation(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])
def get_scale(s):
    return np.array([
        [s, 0, 0],
        [0, s, 0],
        [0, 0, 1]
    ])

R = get_rotation(50)
T = get_translation(-2, 1)
S = get_scale(2/3)

A1 = R @ T @ S @ A
B1 = R @ T @ S @ B
C1 = R @ T @ S @ C
D1 = R @ T @ S @ D

A2 = S @ T @ R @ A
B2 = S @ T @ R @ B
C2 = S @ T @ R @ C
D2 = S @ T @ R @ D

ms = [A0,B0,D0,C0]
for m in ms:
    plt.scatter (m[0],m[1],s=25, c='g')
    for i in range (len(ms)):
        if i in range(0,2):
            plt.plot([ms[i][0],ms[i+1][0]],[ms[i][1],ms[i+1][1]], c='g')
        else:
            plt.plot([ms[i][0],ms[i-3][0]],[ms[i][1],ms[i-3][1]], c='g')

ns = [A1,B1,D1,C1]
for n in ns:
    plt.scatter (n[0],n[1],s=25, c='r')
    for i in range (len(ns)):
        if i in range(0,2):
            plt.plot([ns[i][0],ns[i+1][0]],[ns[i][1],ns[i+1][1]], c='r')
        else:
            plt.plot([ns[i][0],ns[i-3][0]],[ns[i][1],ns[i-3][1]], c='r')
            
ps = [A2,B2,D2,C2]
for p in ps:
    plt.scatter (p[0],p[1],s=25, c='b')
    for i in range (len(ps)):
        if i in range(0,2):
            plt.plot([ps[i][0],ps[i+1][0]],[ps[i][1],ps[i+1][1]], c='b')
        else:
            plt.plot([ps[i][0],ps[i-3][0]],[ps[i][1],ps[i-3][1]], c='b')      

ax = plt.gca()

plt.axis("equal")
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

plt.show()
