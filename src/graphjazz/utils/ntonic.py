import numpy as np
import tqdm
def Q2q(Q):
    """ q value from Q

    Args:
       Q: Q
    
    Returns:
       q (list of byte(Q))

    """
    q=[]
    for n in range(0,12):
        if Q & (1 << n) > 0:
            q.append(1)
        else:
            q.append(0)
    q.reverse()
    return np.array(q)

def q2Q(q):
    """ Q from q value

    Args:
       q: q
    
    Returns:
       Q 

    """
    orderlist=2**(np.array(range(0,12))[::-1])
    return np.sum(np.array(q)*orderlist)
    

def cshift(q,x):
    """cyclic shift

    Args:
       q: list (ndarray)
       x: shift value

    Returns:
       cyclic shifted list

    """
    return np.concatenate([q[x:],q[:x]])

def all_ntonic():
    """derive all of the N-tonic

    Returns:
       list of Q for N-tonics.

    """
    Q_ntonic=[0]
    N_ntonic=[0]
    for Q in (range(1,2**12)):
        q=Q2q(Q)
        Q_circular = [q2Q(cshift(q,x)) for x in range(len(q))] # list of circular of q
        sw=True
        for i in Q_ntonic: 
            if i in Q_circular: # checking duplication
                sw=False
        if sw:
            Q_ntonic.append(Q)
            N_ntonic.append(np.sum(Q2q(Q)))
    Q_ntonic=np.array(Q_ntonic)
    N_ntonic=np.array(N_ntonic)

    ntonic_Qlist=[]
    for i in range(0,13):
        mask=(N_ntonic==i)
        itonic=Q_ntonic[mask]
        ntonic_Qlist.append(itonic)
        #print(i,"&",len(itonic),'& \\\\')
        
    return ntonic_Qlist

def qinterval(q):
    """interval expression of q
    
    Args:
       q: q value
    
    Return:
       interval expression of q

    """
    kmask=(q==1)
    interval=np.zeros(12,dtype=int)
    qx=np.copy(q)
    for x in range(1,12):
        red=(qx-cshift(q,x))
        mask=(red==0)
        interval[mask]=x
        qx[mask]=13        
    return interval[kmask]

def splitindex(q):
    """splitting index of q
    
    Args:
       q: q value
    
    Return:
       spliting index

    """


    qint=qinterval(q)
    return 1/(np.sum(1/qint)/np.sum(q))

def write_all_ntonic():
    ATL=all_ntonic()
    for i,itonic in enumerate(ATL):
        print(str(i)+"-TONIC")
        for Q in itonic:
            q=Q2q(Q)
            qint=qinterval(q)
            print(Q,q,qint,splitindex(q))
            
if __name__=="__main__":
    print(bin(5))
    q=Q2q(285)
#    q=np.array([0,0,1,0,0,0,1,0,0,0,1,1])
    q=np.array([0,0,0,0,1,0,1,1,1,1,0,1])
    #    print(q,qinterval(q))
    # write_all_ntonic()

    ###
    import matplotlib.pyplot as plt
    cl=["","","","","C0","C1","C2"]
    ATL=all_ntonic()
    for j in [4,5,6]:
        sindex=[]
        for i,itonic in enumerate(ATL[j:j+1]):
            for Q in itonic:
                q=Q2q(Q)
                qint=qinterval(q)
                print(Q,q,qint,splitindex(q))
                sindex.append(splitindex(q))
            sindex=np.array(sindex)

        plt.hist(sindex,bins=20,color=cl[j],alpha=0.3,label=str(j)+"-tonic")

    plt.text(3.0,3,"dim",rotation=90, horizontalalignment="center", color="C0")
    plt.text(2.82,3,"m7, 6",rotation=90, horizontalalignment="center", color="C0")
    plt.text(2.1818,3,"M7",rotation=90, horizontalalignment="center", color="C0")

    plt.text(2.307,3,"major and minor pentatonics",rotation=90, horizontalalignment="center", color="C1")
    plt.text(1.5,3,"(traditional) hexatonic",rotation=90, horizontalalignment="center", color="C2")
    plt.text(2.0,3,"whole tone",rotation=90, horizontalalignment="center", color="C2")

    plt.xlabel("splitting index")
    plt.legend()
    plt.savefig("split.png")
    plt.show()
