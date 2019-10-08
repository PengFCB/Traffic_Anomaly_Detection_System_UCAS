from math import radians, cos, sin, asin, sqrt


def cal_distance_meter(lat1, lng1, lat2, lng2):
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    d_lon = lng2-lng1
    d_lat = lat2-lat1
    a=sin(d_lat/2)**2 + cos(lat1) * cos(lat2) * sin(d_lon/2)**2
    dis=2*asin(sqrt(a))*6371*1000
    return dis


if __name__ == '__main__':
    print(cal_distance_meter(39, 116, 40, 116))