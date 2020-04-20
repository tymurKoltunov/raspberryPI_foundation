from drawings.shapes import Rectangle, Oval, Paper

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
rect1.draw()
ov1 = Oval()
ov1.randomize()
ov2 = Oval()
ov2.randomize()
ov1.draw()
Paper.display()


