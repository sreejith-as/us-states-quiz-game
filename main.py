import turtle
from turtle import Turtle, Screen
import pandas

# Set up the screen
screen = Screen()
screen.title("U.S States Game")

# Load the U.S. map image as the shape for the turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the CSV data with all 50 states and their coordinates
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Main game loop: continues until 50 correct guesses
while len(guessed_states) < 50:
    # Prompt user to enter a state name
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state?"
    ).capitalize()

    # If the user types "Exit", save missing states to a CSV and quit
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # If the guess is correct and not already guessed
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        # Get the x and y coordinates of the guessed state
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # Write the state name on the map
        t.write(answer_state)
