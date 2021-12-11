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
    

def all_ntonic():
    Q_ntonic=[0]
    N_ntonic=[0]
    for Q in (range(1,2**12)):
        q=Q2q(Q)
        Q_circular = [q2Q(np.concatenate([q[x:],q[:x]])) for x in range(len(q))]
        sw=True
        for i in Q_ntonic:
            if i in Q_circular:
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
        print(i,"&",len(itonic),'& \\\\')
if __name__=="__main__":
    print(bin(5))
    q=Q2q(15)
    
    all_ntonic()
