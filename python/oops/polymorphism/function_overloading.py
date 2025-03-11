class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

math_ops = MathOperations()
print(math_ops.add(1, 2))  # Output: 3
print(math_ops.add(1, 2, 3))  # Output: 6