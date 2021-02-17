
class FuzzySet:

    def __init__(self, center, name):
        self.center = center
        self.name = name
        self.left_boundary = center - 1
        self.right_boundary = center + 1

    def blur(self, sharp_value):
        if sharp_value == self.center:
            fuzzy_value = 1
        elif self.left_boundary < sharp_value < self.center:
            fuzzy_value = sharp_value - self.left_boundary
        elif self.center < sharp_value < self.right_boundary:
            fuzzy_value = (-1 * sharp_value) + self.right_boundary
        else:
            fuzzy_value = 0
        return fuzzy_value




class FirstFuzzySet:

    def __init__(self, center, name):
        self.center = center
        self.name = name
        self.right_boundary = center + 1

    def blur(self, sharp_value):
        if sharp_value <= self.center:
            fuzzy_value = 1
        elif self.center < sharp_value < self.right_boundary:
            fuzzy_value = (-1 * sharp_value) + self.right_boundary
        else:
            fuzzy_value = 0
        return fuzzy_value


class LastFuzzySet:

    def __init__(self, center, name):
        self.center = center
        self.name = name
        self.left_boundary = center - 1

    def blur(self, sharp_value):
        if self.left_boundary < sharp_value < self.center:
            fuzzy_value = sharp_value - self.left_boundary
        elif self.center <= sharp_value:
            fuzzy_value = 1
        else:
            fuzzy_value = 0
        return fuzzy_value




