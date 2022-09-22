

class Feature:

    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get(self):
        return {self.name: self.weight}

    def re_evaluate(self, weight):
        self.weight = weight

    def calculate(self, song_features):
        pass
