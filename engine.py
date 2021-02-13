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
        self.currentRegulator = 'pid'

    def run(self):
        print ("Starting " + self.name)
        self.execute()
        print ("Exiting " + self.name)

    def execute(self):
        base_field = 1.5
        beta = 0.0035
        period = 0.2
        h_init = 0
        time_of_simulation = 3600
        number_of_samples = int(time_of_simulation / period)
        self.aim = 5
        self.pid = PID(0.5, 1000, 0.01, h_init, period)
        self.fuzzy = FuzzyRegulator()
        self.model = OneInOneOutModel(base_field, beta, period, h_init)

        x = [0]
        y = [h_init]
        while True:
            current_time = time.process_time()
            time.sleep(period)
            current_q = 0.005
            uchyb = self.aim - y[-1]

            steering_signal = self.pid.proces(uchyb)
            if steering_signal >= 0:
                self.inflow = self.pid.proces(uchyb)
            else:
                self.inflow = 0

            self.waterLevel = self.model.next_step(self.inflow)

            x.append(current_time / 3600)
            y.append(self.waterLevel)
            # print(self.waterLevel)


def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

