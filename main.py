import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#turtle
text = turtle.Turtle()
text.hideturtle()
text.penup()


states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()

guessed_states = []
game_is_on = True

while game_is_on:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")

    if answer_state == "exit":
        game_is_on = False

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = states[states.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        text.goto(x, y)
        text.write(answer_state, align=ALIGNMENT, font= FONT)

    if len(guessed_states) >= 50:
        game_is_on = False


screen.exitonclick()
