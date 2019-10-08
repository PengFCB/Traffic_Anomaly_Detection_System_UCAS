#input : list1([1,2,5,1,1,3,6,1,55,...])
import math
import os
import numpy as np


def get_prior_data_matrix(_list_):
    road_count = len(_list_)
    k = 250
    t = 24

    data_matrix = [[[] for i in range(t)] for j in range(k)]
    #for load all txt
    root_path = './data/training_csv_cut'
    root_path1 = './data/test_csv_cut'
    filelist = os.listdir(root_path)
    filelist1 = os.listdir(root_path1)

    loop_count = 1
    for filename in filelist:
        filepath = os.path.join(root_path, filename)
        data = np.loadtxt(filepath, delimiter = ',')
        print('open file', loop_count)
        for i in range(road_count):
            #the i point is in group list[i]
            group_number = int(_list_[i])
            #put this data into data_matrix[group_number][...]
            for j in range(t):
                data_matrix[group_number][j].append(data[i,j])
        loop_count += 1
    for filename in filelist1:
        filepath = os.path.join(root_path1, filename)
        data = np.loadtxt(filepath, delimiter=',')
        print('open file', loop_count)
        for i in range(road_count):
            # the i point is in group list[i]
            group_number = int(_list_[i])
            # put this data into data_matrix[group_number][...]
            for j in range(t):
                data_matrix[group_number][j].append(data[i, j])
        loop_count += 1
    return data_matrix

def get_current_data_matrix(_list_):
    road_count = len(_list_)
    k = 250
    t = 24

    data_matrix = [[[] for i in range(t)] for j in range(k)]
    root_path = './data/final_test_cut'
    filelist = os.listdir(root_path)

    for filename in filelist:
        filepath = os.path.join(root_path, filename)
        data = np.loadtxt(filepath, delimiter = ',')
        for i in range(road_count):
            #the i point is in group list[i]
            group_number = int(_list_[i])
            #put this data into data_matrix[group_number][...]
            for j in range(t):
                data_matrix[group_number][j].append(data[i,j])
    return data_matrix


def get_poisson_matrix(data_matrix):
    m = len(data_matrix)
    n = len(data_matrix[0])
    poisson_matrix = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            _list_ = data_matrix[i][j]
            sum = 0
            for k in range(len(_list_)):
                sum += _list_[k]
            ave = sum/len(_list_)
            poisson_matrix[i][j] = ave
    return poisson_matrix

def get_normal_matrix(data_matrix):
    m = len(data_matrix)
    n = len(data_matrix[0])
    normal_matrix = [[[] for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            _list_ = data_matrix[i][j]
            sum = 0
            std = 0
            for k in range(len(_list_)):
                sum += _list_[k]
            ave = sum/len(_list_)
            for k in range(len(_list_)):
                std += (_list_[k] - ave)**2
            std /= len(_list_)
            std = np.sqrt(std)
            normal_matrix[i][j].append(ave)
            normal_matrix[i][j].append(std)
    return normal_matrix

def get_class_list():
    _list_ = np.loadtxt(r'./data/class_list.txt', delimiter = ',')
    return _list_

def train_prior_probability_model():
    _list_ = get_class_list()
    data_matrix = get_prior_data_matrix(_list_)
    #if want data of Roadi at time t:
    #-----data_matrix[i][k]----
    poisson_matrix = get_poisson_matrix(data_matrix)
    normal_matrix = get_normal_matrix(data_matrix)

    np_poisson_matrix = np.matrix(poisson_matrix)
    np.savetxt(r'./data/prior_poison_matrix.txt', np_poisson_matrix)

def train_current_probability_model():
    _list_ = get_class_list()
    data_matrix = get_current_data_matrix(_list_)

    poisson_matrix = get_poisson_matrix(data_matrix)

    np_poisson_matrix = np.matrix(poisson_matrix)
    np.savetxt(r'./data/current_poison_matrix.txt', np_poisson_matrix)


def run():
    train_prior_probability_model()
    train_current_probability_model()


if __name__ == '__main__':

    train_prior_probability_model()
    train_current_probability_model()
