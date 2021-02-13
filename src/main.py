import matplotlib.pyplot as plt
from src.models import OneInOneOutModel
from src.pid import PID

base_field = 1.5
beta = 0.0035
period = 1
h_init = 0
time_of_simulation = 3600
number_of_samples = int(time_of_simulation / period)
aim = 5

pid = PID(0.1, 100000, 0.01, h_init, period)
model = OneInOneOutModel(base_field, beta, period, h_init)

x = [0]
y = [h_init]
for current_sample in range(0, number_of_samples):
    current_time = current_sample * period
    current_q = 0.005
    uchyb = aim - y[-1]

    sterowanie = pid.proces(uchyb)
    next_h = model.next_step(sterowanie)

    x.append(current_time / 3600)
    y.append(next_h)
    print(next_h)

plt.plot(x, y)
plt.show()

