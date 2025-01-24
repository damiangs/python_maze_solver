class Line:
    # Constructor takes two Point objects
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    # Draw method to render the line on canvas
    def draw(self, canvas, fill_color):
        # Call canvas method to create line
        canvas.create_line(
            self.point1.x,  # x1 coordinate
            self.point1.y,  # y1 coordinate
            self.point2.x,  # x2 coordinate
            self.point2.y,  # y2 coordinate
            fill=fill_color,
            width=2,
        )