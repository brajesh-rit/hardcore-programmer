class MathClass(object):
    def __init__(self, size, avg_gpa):
        self.size = size
        self.avg_gpa = avg_gpa
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, MathClass):
            return (self.size == other.size and self.avg_gpa == other.avg_gpa)
        return false

a = MathClass(20, 3.5)
b = MathClass(20, 3.5)
a==b # true or false? why?