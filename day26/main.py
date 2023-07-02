import turtle
import pandas

guessed_State = []
missing_states = []
screen = turtle.Screen()
screen.title("States guessing game")
image = "day26\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("day26\\50_states.csv")
states_data = data["state"].to_list()
while len(guessed_State) <= 50:
    answer = screen.textinput(f"{len(guessed_State)}/50", "Enter the name:").title()
    if answer in states_data:
        guessed_State.append(answer)
        states_coordinates = data[data["state"] == answer]
        ujwal = turtle.Turtle()
        ujwal.penup()
        ujwal.hideturtle()
        states_coordinates_x = states_coordinates['x']
        states_coordinates_y = states_coordinates['y']
        coordinates = (float(states_coordinates_x), float(states_coordinates_y))
        ujwal.goto(coordinates)
        ujwal.write(answer)
    if answer == "Exit":
        break
missing_states = [states for states in states_data if states not in guessed_State]
print(missing_states)
dictionary_data = {
    "states_missed": missing_states
}
data_dick = pandas.DataFrame(dictionary_data)
print(data_dick)
data_dick.to_csv("day26\\states_missed.csv")
