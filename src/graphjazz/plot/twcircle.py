import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

def ntonic(ax,p,rcircle=0.17,rad=1.0,oncolor="black",offcolor="white",linecolor="black"):
    """Plot N-tonic on a 12 circle
    
    Args:
       ax: axis
       p: p-value
    
    """
    delta=np.pi/6.0
    for i,peach in enumerate(p):
        theta=delta*(i-1)+np.pi/2.0
        x=rad*np.cos(theta)
        y=rad*np.sin(theta)
        print(x,y)
        if peach==1 or peach==True:
            c=Circle(xy=(x, y), radius=rcircle, facecolor=oncolor,edgecolor=linecolor)
        else:
            c=Circle(xy=(x, y), radius=rcircle, facecolor=offcolor,edgecolor=linecolor)
            
        ax.add_patch(c)


def set_twcircle(ax):
    """Set axis for 12 circle

    Args:
       ax: axis

    """
    ax.plot(0,0,".",color="white")
    plt.xlim(-1.2,1.2)
    plt.ylim(-1.2,1.2)
    ax.axis("off")
    ax.set_aspect('equal')


    
if __name__=="__main__":
    p=[0,1,1,0,1,0,0,0,0,1,0,1]
    fig=plt.figure()
    ax = plt.axes()
    set_twcircle(ax)
    ntonic(ax,p)
    plt.show()
