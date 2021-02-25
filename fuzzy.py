from base_of_regules import BaseOfRegules
from fuzzy_parameter import FuzzyParameter
from fuzzy_set import FuzzySet, FirstFuzzySet, LastFuzzySet
import numpy as np

class FuzzyRegulator:

    def __init__(self, ):
        self.base_of_regules = BaseOfRegules()
        self.sum_of_uchyb = 0
        self.fuzzy_sets = {
            "du": FirstFuzzySet(-3, "du"),
            "su": FuzzySet(-2, "su"),
            "mu": FuzzySet(-1, "mu"),
            "z": FuzzySet(0, "z"),
            "md": FuzzySet(1, "md"),
            "sd": FuzzySet(2, "sd"),
            "dd": LastFuzzySet(3, "dd")
        }


    def proces(self, uchyb, loop_time):

        if -0.5 < self.sum_of_uchyb + (loop_time * uchyb) < 0.5:
            self.sum_of_uchyb += (loop_time * uchyb)

        # Rozmywanie
        fuzzy_e_values = self.blur(uchyb)
        fuzzy_se_values = self.blur(self.sum_of_uchyb)

        # Wnioskowanie
        active_regules = []
        for e in fuzzy_e_values:
            for se in fuzzy_se_values:
                active_regules.append(self.apply_regule(e, se))

        #Wyostrzanie

        # control = self.midleOfMaxima(active_regules)

        control = self.centerOfWeight(active_regules)

        return control / 5

    def centerOfWeight(self, active_regules):
        nominator = 0
        denominator = 0
        width_of_micro_square = 0.01
        for y in np.arange(-6, 6, width_of_micro_square):
            belongings = []
            for parameter in active_regules:
                belongings.append(parameter.getBelonging(y))
            u = max(belongings)
            nominator += y * u * width_of_micro_square
            denominator += u * width_of_micro_square
        yc = nominator / denominator
        return yc

    def midleOfMaxima(self, active_regules):
        levels = []
        for parameter in active_regules:
            levels.append(parameter.level_of_belonging)
        max_level = max(levels)
        max_parameters = []
        for parameter in active_regules:
            if parameter.level_of_belonging == max_level:
                max_parameters.append(parameter)
        middle_of_maxima = self.calculateMiddleOfMaxima(max_parameters)
        return middle_of_maxima

    def calculateMiddleOfMaxima(self, max_parameters):
        max_parameters.sort(key=lambda fuzzy_parameter: fuzzy_parameter.fuzzy_set.center)
        first_set = max_parameters[0]
        last_set = max_parameters[-1]
        middle_of_maxima = (first_set.fuzzy_set.center + last_set.fuzzy_set.center) / 2
        return middle_of_maxima

    def apply_regule(self, fuzzy_e, fuzzy_se):
        active_regule_name = self.base_of_regules \
            .data['e_' + str(fuzzy_e.fuzzy_set.name)]['se_' + str(fuzzy_se.fuzzy_set.name)]
        active_regule_value = min(fuzzy_e.level_of_belonging, fuzzy_se.level_of_belonging)
        return FuzzyParameter(active_regule_value, self.fuzzy_sets[active_regule_name.lower()])

    def blur(self, sharp_value):
        non_zero_fuzzy_parameters = []
        for fuzzy_set in self.fuzzy_sets.values():
            value = fuzzy_set.blur(sharp_value)
            if value > 0:
                non_zero_fuzzy_parameters.append(FuzzyParameter(value, fuzzy_set))
        return non_zero_fuzzy_parameters

