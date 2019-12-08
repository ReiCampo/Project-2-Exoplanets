def plotter(x, y, z, proj = 3):
    
    x1 = result2[0:,0]
    y1 = result2[0:,1]
    z1 = result2[0:,2]

    x2 = result2[0:,3]
    y2 = result2[0:,4]
    z2 = result2[0:,5]

    x3 = result2[0:,6]
    y3 = result2[0:,7]
    z3 = result2[0:,8]

    vx1 = result2[0:,9]
    vy1 = result2[0:,10]
    vz1 = result2[0:,11]

    vx2 = result2[0:,12]
    vy2 = result2[0:,13]
    vz2 = result2[0:,14]

    vx3 = result2[0:,15]
    vy3 = result2[0:,16]
    vz3 = result2[0:,17]
    
    
    if proj == 2:
        fig = plt.figure(figsize = (7, 7))
        ax = fig.add_subplot(111)
        if x == 1:
            ax.plot(x1,y1, 'b', label = "Body 1")
        if y == 1:
            ax.plot(x2,y2, 'k', label = "Body 2")
        if z == 1:
            ax.plot(x3,y3, 'r',label = "Body 3")
    if proj == 3:
        fig = plt.figure(figsize = (7, 7))
        ax = fig.add_subplot(111, projection = '3d')
        if x == 1:
            ax.plot(x1, y1, z1, 'b', label = "Body 1")
        if y == 1:
            ax.plot(x2, y2, z2, 'k', label = "Body 2")
        if z == 1:
            ax.plot(x3, y3, z3, 'r', label = "Body 3")
    plt.legend(loc = 'best')
    plt.grid()
    plt.show()