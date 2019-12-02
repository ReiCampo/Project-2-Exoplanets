######################################################################
# IMPORTANT: this code requires the 'celluloid' package:
# https://pypi.org/project/celluloid/
######################################################################

import matplotlib.pyplot as plt
from celluloid import Camera
from mpl_toolkits.mplot3d import Axes3D

######################################################################
# Take a set of arrays that characterize the gravitational evolution
# of a system, and make an animated GIF.
#
# Required inputs:
#   t = array of times
#   dat = list of (x,y,z) where each of x,y,z is an array with dimension
#         [number of time steps, number of stars]
#
# Optional inputs:
#   labels = list of axis lablels corresponding to the x,y,z arrays
#   Edat = list of arrays containing energies as a function of time
#   Elabels = list of labels for the energies
#   color = color to use for the orbit(s)
#   tail = number of time steps to show in a 'tail' behind each star
#   skip = set to something >1 if you don't want to show all stars
#   xmax = range of spatial plots
#   out = name of output file
######################################################################

def movie(t,body1,body2,body3,labels=[],Edat=[],Elabels=[],color='black',tail=0,skip=1,xmax=1.0,out='movie.gif', title=''):
    # determine how many position panels to use
    if len(body1)==2:
        x1 = body1[0]
        x2 = body2[0]
        x3 = body3[0]
        y1 = body1[1]
        y2 = body2[1]
        y3 = body3[1]
        
    elif len(body1)==3:
        x1 = body1[0]
        x2 = body2[0]
        x3 = body3[0]
        y1 = body1[1]
        y2 = body2[1]
        y3 = body3[1]
        z1 = body1[2]
        z2 = body2[2]
        z3 = body3[2]
    else:
        print('ERROR: length of dat array is not recognized')
        return

    # set up the plot structure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    camera = Camera(fig)
    ax.set_ylabel('y')
    ax.set_xlabel('x')
    ax.set_zlabel('z')
    ax.set_title(title)
    plt.grid()
    ax.scatter(x1[0],y1[0], z1[0], label="Body 1", color='blue')
    ax.scatter(x2[0],y2[0], z2[0], label="Body 2", color='black')
    ax.scatter(x3[0],y3[0], z3[0], label="Body 3", color='red')
    
    
    
    # loop over times
    for tindx in range(len(t)):
        thi = tindx+1
        tlo = max(0,thi-tail)
            
        for istar in range(0,len(x1),skip):
            ax.plot(x1[tlo:thi],y1[tlo:thi],z1[tlo:thi], color='blue')
            ax.scatter(x1[tindx],y1[tindx],z1[tindx],color='blue')                
                
            ax.plot(x2[tlo:thi],y2[tlo:thi],z2[tlo:thi], color='black')
            ax.scatter(x2[tindx],y2[tindx],z2[tindx],color='black')
                
            ax.plot(x3[tlo:thi],y3[tlo:thi],z3[tlo:thi], color='red')
            ax.scatter(x3[tindx],y3[tindx],z3[tindx],color='red')
            ax.legend()
        camera.snap()
    camera.animate().save(out)
