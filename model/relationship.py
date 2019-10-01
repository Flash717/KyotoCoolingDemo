
class relationship:

    def __init__(self, a, b):
        self.user_id_a = a
        self.user_id_b = b

    def __repr__(self):
        return '{0} -> {1}'.format(self.user_id_a, self.user_id_b)



