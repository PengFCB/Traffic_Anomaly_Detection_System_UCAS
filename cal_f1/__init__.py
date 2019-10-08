import os
import numpy as np
import re

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from math import radians, cos, sin, asin, sqrt

def cal_distance_meter(lat1, lng1, lat2, lng2):

    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])

    d_lon = lng2-lng1

    d_lat = lat2-lat1

    a=sin(d_lat/2)**2 + cos(lat1) * cos(lat2) * sin(d_lon/2)**2

    dis=2*asin(sqrt(a))*6371*1000

    return dis

def judge_dis(dis1, dis2):
    return dis1 < 2000 or dis2 < 2000

def judge_time(t1, t2):
    return abs(int(t1)-int(t2)) <= 1

def get_lat_lon(id, lonlat_dict):
    values = lonlat_dict.get(int(id))

    if values == None:
        return 1.0, 1.0
    else:
        return values[0],values[1]

def cal_f1(filepath):
    print('------------------------------')
    print('dealing with file:', filepath)
    file = open(filepath,'r')
    our_error_lines = file.readlines()
    data_lines = open('./data/final_test/20111129.csv', 'r').readlines()
    test_line = open('./data/accident/n_11.29.csv', 'r',encoding="gb2312").readlines()

    lonlat_matrix = np.loadtxt(r'./data/map/beijing.csv', delimiter = '\t')
    lonlat_dict = {}
    for i in range(len(lonlat_matrix)):
        numbert = int(lonlat_matrix[i][0])
        lat = lonlat_matrix[i][1]
        lon = lonlat_matrix[i][2]
        lonlat_dict[numbert] = [lon,lat]

    TP1 = 0
    wrongset = set()

    for i in range(len(our_error_lines)):
        message1 = our_error_lines[i].split(',')
        road_id = int(message1[0])
        time1 = message1[1]
        message2 = data_lines[road_id].split(',')
        road_osm1 = message2[0]
        road_osm2 = message2[1]
        X1,Y1 = get_lat_lon(road_osm1, lonlat_dict)
        X2,Y2 = get_lat_lon(road_osm2, lonlat_dict)
        for j in range(len(test_line)):
            message3 = test_line[j].split(',')
            time2 = message3[0].split(':')[0]
            X0 = float(message3[2])
            Y0 = float(message3[3])
            distance1 = cal_distance_meter(X0,Y0,X1,Y1)
            distance2 = cal_distance_meter(X0,Y0,X2,Y2)
            if judge_dis(distance1,distance2) and judge_time(time1,time2):
                TP1 += 1
                wrongset.add(j)

    TP2 = len(wrongset)
    P = TP1 / len(our_error_lines)
    R = TP2 / len(test_line)
    F1 = 2*P*R/(P+R)
    return F1, TP1, TP2, P, R

def show_matrix(mt):
    ax=plt.subplot(111,projection='3d') 
    for i in range(len(mt)):
        for j in range(len(mt[0])):
            value = mt[i][j]       
            ax.scatter(i, j, mt[i][j] ,c="r")
    plt.show()

def get_b_s(filename):
    names = filename.split(',')
    return int(names[0][-1:]), int(names[1].split('.')[0])

def real_run():
    root_dir = './data/result1'
    filelist = os.listdir(root_dir)
    
    best_F1 = 0
    F1_matrix = [[0 for col in range(10)]for row in range(9)]

    for filename in filelist:
        filepath = os.path.join(root_dir, filename)
        F1, TP1, TP2, P, R = cal_f1(filepath)
        beta, suppose = get_b_s(filename)
        print('     beta = ', beta, 'sup = ', suppose)
        print('     F1:', F1)
        print('     TP1:', TP1)
        print('     TP2:', TP2)
        print('     P:', P)
        print('     R:', R)
        

        #save it to matrix 1-9 1-10 (9*10)
        
        F1_matrix[int(beta)-1][int(suppose)-1] = F1

        if F1 > best_F1:
            best_F1 = F1
            best_beta = beta
            best_suppose = suppose
            best_TP1 = TP1
            best_TP2 = TP2
            best_P = P
            best_R = R

    print('-----best result-----')    
    print('     beta:', best_beta, ' suppose:', best_suppose)
    print('     F1 =', best_F1)
    print('     TP1:', best_TP1)
    print('     TP2:', best_TP2)
    print('     P:', best_P)
    print('     R:', best_R)

    show_matrix(F1_matrix)
    return

def real_run_one():
    #root_dir = './result'
    #filelist = os.listdir(root_dir)
    root_dir = './data/result'
    filelist = os.listdir(root_dir)

    filename = filelist[0]
    filepath = os.path.join(root_dir, filename)
    
    best_F1 = 0
    #F1_matrix = [[0 for col in range(10)]for row in range(9)]

    #for filename in filelist:
        #filepath = os.path.join(root_dir, filename)
    F1, TP1, TP2, P, R = cal_f1(filepath)
    #beta, suppose = get_b_s(filename)
    beta, suppose =2,6
    print('     beta = ', beta, 'sup = ', suppose)
    print('     F1:', F1)
    print('     TP1:', TP1)
    print('     TP2:', TP2)
    print('     P:', P)
    print('     R:', R)
        

        #save it to matrix 1-9 1-10 (9*10)
        
    #F1_matrix[int(beta)-1][int(suppose)-1] = F1

    if F1 > best_F1:
        best_F1 = F1
        best_beta = beta
        best_suppose = suppose
        best_TP1 = TP1
        best_TP2 = TP2
        best_P = P
        best_R = R

    print('-----best result-----')    
    print('     beta:', best_beta, ' suppose:', best_suppose)
    print('     F1 =', best_F1)
    print('     TP1:', best_TP1)
    print('     TP2:', best_TP2)
    print('     P:', best_P)
    print('     R:', best_R)

    #show_matrix(F1_matrix)
    return


def run():
    real_flag = 2
    if real_flag == 1:
        real_run()
    elif real_flag == 2:
        real_run_one()
    else:
        #do some test here and set real_flag = False
        ax=plt.subplot(111,projection='3d') 
        ax.scatter(1, 2, 3 ,c="r")
        ax.scatter(5, 7, 9 ,c="r")
        plt.show()
    


#beta = 1
#suppose = 1

#for i in range(9):
    #for j in range(10):
        #print()
        #result = ...
        #np.savetxt("....../result" + '.' + beta + '.' + suppose +'.txt',......)
        #suppose += 1
    #beta += 1
