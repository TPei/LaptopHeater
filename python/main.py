from python.HeatingThread import HeatingThread

__author__ = 'TPei'
import psutil
cpu_count = psutil.cpu_count()

for i in range(0, cpu_count):
    HeatingThread().start()
