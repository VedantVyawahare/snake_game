# from turtle import Turtle
#
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 360
# x_cors = [(0, 0), (-20, 0), (-40, 0) ]
#
#
#
# class Snake:
#     def __init__(self):
#         self.snakes = []
#         self.create_snake()
#         self.head = self.snakes[0]
#
#     def create_snake(self):
#         for position in x_cors:
#             self.add_segment(position)
#
#     def add_segment(self, position):
#         snake = Turtle(shape="square")
#         snake.color("white")
#         snake.penup()
#         snake.goto(position)
#         self.snakes.append(snake)
#
#     def extend(self):
#     #adds the new segment to snake
#         self.add_segment(self.snakes[-1])
#
#
#     def up(self):
#         if self.head.heading() != DOWN:
#             self.snakes[0].setheading(UP)
#
#     def down(self):
#         if self.head.heading() != UP:
#             self.snakes[0].setheading(DOWN)
#
#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.snakes[0].setheading(LEFT)
#
#     def right(self):
#         if self.head.heading() != LEFT:
#             self.snakes[0].setheading(RIGHT)
#
#     def move(self):
#         for seg_num in range(len(self.snakes)-1, 0, -1):
#             new_x = self.snakes[seg_num - 1].xcor()
#             new_y = self.snakes[seg_num - 1].ycor()
#             self.snakes[seg_num].goto(x=new_x, y=new_y)
#         self.head.forward(20)
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
