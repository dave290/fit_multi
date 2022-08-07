#modify_parameters.py
import collections

def fitA(parameter):
    tem_par=[0]
    for j in range(8):
        tem_par.append(0)
    tem_par[0]=parameter[0]
    tem_par[1]=parameter[1]
    tem_par[2]=parameter[2]
    tem_par[3]=parameter[3]
    tem_par[4]=parameter[4]
    tem_par[5]=parameter[5]
    tem_par[6]=parameter[6]
    tem_par[7]=parameter[7]
    tem_par[8]=parameter[8]
    return tem_par

def fitAB(parameter):
    tem_par=[0]
    for j in range(8):
        tem_par.append(0)
    tem_par[0]=parameter[3]
    tem_par[1]=parameter[4]
    tem_par[2]=parameter[5]
    tem_par[3]=parameter[0]
    tem_par[4]=parameter[1]
    tem_par[5]=parameter[2]
    tem_par[6]=parameter[6]
    tem_par[7]=parameter[7]
    tem_par[8]=parameter[8]
    return tem_par

def fitABC(parameter):
    tem_par=[0]
    for j in range(8):
        tem_par.append(0)
    tem_par[0]=parameter[6]
    tem_par[1]=parameter[7]
    tem_par[2]=parameter[8]
    tem_par[3]=parameter[0]
    tem_par[4]=parameter[1]
    tem_par[5]=parameter[2]
    tem_par[6]=parameter[3]
    tem_par[7]=parameter[4]
    tem_par[8]=parameter[5]
    return tem_par

    