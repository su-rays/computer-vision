class MagicMethodsDemo:
    # Initialization and Representation
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MagicMethodsDemo({self.value})"

    def __str__(self):
        return f"MagicMethodsDemo with value: {self.value}"

    # Comparison methods
    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    # Arithmetic operations
    def __add__(self, other):
        return MagicMethodsDemo(self.value + other.value)

    def __sub__(self, other):
        return MagicMethodsDemo(self.value - other.value)

    def __mul__(self, other):
        return MagicMethodsDemo(self.value * other.value)

    def __truediv__(self, other):
        return MagicMethodsDemo(self.value / other.value)

    def __floordiv__(self, other):
        return MagicMethodsDemo(self.value // other.value)

    def __mod__(self, other):
        return MagicMethodsDemo(self.value % other.value)

    def __pow__(self, other):
        return MagicMethodsDemo(self.value ** other.value)

    # Unary operations
    def __neg__(self):
        return MagicMethodsDemo(-self.value)

    def __pos__(self):
        return MagicMethodsDemo(+self.value)

    def __abs__(self):
        return MagicMethodsDemo(abs(self.value))

    # Type conversion
    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __bool__(self):
        return bool(self.value)

    # Container methods
    def __len__(self):
        return len(str(self.value))

    def __getitem__(self, key):
        return str(self.value)[key]

    def __setitem__(self, key, value):
        temp = list(str(self.value))
        temp[key] = str(value)
        self.value = int("".join(temp))

    def __contains__(self, item):
        return str(item) in str(self.value)

    # Context management
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

    # Callable object
    def __call__(self, *args, **kwargs):
        print(f"Called with args: {args}, kwargs: {kwargs}")

# Example usage
if __name__ == "__main__":
    a = MagicMethodsDemo(10)
    b = MagicMethodsDemo(20)

    # Representation
    print(repr(a))  # MagicMethodsDemo(10)
    print(str(a))   # MagicMethodsDemo with value: 10

    # Comparison
    print(a == b)   # False
    print(a < b)    # True

    # Arithmetic operations
    c = a + b
    print(c.value)  # 30

    # Unary operations
    d = -a
    print(d.value)  # -10

    # Type conversion
    print(int(a))   # 10
    print(float(a)) # 10.0
    print(bool(a))  # True

    # Container methods
    print(len(a))   # 2
    print(a[1])    # 0
    print(1 in a)   # True

    # Context management
    with a as context:
        print(context.value)  # 10

    # Callable object
    a(1, 2, key="value")  # Called with args: (1, 2), kwargs: {'key': 'value'}