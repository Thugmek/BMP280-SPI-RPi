import time
import sys

from bmp280.bmp280 import BMP280
from bmp280 import pressure_oversampling, temperature_oversampling, sampling_interval, filter

# create BMP280 on /dev/spi1.2
bmp = BMP280(1, 2)

# configure oversampling, sampling speed and filter coefficient
# this also starts periodic sampling
bmp.configure(
    temperature_oversampling.TO_16,
    pressure_oversampling.PO_16,
    sampling_interval.SI_0_5,
    filter.FC_16
)

# filter coefficient 16 has little slow response, so we wait few seconds
print("Wait 3s before read base pressure...")
time.sleep(3)

# read BMP280 pressure
base_p = bmp.read()["press"]

print("Base pressure {:.2f}Pa".format(base_p))

while True:
    # read BMP280 pressure and temperature
    res = bmp.read()

    sys.stdout.write("\033[K")
    print("temperature: {:.2f}C,\tPressure: {:.2f}Pa".format(res['temp'], res['press']))
    sys.stdout.write("\033[K")
    print("Pressure dif: {:.2f}Pa".format(res['press']-base_p))
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")

    time.sleep(0.1)
