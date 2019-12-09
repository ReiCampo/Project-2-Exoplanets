import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.sans-serif'] = 'stix'
from mpl_toolkits.mplot3d import Axes3D

def plotter(result, x,y,z, pos3,proj=3, tarr=[], point='n'):
    x1=result[0:,0]
    y1=result[0:,1]
    z1=result[0:,2]

    x2=result[0:,3]
    y2=result[0:,4]
    z2=result[0:,5]

    x3=result[0:,6]
    y3=result[0:,7]
    z3=result[0:,8]

    vx1=result[0:,9]
    vy1=result[0:,10]
    vz1=result[0:,11]

    vx2=result[0:,12]
    vy2=result[0:,13]
    vz2=result[0:,14]

    vx3=result[0:,15]
    vy3=result[0:,16]
    vz3=result[0:,17]

    if proj==0: #plots initial positions
        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(111)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Initial Positions, initial position of body 3=%.5f'%(pos3))
        if x==1:
            ax.plot(x1[0],y1[0], 'ro', label="Star 1", markersize=10)
        if y==1:
            ax.plot(x2[0],y2[0], 'ko', label="Planet")
        if z==1:
            ax.plot(x3[0],y3[0], 'bo',label="Star 2", markersize=10)
    
    if proj==2 and point=='n': #creates a 2D plot
        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(111)        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Motion of Bodies, initial position of body 3=%.5f'%(pos3))
        if x==1:
            ax.plot(x1,y1, 'r', label="Star 1")
        if y==1:
            ax.plot(x2,y2, 'k', label="Planet")
        if z==1:
            ax.plot(x3,y3, 'b',label="Star 2")
            
    if proj==2 and point=='y': #creates a 2D plot and makes points for stars
        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(111)        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Motion of Bodies, initial position of body 3=%.5f'%(pos3))
        if x==1:
            ax.plot(x1,y1, 'ro', label="Star 1", markersize=10)
        if y==1:
            ax.plot(x2,y2, 'k', label="Planet")
        if z==1:
            ax.plot(x3,y3, 'bo',label="Star 2", markersize=10)
            
    if proj==3: #creates a 3D plot
        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('Motion of Bodies, initial position of body 3=%.5f'%(pos3))
        if x==1:
            ax.plot(x1,y1,z1, 'b', label="Star 1")
        if y==1:
            ax.plot(x2,y2,z2, 'k', label="Planet")
        if z==1:
            ax.plot(x3,y3,z3, 'r',label="Star 2")
            
    if proj==4: #shows a velocity component of 1 body versus time
        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(111)
        ax.set_xlabel('time')
        ax.set_ylabel('velocity')
        ax.set_title('Velocity of Planet, initial position of body 3=%.5f'%(pos3))
        if x==1:
            ax.plot(tarr, vx2, 'k', label="Planet")
    
    plt.legend(loc='best')
    plt.grid()
    plt.show()