from setuptools import setup, find_packages

setup(
    name='bmp280-spi-RPi',
    version='0.0.1',
    install_requires=[
        'spidev'
    ],
    packages=find_packages(
        include=['bmp280']
    ),
    zip_safe=False
)
