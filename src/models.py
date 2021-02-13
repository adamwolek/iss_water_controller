import math


class OneInOneOutModel:

    def __init__(self, base_field, beta, period, h_init):
        self.base_field = base_field
        self.beta = beta
        self.period = period
        self.h_history = [h_init]

    def next_step(self, current_q):
        last_h = self.h_history[-1]
        result = 1/self.base_field * (-self.beta * math.sqrt(last_h) + current_q) * self.period + last_h
        self.h_history.append(result)
        return result




class MixingInputsModel:

    def __init__(self, base_field, beta, period, v_init, c_init):
        self.base_field = base_field
        self.beta = beta
        self.period = period
        self.v_history = [v_init]
        self.c_history = [c_init]

    def next_step(self, q1, q2, c1, c2):
        odplyw = 0
        last_v = self.v_history[-1]
        last_c = self.c_history[-1]
        next_v = (q1 + q2 - odplyw) * self.period + last_v
        next_c = (1/last_v) * (q1 * (c1-last_c) + q2 * (c2 - last_c)) * self.period + last_c

        next_v = 1
        next_c = 1

        self.last_v.append(next_v)
        self.last_c.append(next_c)
        return next_c
