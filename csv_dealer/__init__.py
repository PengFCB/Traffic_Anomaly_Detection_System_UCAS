import numpy as np
import os


def csv_deal_to_file(root_addr, no_total = 0, to_addr = None):
    #if not os.path.exists(root_addr+"/new"):
    #    os.mkdir(root_addr+"/new")
    n_mat_list = []
    file_list = os.listdir(root_addr)
    for file_name in file_list:
        if file_name.endswith("csv"):
            print("Dealing "+file_name)
            file_path = os.path.join(root_addr,file_name)
            mat = np.loadtxt(file_path,delimiter=",")[:,3:]
            n_mat = np.zeros(shape=(mat.shape[0], int(mat.shape[1] / 4)))
            for i in range(0, mat.shape[0]):
                for j in range(0, 96, 4):
                    n_mat[i, int(j / 4)] = mat[i, j] + mat[i, j + 1] + mat[i, j + 2] + mat[i, j + 3]
            if len(to_addr):
                np.savetxt(to_addr + "/n" + file_name, n_mat, delimiter=",", fmt="%f")
            n_mat_list.append(n_mat)
            print("Finish dealing "+file_name)

    total_mat = np.zeros(shape=n_mat_list[0].shape)
    if no_total == 0:
        print("Generating total.csv")
        for mat_item in n_mat_list:
            total_mat = total_mat + mat_item
        print("Finish generating total.csv")
        if len(to_addr):
            np.savetxt(to_addr + "/total.csv", total_mat, delimiter=",", fmt="%f")
    return n_mat_list, total_mat


def csv_deal(root_addr,no_total):
    if not os.path.exists(root_addr+"/new"):
        os.mkdir(root_addr+"/new")
    n_mat_list = []
    file_list = os.listdir(root_addr)
    for file_name in file_list:
        if file_name.endswith("csv"):
            print("Dealing "+file_name)
            file_path = os.path.join(root_addr,file_name)
            mat = np.loadtxt(file_path,delimiter=",")[:,3:]
            n_mat = np.zeros(shape=(mat.shape[0], int(mat.shape[1] / 4)))
            for i in range(0, mat.shape[0]):
                for j in range(0, 96, 4):
                    n_mat[i, int(j / 4)] = mat[i, j] + mat[i, j + 1] + mat[i, j + 2] + mat[i, j + 3]
            # np.savetxt(root_addr + "/new/n" + file_name, n_mat, delimiter=",", fmt="%d")
            n_mat_list.append(n_mat)
            print("Finish dealing "+file_name)

    total_mat = np.zeros(shape=n_mat_list[0].shape)
    if no_total == 0:
        print("Generating total.csv")
        for mat_item in n_mat_list:
            total_mat = total_mat + mat_item
        print("Finish generating total.csv")
    # np.savetxt(root_addr + "/new/total.csv", total_mat, delimiter=",", fmt="%d")
    return n_mat_list, total_mat


def mat_list_to_total(n_mat_list):
    total_mat = np.zeros(shape=n_mat_list[0].shape)
    print("Generating total.csv")
    for mat_item in n_mat_list:
        total_mat = total_mat + mat_item
    print("Finish generating total.csv")
    return total_mat


if __name__ == '__main__':
    csv_deal_to_file("/Users/liuyupeng/Desktop/data/traffic_csv/total/", 0)
    csv_deal_to_file("/Users/liuyupeng/Desktop/data/traffic_csv/test/", 1)
