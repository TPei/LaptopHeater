__author__ = 'TPei'
from threading import Thread


class HeatingThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        print(self.name + " started")

    def run(self):
        i = 0
        while True:
            i += 1