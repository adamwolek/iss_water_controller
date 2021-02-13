



class FuzzyRegulator:

    def __init__(self, ):
        e_du = {"ce_du": "BDU", "ce_su": "BDU", "ce_mu": "BDU", "ce_z": "DU", "ce_md": "SU", "ce_sd": "MU", "ce_dd": "Z"}
        e_su = {"ce_du": "BDU", "ce_su": "BDU", "ce_mu": "DU", "ce_z": "SU", "ce_md": "MU", "ce_sd": "Z", "ce_dd": "MD"}
        e_mu = {"ce_du": "BDU", "ce_su": "DU", "ce_mu": "SU", "ce_z": "MU", "ce_md": "Z", "ce_sd": "MD", "ce_dd": "SD"}
        e_z = {"ce_du": "DU", "ce_su": "SU", "ce_mu": "MU", "ce_z": "Z", "ce_md": "MD", "ce_sd": "SD", "ce_dd": "DD"}
        e_md = {"ce_du": "", "ce_su": "", "ce_mu": "", "ce_z": "", "ce_md": "", "ce_sd": "", "ce_dd": ""}
        e_sd = {"ce_du": "", "ce_su": "", "ce_mu": "", "ce_z": "", "ce_md": "", "ce_sd": "", "ce_dd": ""}
        e_dd = {"ce_du": "", "ce_su": "", "ce_mu": "", "ce_z": "", "ce_md": "", "ce_sd": "", "ce_dd": ""}

    # def blur(self, input):


    def proces(self, input):
        temp = self.Kp * input
        p_part = temp

        self.integral_helper = self.integral_helper + (temp * self.period) * 1 / self.Ti
        i_part = self.integral_helper

        d_part = self.Td * ((temp - self.last_value) / self.period)

        result = p_part + i_part + d_part
        self.last_value = input
        return result