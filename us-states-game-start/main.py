import turtle
import pandas

score = 0
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()

game_is_on = True
no_of_iteration = 0

# at the begning of the game
wrong_guess_states = all_states

correct_guess = []

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct Guess the state",
                                    prompt="What's another state's name?")
    req_state = answer_state.title()
    # print(answer_state.capitalize())
    no_of_iteration += 1
    if req_state == "Exit":
        break
    if no_of_iteration == 50:
        game_is_on = False
    if req_state in all_states:
        wrong_guess_states.remove(req_state)
        score += 1
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data.state == req_state]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(f"{req_state}", align="center", font=("Arial", 10, "normal"))


wrong_guess_x = []
wrong_guess_y = []

for item in wrong_guess_states:
    state_data = data[data.state == item]
    wrong_guess_x.append(int(state_data.x))
    wrong_guess_y.append(int(state_data.y))

print(wrong_guess_states)
print(wrong_guess_x)
print(wrong_guess_y)

wrong_data_dict = {
    "state": wrong_guess_states,
    "x": wrong_guess_x,
    "y": wrong_guess_y
}
new_data = pandas.DataFrame(wrong_data_dict)
new_data.to_csv("states_to_learn.csv")










