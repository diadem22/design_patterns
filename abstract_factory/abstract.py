class ShapeFactory:
    def create_circle(self):
        pass

    def create_square(self):
        pass

class RedShapeFactory(ShapeFactory):
    def create_circle(self):
        return RedCircle()

    def create_square(self):
        return RedSquare()

class BlueShapeFactory(ShapeFactory):
    def create_circle(self):
        return BlueCircle()

    def create_square(self):
        return BlueSquare()

class Shape:
    def draw(self):
        pass

class RedCircle(Shape):
    def draw(self):
        return "Drawing a red circle"

class RedSquare(Shape):
    def draw(self):
        return "Drawing a red square"

class BlueCircle(Shape):
    def draw(self):
        return "Drawing a blue circle"

class BlueSquare(Shape):
    def draw(self):
        return "Drawing a blue square"

def create_and_draw_shapes(factory):
    circle = factory.create_circle()
    square = factory.create_square()
    
    print(circle.draw())
    print(square.draw())

print("Creating and drawing Red shapes:")
red_factory = RedShapeFactory()
create_and_draw_shapes(red_factory)

print("\nCreating and drawing Blue shapes:")
blue_factory = BlueShapeFactory()
create_and_draw_shapes(blue_factory)
