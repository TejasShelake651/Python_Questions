# Access Specifiers & Name Mangling

class AccessSpecifierBase:
    def __init__(self, name, roll_no, marks):
        self.name = name              # Public
        self._roll_no = roll_no       # Protected
        self.__marks = marks          # Private

    def display(self):
        print(f"Public name: {self.name}")
        print(f"Protected _roll_no: {self._roll_no}")
        print(f"Private __marks: {self.__marks}")


class AccessSpecifierDerived(AccessSpecifierBase):
    def test_access(self):
        print("Derived accessing public:", self.name)
        print("Derived accessing protected:", self._roll_no)
        # Accessing private attribute via Python Name Mangling: _ClassName__attribute
        print("Derived accessing private via mangled name:", self._AccessSpecifierBase__marks)


if __name__ == "__main__":
    acc_obj = AccessSpecifierDerived("Viraj", 24, 95)
    acc_obj.display()
    acc_obj.test_access()
