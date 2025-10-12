# main.py
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # Create instances of different shapes
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Demonstrate polymorphism
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
