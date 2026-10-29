# Duck Typing Polymorphism

class Car:
    def move(self):
        return "Car is driving smoothly on the road."


class Boat:
    def move(self):
        return "Boat is sailing gracefully through the water."


def start_moving(vehicle):
    print(vehicle.move())


if __name__ == "__main__":
    start_moving(Car())
    start_moving(Boat())
