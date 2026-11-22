# modul.py
from my_packages import operasi, geometri

print(operasi.kurang(10, 4))          # 6
print(geometri.luas_persegi(5))       # 25

from my_packages.operasi import kurang
from my_packages.geometri import luas_persegi

print(kurang(20, 7))                  # 13
print(luas_persegi(8))                # 64