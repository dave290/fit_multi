#fit_multi.py
#Fits data from a kel file with a function made up of up to 4 gaussian functions
#Format is intensity vs velocity

import collections        #needed for deque, remove, & rotate
import os                 #allows use of directory changing & reading commands
import read_datafilename  #reads name of .kel file
import read_datafile      #reads contents of a single .kel file
import read_parameters    #reads fit_parameters.txt
import modify_parameters  #modifies parameter list
import minimize           #fits center, coefficient & sigma vals
import plot               #plots data and final fit

#READ NAME AND TYPE OF .KEL FILE
A=read_datafilename.get_datafilename()
datafilename=A[0]; print("Data file",datafilename)
LDFN=len(datafilename)
newfilename=datafilename[0:LDFN-4]+".dat"
path=os.getcwd()+"/data/"
newfilename=path+newfilename
coordinate=A[1]; print("Coordinate",coordinate)

with open(newfilename, 'w') as g:
    g.write(A[0]);g.write("\n")
    g.write(coordinate);g.write("\n")

    #GET PARAMETERS AND FLAGS
    params_flags=read_parameters.get_params_flags()
    parameter=params_flags[0]
    print("Initial parameters")
    print(parameter[0:3])
    print(parameter[3:6])
    print(parameter[6:9])
    print(parameter[9:11])    
    g.write("Initial parameters: center, coefficient, sigma");g.write("\n")
    g.write("Peak A "+str(parameter[0:3]));g.write("\n")
    g.write("Peak B "+str(parameter[3:6]));g.write("\n")
    g.write("Peak C "+str(parameter[6:9]));g.write("\n")
    g.write("Peak D "+str(parameter[6:9]));g.write("\n")

    flag=params_flags[1]
    centerflagA=flag[0];coefflagA=flag[1];sigmaflagA=flag[2]
    centerflagB=flag[3];coefflagB=flag[4];sigmaflagB=flag[5]
    centerflagC=flag[6];coefflagC=flag[7];sigmaflagC=flag[8]
    centerflagD=flag[9];coefflagD=flag[10];sigmaflagD=flag[11]
    print("Flags: Peak A (x3), Peak B (x3), Peak C (x3), Peak D(x3)");print(flag)
    g.write("Flags: Peak A (x3), Peak B (x3), Peak C (x3)");g.write("\n")
    g.write("Flag A "+str(flag[0:3]));g.write("\n")
    g.write("Flag B "+str(flag[3:6]));g.write("\n")
    g.write("Flag C "+str(flag[6:9]));g.write("\n")
    g.write("Flag D "+str(flag[9:12]));g.write("\n")

    #GET ITERATIONS, STARTLINE AND ENDLINE
    total_iterations=read_parameters.get_iterations()
    print("Total Iterations ",total_iterations)
    g.write("Total Iterations ");g.write("\n")
    g.write(str(total_iterations));g.write("\n")
    limits=read_parameters.get_limits()
    lowerfitthreshold=limits[0];upperfitthreshold=limits[1]
    startline=limits[2];endline=limits[3]
    print("Lower fit threshold, upper fit threshold, startline, endline ")
    print(limits)
    g.write("Lower fit threshold, upper fit threshold, startline, endline ");g.write("\n")
    g.write(str(limits));g.write("\n")

    #GET STEPS AND MAX_PASSES
    steplist=read_parameters.get_step()
    print("Stepsize & Maximum Passes: Center (x2), Coefficient (x2), Sigma (x2)")
    print(steplist)
    g.write("Stepsize & Maximum Passes: Center (x2), Coefficient (x2), Sigma (x2)");g.write("\n")
    g.write(str(steplist));g.write("\n")

    #READ EXPERIMENTAL DATA
    velocity=read_datafile.velocity(startline,endline)
    intensity=read_datafile.intensity(startline,endline)

    #GENERATE PARAMETER FILES WITH ROTATED PEAKS FOR FITTING
    parameterA=modify_parameters.fitA(parameter)
    parameterAB=modify_parameters.fitAB(parameter)
    parameterABC=modify_parameters.fitABC(parameter)
    parameterABCD=modify_parameters.fitABCD(parameter)

    #EXECUTE ITERATIONS
    print("Differences")
    g.write("Differences");g.write("\n")
    Z=[99999]
    sumterms=0
    for iterations in range(total_iterations):
        for i in range(4):
            #Fit center***********************************************
            if i==0 and centerflagA==1: #fit peak A 
                centerA=minimize.center(velocity,intensity,parameterA,startline,endline,steplist)
                parameter[0]=centerA[0]
                sumterms=centerA[1]  
            if i==1 and centerflagB==1: #fit peak B
                centerB=minimize.center(velocity,intensity,parameterAB,startline,endline,steplist)
                parameter[3]=centerB[0]
                sumterms=centerB[1]
            if i==2 and centerflagC==1: #fit peak C
                centerC=minimize.center(velocity,intensity,parameterABC,startline,endline,steplist) 
                parameter[6]=centerC[0]
                sumterms=centerC[1]
            if i==3 and centerflagD==1: #fit peak D
                centerD=minimize.center(velocity,intensity,parameterABCD,startline,endline,steplist) 
                parameter[9]=centerD[0]
                sumterms=centerD[1]
            parameterA=modify_parameters.fitA(parameter)
            parameterAB=modify_parameters.fitAB(parameter) 
            parameterABC=modify_parameters.fitABC(parameter)
            parameterABCD=modify_parameters.fitABCD(parameter)

            #Fit coefficient******************************************
            if i==0 and coefflagA==1:
                coefA=minimize.coef(velocity,intensity,parameterA,startline,endline,steplist)
                parameter[1]=coefA[0]
                sumterms=coefA[1]
            if i==1 and coefflagB==1:
                coefB=minimize.coef(velocity,intensity,parameterAB,startline,endline,steplist)
                parameter[4]=coefB[0]
                sumterms=coefB[1]
            if i==2 and coefflagC==1:
                coefC=minimize.coef(velocity,intensity,parameterABC,startline,endline,steplist) 
                parameter[7]=coefC[0]
                sumterms=coefC[1]
            if i==3 and coefflagD==1:
                coefD=minimize.coef(velocity,intensity,parameterABCD,startline,endline,steplist) 
                parameter[10]=coefD[0]
                sumterms=coefD[1]
            parameterA=modify_parameters.fitA(parameter)
            parameterAB=modify_parameters.fitAB(parameter)
            parameterABC=modify_parameters.fitABC(parameter)
            parameterABCD=modify_parameters.fitABCD(parameter)

            #Fit sigma************************************************            
            if i==0 and sigmaflagA==1:
                sigmaA=minimize.sigma(velocity,intensity,parameterA,startline,endline,steplist)
                parameter[2]=sigmaA[0]
                sumterms=sigmaA[1]
            if i==1 and sigmaflagB==1:
                sigmaB=minimize.sigma(velocity,intensity,parameterAB,startline,endline,steplist)
                parameter[5]=sigmaB[0]
                sumterms=sigmaB[1]
            if i==2 and sigmaflagC==1:
                sigmaC=minimize.sigma(velocity,intensity,parameterABC,startline,endline,steplist) 
                parameter[8]=sigmaC[0]
                sumterms=sigmaC[1]
            if i==3 and sigmaflagD==1:
                sigmaD=minimize.sigma(velocity,intensity,parameterABCD,startline,endline,steplist) 
                parameter[11]=sigmaD[0]
                sumterms=sigmaD[1]
            parameterA=modify_parameters.fitA(parameter)
            parameterAB=modify_parameters.fitAB(parameter)
            parameterABC=modify_parameters.fitABC(parameter)
            parameterABCD=modify_parameters.fitABCD(parameter)

        Z.append(sumterms)
        if Z[iterations+1]<Z[iterations]:
            print(Z)
            g.write(str(Z));g.write("\n")  
        else:
            break
    print("ALL DONE!")
    print("Final parameters")
    print(parameter[0:3])
    print(parameter[3:6])
    print(parameter[6:9])
    print(parameter[9:12])    
    print("\n")
    g.write("Final parameters");g.write("\n")
    g.write("Peak A "+str(parameter[0:3]));g.write("\n")
    g.write("Peak B "+str(parameter[3:6]));g.write("\n")
    g.write("Peak C "+str(parameter[6:9]));g.write("\n")
    g.write("Peak D "+str(parameter[9:12]));g.write("\n")
g.closed
True

plot.do_it(velocity,intensity,parameter,startline,endline,coordinate)
exit()
