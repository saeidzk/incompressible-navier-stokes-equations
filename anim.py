import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Anim:
    def my_animation(self,solution, dt, Y, Z):

        ####################   Animation   ####################
        fig = plt.figure(figsize=(6.1,5),facecolor='w')
        images=[]
        lev=np.linspace(-1,1,50)
        i=0
        t=0

        for sol in solution:
            if i%50==0: # plots contour each 50 time steps
                im=plt.contourf(Y,Z,sol[:], levels=lev,vmax=1.0,vmin=-1.0)
                images.append(im.collections)
            i+=1
            t += dt

        cbar = plt.colorbar()
        plt.title('Velocity Contour')
        #plt.clim(-1,1)
        cbar.set_ticks(np.linspace(-1,1,50))

        ani = animation.ArtistAnimation (fig, images, interval=35, blit= True, repeat_delay=50)

        plt.show()