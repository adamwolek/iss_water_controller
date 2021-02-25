
class PID:


    def __init__(self, Kp, Ti, Td, init_value):
        self.Kp = Kp
        self.Ti = Ti
        self.Td = Td
        self.integral_helper = 0
        self.last_value = init_value

    def proces(self, input, loop_time):
        temp = self.Kp * input
        p_part = temp

        self.integral_helper = self.integral_helper + (temp * loop_time) * 1/self.Ti
        if self.integral_helper > 5: self.integral_helper = 5
        elif self.integral_helper < -5: self.integral_helper = -5
        i_part = self.integral_helper

        d_part = self.Td * ((temp - self.last_value) / loop_time)

        result = p_part + i_part + d_part
        self.last_value = input
        return result

