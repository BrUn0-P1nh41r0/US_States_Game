import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# turtle
text = turtle.Turtle()
text.hideturtle()
text.penup()

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")

    if answer_state == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_missing.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = states[states.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        text.goto(x, y)
        text.write(answer_state, align=ALIGNMENT, font=FONT)

