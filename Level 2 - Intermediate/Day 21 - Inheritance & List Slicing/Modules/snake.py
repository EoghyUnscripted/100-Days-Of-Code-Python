from turtle import Screen, Turtle

position_list = [(0, 0), (-20, 0), (-40, 0)]
distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    """Class used to create initial snake body and add functions for snake objects."""

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def up(self):
        """Function used to turn turtle object counter-clockwise."""
        if self.head.heading() != down:
            self.head.setheading(90)  # Turn North

    def down(self):
        """Function used to turn turtle object clockwise."""
        if self.head.heading() != up:
            self.head.setheading(270)  # Turn South

    def left(self):
        """Function used to turn turtle object clockwise."""
        if self.head.heading() != right:
            self.head.setheading(180)  # Turn West

    def right(self):
        """Function used to turn turtle object clockwise."""
        if self.head.heading() != left:
            self.head.setheading(0)  # Turn East

    def move(self):
        """Function used to move snake object forward."""
        for segment in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[segment - 1].xcor()
            new_y = self.turtle_list[segment - 1].ycor()
            self.turtle_list[segment].goto(new_x, new_y)
        self.turtle_list[0].forward(distance)

    def create_snake(self):
        """Function used to create initial snake objet for Turtle screen."""
        # Fill the initial turtle list for snake body
        for position in position_list:
            self.add_tail(position)

    def add_tail(self, position):
        new_turtle = Turtle()
        new_turtle.color("grey")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtle_list.append(new_turtle)

    def extend(self):
        self.add_tail(self.turtle_list[-1].position())
