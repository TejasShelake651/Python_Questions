# Object Destructor (__del__)

class DestructorDemo:
    def __init__(self, name):
        self.name = name
        print(f"  [Init] Object '{self.name}' initialized.")

    def __del__(self):
        print(f"  [Destructor] Object '{self.name}' is destroyed.")


if __name__ == "__main__":
    print("Creating object:")
    obj = DestructorDemo("Alpha")
    print("Explicitly deleting object:")
    del obj
