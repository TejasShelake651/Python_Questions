# Operator Overloading (+ and str)

class OverloadedNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return OverloadedNumber(self.value + other.value)

    def __str__(self):
        return f"OverloadedNumber({self.value})"


if __name__ == "__main__":
    n1 = OverloadedNumber(25)
    n2 = OverloadedNumber(75)
    n3 = n1 + n2
    print(f"{n1} + {n2} = {n3} (Result value: {n3.value})")
