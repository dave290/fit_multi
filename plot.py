#plot.py

import collections
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def do_it(velocity,intensity,parameter,startline,endline,coordinate):
    gaussAA=[0];gaussBB=[0];gaussCC=[0];gaussTT=[0]
    #calculate gaussian function
    totallines=endline-startline+1
    for j in range(totallines):
        exponentA=(-1*(velocity[j]-parameter[0])**2)/(2*(parameter[2])**2)
        gaussA=(parameter[1])*(2.718**exponentA)
        gaussAA.append(gaussA)
        exponentB=(-1*(velocity[j]-parameter[3])**2)/(2*(parameter[5])**2)
        gaussB=(parameter[4])*(2.718**exponentB)         
        gaussBB.append(gaussB)
        exponentC=(-1*(velocity[j]-parameter[6])**2)/(2*(parameter[8])**2)
        gaussC=(parameter[7])*(2.718**exponentC) 
        gaussCC.append(gaussC)
        gaussT=gaussA+gaussB+gaussC
        gaussTT.append(gaussT)
    gauss_dequed=collections.deque(gaussTT)
    gauss_dequed.remove(0)
    gaussTTT=list(gauss_dequed)   

    #plot the data
    fig=plt.figure(figsize=(10,6))
    ax=plt.axes()
    ax.set_title("Intensity_(Kelvins) vs "+coordinate)
    ax.set_xlabel(coordinate)
    ax.set_ylabel("Intensity_(K)")
    #ax.set_xlim(1419500000,1421500000)
    #ax.set_xticks([1419500000,1420000000,1420500000,1421000000,1421500000])
    ax.scatter(velocity,intensity, marker=".", c="red")
    ax.scatter(velocity,gaussTTT, marker=".", c="blue")
    plt.show()
