#minimize.py
#temp_param[1,2,3]   actively fit parameters listed as elements 1,2 and 3
#temp_param[4,5,6]   static parameters
#temp_param[7,8,9]   static parameters
#Note that suffixes A,B and C below do NOT refer to parameter file peaks A,B,C
#Instead, A is "Active".  It is the peak being fit,while B and C are static

def center(velocity,intensity,temp_param,startline,endline,steplist):
    totallines=endline-startline+1
    sumtermsarray=[0];sumterms=[0]
    centerA=temp_param[0];coefficientA=temp_param[1];sigmaA=temp_param[2]
    centerB=temp_param[3];coefficientB=temp_param[4];sigmaB=temp_param[5]
    centerC=temp_param[6];coefficientC=temp_param[7];sigmaC=temp_param[8]
    step=steplist[0];max_passes=steplist[1]

    for i in range(max_passes):   #create an empty array for sumterms
        sumterms.append(0)
    for i in range(max_passes):
        gaussAA=[0];gaussBB=[0];gaussCC=[0];gaussTT=[0]
        pass_no=i+1
        for j in range(totallines):
            #calculate gaussian function
            exponentA=(-1*(velocity[j]-centerA)**2)/(2*sigmaA**2)
            gaussA=coefficientA*(2.718**exponentA)
            gaussAA.append(gaussA)
            exponentB=(-1*(velocity[j]-centerB)**2)/(2*sigmaB**2)
            gaussB=coefficientB*(2.718**exponentB)
            gaussBB.append(gaussB)
            exponentC=(-1*(velocity[j]-centerC)**2)/(2*sigmaC**2)
            gaussC=coefficientC*(2.718**exponentC)
            gaussCC.append(gaussC)
            gaussT=gaussA+gaussB+gaussC
            gaussTT.append(gaussT)
            #calculate least sum of squares
            termdiff=(intensity[j]-gaussT)**2
            sumtermsarray.append(termdiff)
        sumterms[i]=sum(sumtermsarray)
        if i==0:
            dir=+1 #start adding    
            centerA=centerA+dir*step
            sumtermsarray=[0]
            continue                        
        if i>0 and sumterms[i]==sumterms[i-1]:
            break              #No change. Leave the i loop and print results
        if i>0 and dir==1 and sumterms[i]<sumterms[i-1]:
            dir=+1 #keep adding
            centerA=centerA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==1 and sumterms[i]>sumterms[i-1]: 
            dir=-1 #start subtracting
            centerA=centerA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]        
            continue
        if i>0 and dir==-1 and sumterms[i]<sumterms[i-1]:
            dir=-1 #keep subtracting
            centerA=centerA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==-1 and sumterms[i]>sumterms[i-1]:
            dir=+1 #start adding
            centerA=centerA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]
            continue
    gaussAA[0]=gaussAA[1];gaussBB[0]=gaussBB[1];gaussCC[0]=gaussCC[1];gaussTT[0]=gaussTT[1]   
    #print("Number of passes: center ",pass_no)
    #print("sumterms ",int(sumterms[i]))
    #print("Center value ", int(centerA), " Hz")
    #print("parameters ", temp_param)
    return centerA,int(sumterms[i])

def coef(velocity,intensity,temp_param,startline,endline,steplist):
    totallines=endline-startline+1
    sumtermsarray=[0];sumterms=[0]
    centerA=temp_param[0];coefficientA=temp_param[1];sigmaA=temp_param[2]
    centerB=temp_param[3];coefficientB=temp_param[4];sigmaB=temp_param[5]
    centerC=temp_param[6];coefficientC=temp_param[7];sigmaC=temp_param[8]
    step=steplist[2]; max_passes=steplist[3]

    for i in range(max_passes): 
        sumterms.append(0)
    for i in range(max_passes):
        gaussAA=[0];gaussBB=[0];gaussCC=[0];gaussTT=[0]
        pass_no=i+1
        for j in range(totallines):
            #calculate gaussian function
            exponentA=(-1*(velocity[j]-centerA)**2)/(2*sigmaA**2)
            gaussA=coefficientA*(2.718**exponentA)
            gaussAA.append(gaussA)
            exponentB=(-1*(velocity[j]-centerB)**2)/(2*sigmaB**2)
            gaussB=coefficientB*(2.718**exponentB)
            gaussBB.append(gaussB)
            exponentC=(-1*(velocity[j]-centerC)**2)/(2*sigmaC**2)
            gaussC=coefficientC*(2.718**exponentC)
            gaussCC.append(gaussC)
            gaussT=gaussA+gaussB+gaussC
            gaussTT.append(gaussT)
            #calculate least sum of squares
            termdiff=(intensity[j]-gaussT)**2
            sumtermsarray.append(termdiff)
        sumterms[i]=sum(sumtermsarray)
        if i==0:
            dir=+1 #start adding    
            coefficientA=coefficientA+dir*step
            sumtermsarray=[0]
            continue                        
        if i>0 and sumterms[i]==sumterms[i-1]: #no change
            break              #leave the i loop and print results
        if i>0 and dir==1 and sumterms[i]<sumterms[i-1]:
            dir=+1 #keep adding
            coefficientA=coefficientA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==1 and sumterms[i]>sumterms[i-1]: 
            dir=-1 #start subtracting
            coefficientA=coefficientA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]        
            continue
        if i>0 and dir==-1 and sumterms[i]<sumterms[i-1]:
            dir=-1 #keep subtracting
            coefficientA=coefficientA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==-1 and sumterms[i]>sumterms[i-1]:
            dir=+1 #start adding
            coefficientA=coefficientA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]
            continue
    gaussAA[0]=gaussAA[1];gaussBB[0]=gaussBB[1];gaussCC[0]=gaussCC[1];gaussTT[0]=gaussTT[1]    
    #print("Number of passes: coefficient ",pass_no)
    #print("sumterms ",int(sumterms[i]))
    #print("Coefficient value ", coefficientA, " Kelvins")
    #print("parameters ", temp_param)
    return coefficientA,int(sumterms[i])

def sigma(velocity,intensity,temp_param,startline,endline,steplist):
    totallines=endline-startline+1
    sumtermsarray=[0];sumterms=[0]
    centerA=temp_param[0];coefficientA=temp_param[1];sigmaA=temp_param[2]
    centerB=temp_param[3];coefficientB=temp_param[4];sigmaB=temp_param[5]
    centerC=temp_param[6];coefficientC=temp_param[7];sigmaC=temp_param[8]
    step=steplist[4];max_passes=steplist[5]

    for i in range(max_passes): 
        sumterms.append(0)
    for i in range(max_passes):
        gaussAA=[0];gaussBB=[0];gaussCC=[0];gaussTT=[0]
        pass_no=i+1
        for j in range(totallines):
            #calculate gaussian function
            exponentA=(-1*(velocity[j]-centerA)**2)/(2*sigmaA**2)
            gaussA=coefficientA*(2.718**exponentA)
            gaussAA.append(gaussA)
            exponentB=(-1*(velocity[j]-centerB)**2)/(2*sigmaB**2)
            gaussB=coefficientB*(2.718**exponentB)
            gaussBB.append(gaussB)
            exponentC=(-1*(velocity[j]-centerC)**2)/(2*sigmaC**2)
            gaussC=coefficientC*(2.718**exponentC)
            gaussCC.append(gaussC)
            gaussT=gaussA+gaussB+gaussC
            gaussTT.append(gaussT)
            #calculate least sum of squares
            termdiff=(intensity[j]-gaussT)**2
            sumtermsarray.append(termdiff)
        sumterms[i]=sum(sumtermsarray)
        if i==0:
            dir=+1 #start adding    
            sigmaA=sigmaA+dir*step
            sumtermsarray=[0]
            continue                        
        if i>0 and sumterms[i]==sumterms[i-1]: #no change
            break              #leave the i loop and print results
        if i>0 and dir==1 and sumterms[i]<sumterms[i-1]:
            dir=+1 #keep adding
            sigmaA=sigmaA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==1 and sumterms[i]>sumterms[i-1]: 
            dir=-1 #start subtracting
            sigmaA=sigmaA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]        
            continue
        if i>0 and dir==-1 and sumterms[i]<sumterms[i-1]:
            dir=-1 #keep subtracting
            sigmaA=sigmaA+dir*step
            sumtermsarray=[0]
            continue
        if i>0 and dir==-1 and sumterms[i]>sumterms[i-1]:
            dir=+1 #start adding
            sigmaA=sigmaA+dir*step
            if i>1:
                break          #leave the i loop and print results
            sumtermsarray=[0]
            continue
    gaussAA[0]=gaussAA[1];gaussBB[0]=gaussBB[1];gaussCC[0]=gaussCC[1];gaussTT[0]=gaussTT[1] 
    #print("Number of passes: sigma ",pass_no)
    #print("sumterms ",int(sumterms[i]))
    #print("Sigma value ", int(sigmaA), " Hz")
    #print("parameters ", temp_param)
    return sigmaA,int(sumterms[i])
