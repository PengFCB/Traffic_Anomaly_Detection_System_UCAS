import cal_distance
import cal_f1
import csv_dealer
import get_gps
import get_Sit
import K_Means
import nmf_sklearn
import probability
import numpy as np
import os


def check_dic():
    path_list = ['final_test_cut', 'test_csv_cut', 'training_csv_cut', 'result', 'result1']

    for path in path_list:
        if not os.path.exists('./data/'+path):
            os.mkdir('./data/'+path)


def total():
    check_dic()

    csv_dealer.csv_deal_to_file("./data/training_csv/",no_total=1,to_addr="./data/training_csv_cut")
    csv_dealer.csv_deal_to_file('./data/test_csv/',no_total=1,to_addr='./data/test_csv_cut')
    csv_dealer.csv_deal_to_file('./data/final_test/',no_total=1,to_addr='./data/final_test_cut')

    mat_list = nmf_sklearn.generate_new_mat_list('./data/training_csv')
    total_mat = csv_dealer.mat_list_to_total(mat_list)
    np.savetxt("./data/total.csv", total_mat, delimiter=',', fmt="%f")
    w, h = nmf_sklearn.nmf_sklearn(3,total_mat)
    K_Means.k_means(w,250,new_file_addr='./data/class_list.txt')

    probability.run()
    get_Sit.run()
    cal_f1.run()


if __name__=='__main__':
    total()





