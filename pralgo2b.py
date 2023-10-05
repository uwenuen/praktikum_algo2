print("Menghitung jarak antara dua titik di permukaan bumi!")
print()

lat1 = float(input("Masukkan latitude kota pertama = "))
long1 = float(input("Masukkan longitude kota pertama = "))
lat2 = float(input("Masukkan latitude kota kedua = "))
long2 = float(input("Masukkan longitude kota kedua = "))

import math

def haversine(lat1, long1, lat2, long2):
  
    lat1 = lat1 * 0.0174532925
    long1 = long1 * 0.0174532925
    lat2 = lat2 * 0.0174532925
    long2 = long2 * 0.0174532925

   
    delta_lat = lat2 - lat1
    delta_long = long2 - long1

  
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_long / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    R = 6371  
    distance = R * c

    return distance

jarak = haversine(lat1, long1, lat2, long2)
print(f'Jarak antara dua titik adalah {jarak:.2f} kilometer')


