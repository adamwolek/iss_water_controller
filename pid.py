
class PID:


    def __init__(self, Kp, Ti, Td, init_value, period):
        self.Kp = Kp
        self.Ti = Ti
        self.Td = Td
        self.integral_helper = 0
        self.last_value = init_value
        self.period = period

    def proces(self, input):
        temp = self.Kp * input
        p_part = temp

        self.integral_helper = self.integral_helper + (temp * self.period) * 1/self.Ti
        i_part = self.integral_helper

        d_part = self.Td * ((temp - self.last_value) / self.period)

        result = p_part + i_part + d_part
        self.last_value = input
        return result
