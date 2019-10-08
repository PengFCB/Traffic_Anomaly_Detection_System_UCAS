import numpy as np
from sklearn.cluster import KMeans


def k_means_to_file(k, file_addr, new_file_addr):
    km = KMeans(n_clusters=k, n_jobs=-1)
    matW = np.loadtxt(file_addr, delimiter=",")
    result = km.fit_predict(matW)
    f = open(new_file_addr, "w")
    for i in range(0, len(result) - 1):
        f.write(np.str(result[i]))
        f.write(",")
        f.flush()
    f.write(np.str(result[len(result) - 1]))
    f.flush()
    f.close()


def k_means(mat, k, new_file_addr = None):
    km = KMeans(n_clusters=k, n_jobs=-1)
    result = km.fit_predict(mat)
    if len(new_file_addr):
        f = open(new_file_addr, "w")
        for i in range(0, len(result) - 1):
            f.write(np.str(result[i]))
            f.write(",")
            f.flush()
        f.write(np.str(result[len(result) - 1]))
        f.flush()
        f.close()
    return result


if __name__ == "__main__":
    k_means_to_file(250, "W.csv", "class_list.txt")