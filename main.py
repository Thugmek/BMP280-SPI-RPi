import time
import sys

from bmp280.bmp280 import BMP280
from bmp280 import pressure_oversampling, temperature_oversampling, sampling_interval, filter

bmp = BMP280(1, 2)
bmp.configure(temperature_oversampling.TO_16, pressure_oversampling.PO_16, sampling_interval.SI_0_5, filter.FC_16)

print("Wait 3s before read base pressure")
time.sleep(3)
base_p = bmp.read()["press"]

print("Base pressure {:.2f}Pa".format(base_p))

while True:
    res = bmp.read()
    sys.stdout.write("\033[K")
    print("temperature: {:.2f}C,\tPressure: {:.2f}Pa".format(res['temp'], res['press']))
    sys.stdout.write("\033[K")
    print("Pressure dif: {:.2f}Pa".format(res['press']-base_p))
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    time.sleep(0.1)
