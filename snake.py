from turtle import Turtle

body_position = [(0, 0), (-20, 0), (-40, 0)]
body_movement = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for i in body_position:
            self.add_segment(i)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for segment_position in range(len(self.snake_body) - 1, 0, -1):
            new_position_x = self.snake_body[segment_position - 1].xcor()
            new_position_y = self.snake_body[segment_position - 1].ycor()
            self.snake_body[segment_position].goto(new_position_x, new_position_y)
        self.snake_body[0].forward(body_movement)

    def up(self):
        if self.snake_body[0] != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0] != 90:
            self.snake_body[0].setheading(270)

    def left(self):
        if self.snake_body[0] != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0] != 180:
            self.snake_body[0].setheading(0)
