from turtle import Turtle, Screen

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
Position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.screen = Screen()
        self.new_turtle = []
        self.defaultBody()
        self.head = self.new_turtle[0]

    def defaultBody(self):
        for i in Position:
            self.add_segment(i)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.new_turtle.append(snake)

    def extend(self):
        self.add_segment(self.new_turtle[-1].position())

    def move(self):
        self.screen.listen()
        for i in range(len(self.new_turtle) - 1, 0, -1):
            position_x = self.new_turtle[i - 1].xcor()
            position_y = self.new_turtle[i - 1].ycor()
            self.new_turtle[i].goto(position_x, position_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
