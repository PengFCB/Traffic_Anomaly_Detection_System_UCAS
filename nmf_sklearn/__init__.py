from sklearn.decomposition import NMF
import numpy as np
import matplotlib.pyplot as plt
import os


def nmf_sklearn_to_file(n,file_addr,outW_addr,outH_addr):
    model = NMF(n_components=n)
    mat = np.loadtxt(file_addr,delimiter=",")
    W=model.fit_transform(mat)
    H=model.components_
    np.savetxt(outW_addr,W,delimiter=',')
    np.savetxt(outH_addr,H,delimiter=',')


def nmf_sklearn(n,mat):
    model = NMF(n_components=n)
    W=model.fit_transform(mat)
    H=model.components_
    return W,H


def generate_new_mat_list(root_addr):
    file_list = os.listdir(root_addr)
    mat_list = []
    new_mat_list = []
    for file_name in file_list:
        if file_name.endswith("csv"):
            print("Dealing "+file_name)
            file_path = os.path.join(root_addr,file_name)
            mat = np.loadtxt(file_path,delimiter=",")[:,3:]
        mat_list.append(mat)
    for i in range (len(mat_list)):
        W, H = nmf_sklearn(3, mat_list[i])
        new_mat_list.append(np.dot(W,H))
    return new_mat_list


if __name__=='__main__':
    model = NMF(n_components=3)
    mat=np.loadtxt("/Users/liuyupeng/Desktop/data/traffic_csv/total.csv",delimiter=',')
    W=model.fit_transform(mat)
    H=model.components_
    np.savetxt("/Users/liuyupeng/Desktop/data/traffic_csv/totalW.csv",W,delimiter=',')
    np.savetxt("/Users/liuyupeng/Desktop/data/traffic_csv/totalH.csv", H, delimiter=',')

    x = []
    y1 = []
    y2 = []
    y3 = []

    for i in range(24):
        x.append(i)
        y1.append(H[0, i])
        y2.append(H[1, i])
        y3.append(H[2, i])

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.plot()
    plt.show()