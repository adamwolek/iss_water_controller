import threading
import time

from fuzzy import FuzzyRegulator
from models import OneInOneOutModel
from pid import PID

exitFlag = 0

class Engine (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.waterLevel = 0
        self.inflow = 0
        self.currentRegulator = 'fuzzy'

    def run(self):
        print ("Starting " + self.name)
        self.execute()
        print ("Exiting " + self.name)

    def execute(self):
        base_field = 1.5
        beta = 0.0035
        period = 0.05
        h_init = 0
        self.aim = 5
        self.pid = PID(0.5, 1000, 0.01, h_init)
        self.fuzzy = FuzzyRegulator()
        self.model = OneInOneOutModel(base_field, beta, period, h_init)
        self.last_time = time.process_time()


        last_h = h_init
        while True:
            time.sleep(period)
            current_time = time.process_time()
            loop_time = current_time - self.last_time
            self.last_time = current_time

            uchyb = self.aim - last_h
            if (self.currentRegulator == 'pid'):
                steering_signal = self.pid.proces(uchyb, loop_time)
            else:
                steering_signal = self.fuzzy.proces(uchyb, loop_time)

            if steering_signal >= 0:
                self.inflow = steering_signal
            else:
                self.inflow = 0

            self.waterLevel = self.model.next_step(self.inflow)

            last_h = self.waterLevel
            # print(self.waterLevel)


def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

