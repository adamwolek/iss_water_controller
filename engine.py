import threading
import time
import math
from fuzzy import FuzzyRegulator
from models import OneInOneOutModel
from pid import PID

exitFlag = 0

class Engine (threading.Thread):
    def __init__(self, threadID, name, counter, lock):
        threading.Thread.__init__(self)
        self.lock = lock
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.waterLevel = 0
        self.inflow = 0
        self.currentRegulator = 'pid'
        self.auto_change_set = True

    def run(self):
        print ("Starting " + self.name)
        self.execute()
        print ("Exiting " + self.name)

    def execute(self):
        base_field = 1.5
        beta = 0.03
        period = 0.5
        h_init = 0
        self.aim = 5
        self.pid = PID(0.5, 1000, 0.01, h_init)
        self.fuzzy = FuzzyRegulator()
        self.model = OneInOneOutModel(base_field, beta, period, h_init)
        self.last_time = time.time()

        while True:
            time.sleep(period)
            with self.lock:

                current_time = time.time()
                loop_time = current_time - self.last_time
                self.last_time = current_time

                if self.auto_change_set:
                    self.aim = math.sin(2 * math.pi * current_time / 10) + 3

                uchyb = self.aim - self.waterLevel
                if (self.currentRegulator == 'pid'):
                    steering_signal = self.pid.proces(uchyb, loop_time)
                else:
                    steering_signal = self.fuzzy.proces(uchyb, loop_time)

                if steering_signal >= 0:
                    self.inflow = steering_signal
                else:
                    self.inflow = 0

                self.waterLevel = self.model.next_step(self.inflow)


def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

