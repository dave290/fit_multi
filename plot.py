#plot.py

import collections
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def do_it(velocity,intensity,parameter,startline,endline,coordinate):
    gaussAA=[0];gaussBB=[0];gaussCC=[0];gaussDD=[0];gaussTT=[0]
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
        exponentD=(-1*(velocity[j]-parameter[9])**2)/(2*(parameter[11])**2)
        gaussD=(parameter[10])*(2.718**exponentD) 
        gaussDD.append(gaussD)
        gaussT=gaussA+gaussB+gaussC+gaussD
        gaussTT.append(gaussT)
    gauss_dequed=collections.deque(gaussTT)
    gauss_dequed.remove(0)
    gaussTTT=list(gauss_dequed)   

    #plot the data and the fit
    fig=plt.figure(figsize=(10,6))
    ax=plt.axes()
    ax.set_title("Intensity vs "+coordinate,fontsize=20)
    ax.set_xlabel(coordinate+" (km/s)", fontsize=18)
    ax.set_ylabel("Intensity (Kelvins)", fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    ax.set_xticks([-200,-150,-100,-50,0,50,100,150,200])
    #use ax.scatter to plot individual data points
    ax.scatter(velocity,intensity, c="red",s=80)
    #use plt.plot in order to plot a function with lines only
    plt.plot(velocity,gaussTTT,c="blue") 
    plt.show()


