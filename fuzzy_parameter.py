
class FuzzyParameter:

    def __init__(self, level_of_belonging, fuzzy_set):
        self.fuzzy_set = fuzzy_set
        self.level_of_belonging = level_of_belonging

    def getBelonging(self, sharpValue):
        blurred_value = self.fuzzy_set.blur(sharpValue)
        if blurred_value > self.level_of_belonging:
            blurred_value = self.level_of_belonging
        return blurred_value

    # def __init__(self, DU, SU, MU, Z, MD, SD, DD):
    #     self.DU = DU
    #     self.SU = SU
    #     self.MU = MU
    #     self.Z = Z
    #     self.MD = MD
    #     self.SD = SD
    #     self.DD = DD
