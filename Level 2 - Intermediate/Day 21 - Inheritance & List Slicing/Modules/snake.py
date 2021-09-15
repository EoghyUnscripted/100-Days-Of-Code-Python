from turtle import Turtle

position_list = [(0, 0), (-20, 0), (-40, 0)]    # Set initial positions of snake body segments
distance = 20   # Set distance to move each time
up = 90     # Set direction heading North
down = 270  # Set direction heading South
left = 180  # Set direction heading West
right = 0   # Set direction heading East


class Snake:
    """Class used to create initial snake body and add functions for snake objects."""

    def __init__(self):
        self.turtle_list = []   # Set blank list for snake body segments
        self.create_snake()     # Call function to create new snake object
        self.head = self.turtle_list[0]     # Set head attribute for navigation

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
        """Function used to move all snake objects forward together."""
        # Loop backward through turtle_list to get all objects and update positions
        for segment in range(len(self.turtle_list) - 1, 0, -1):
            # Get the previous x and y positions of the turtle in front of current object
            new_x = self.turtle_list[segment - 1].xcor()
            new_y = self.turtle_list[segment - 1].ycor()
            # Got to the new x and y coordinates
            self.turtle_list[segment].goto(new_x, new_y)
        self.turtle_list[0].forward(distance)   # Moves the head object at 0 forward

    def create_snake(self):
        """Function used to create initial snake objet for Turtle screen."""
        # Fill the initial turtle list for snake body
        for position in position_list:
            self.add_tail(position)     # Call function to create initial snake

    def add_tail(self, position):
        """Function used to add tail segments to the snake object."""
        new_turtle = Turtle()  # Create new turtle object
        new_turtle.color("grey")  # Set color to grey
        new_turtle.shape("square")  # Set the shape to square
        new_turtle.penup()  # Pen up to prevent drawing
        new_turtle.goto(position)  # Go to starting positions
        self.turtle_list.append(new_turtle)  # Append to turtle_list

    def extend(self):
        """Function used to add a new segment to end of snake tail."""
        self.add_tail(self.turtle_list[-1].position())  # Add new segment to tail
