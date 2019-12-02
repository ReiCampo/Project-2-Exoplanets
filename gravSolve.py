import numpy as np
def df_Nbody(v0, t, M, ϵ = 0.0005):
    Nbody = len(M)
    half = Nbody * 3
    end = Nbody * 6
    pos = v0[0:half]
    velo = v0[half:end]

    x = np.array(pos[0::3])
    y = np.array(pos[1::3])
    z = np.array(pos[2::3])
    vx = np.array(velo[0::3])
    vy = np.array(velo[1::3])
    vz = np.array(velo[2::3]) 
    
    Dx = np.subtract.outer(x,x)
    Dy = np.subtract.outer(y,y)
    Dz = np.subtract.outer(z,z)
    
    #acc = dv/dt    
    bracketx = Dx/((ϵ**2+Dx**2+Dy**2+Dz**2)**(3/2))
    accex = -np.dot(bracketx, M)
    
    brackety = Dy/((ϵ**2+Dx**2+Dy**2+Dz**2)**(3/2))
    accey = -np.dot(brackety, M)
    
    bracketz = Dz/((ϵ**2+Dx**2+Dy**2+Dz**2)**(3/2))
    accez = -np.dot(bracketz, M)    
    
    dpos = np.zeros(3*Nbody)
    dvelo = np.zeros(3*Nbody)
    dpos[0::3] = velo[0::3]               
    dpos[1::3] = velo[1::3]
    dpos[2::3] = velo[2::3]
    dvelo[0::3] = accex[0::1]
    dvelo[1::3] = accey[0::1]
    dvelo[2::3] = accez[0::1]

    return np.array([dpos,dvelo]).flatten()