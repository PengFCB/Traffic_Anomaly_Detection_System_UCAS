import math
import os
import numpy as np




def open_file(path):
    return open(path, 'r')

def close_file(f):
    f.close()


def get_road(n29data):
    road_count = len(n29data)
    hour = len(n29data[0])
    return road_count,hour

def get_class(_list_):
    road_no = len(_list_)
    return road_no

def get_p(_list_):
    class_V = len(_list_)
    delta = len(_list_[0])
    return class_V,delta

def get_road_list():
    n29data = np.loadtxt(filepath1, delimiter=',')
    return n29data

def get_poison_probability(lam, k):
    #factorial_list = get_fact_list()
    sum = 0
    c = math.exp(-lam)
    last_value = c
    for i in range(0, k):
        try:
            if i == 0:
                cur_value = last_value
            else:
                cur_value = last_value * lam / i
            sum += cur_value
            last_value = cur_value
        except:
            print(i,'error')
            break

    return 1 - sum

def check(beta,supposeV,n29data,classdata,p1,p2):
    road_count,hour = get_road(n29data)
    result=[]
    for i in range(road_count):
        #print(i)
        for j in range(hour):
            k = int(n29data[i,j])
            x = int (classdata[i])
            lam1 = p1[x,j]
            lam2 = p2[x,j]
            p1V = get_poison_probability(lam1, k)
            p2V = get_poison_probability(lam2, k)
            #print('p1v', p1V)
            #print('p2v', p2V)
            p = beta*p1V+(1-beta)*p2V
            #print('P:', p)
            if supposeV>p:
                result.append([i,j])

    return result



def run():

    filepath1 = './data/n29.csv'
    n29data = np.loadtxt(filepath1, delimiter=',')

    filepath2 = './data/class_list.txt'
    classdata = np.loadtxt(filepath2, delimiter= ',')

    filepath3 = './data/prior_poison_matrix.txt'
    p1data = np.loadtxt(filepath3, delimiter=' ')

    filepath4 = './data/current_poison_matrix.txt'
    p2data = np.loadtxt(filepath4, delimiter=' ')


    beta = 2  #You can test beta from 0.1 to 0.9
    #for j in range(9):
    suppose = 6
     #   for i in range(10):
      #      print('time',i,'suppose =',suppose)
    result = check(beta/10, suppose/100000, n29data, classdata, p1data, p2data)   #10000-1000000
    np.savetxt('./data/result/finalresultfinal.txt', result, delimiter=',', fmt='%d')
    #np.savetxt('C:/6/finalresult' + str(beta) + str(',') + str(suppose) +  '.txt', result, delimiter=',', fmt='%d')
     #       suppose += 1
      #  beta += 1
