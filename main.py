from turtle import Turtle, Screen
import pandas
import sys

#set up pen
pen = Turtle()
pen.penup()
pen.hideturtle()

#set up turtle obect screen
screen = Screen()
screen.title("U.S States Game")

#insert gif image for screen and set turtle to new shape
image = "blank_states_img.gif"
screen.addshape(image)
map = Turtle()
map.shape(image)

#access the csv file and set to varaible "data"
data = pandas.read_csv("C:\Code\\Python\\day-25-us-states-game-start\\50_states.csv")

#set up list
correct_answers = []

all_states = data.state.to_list()
score = len(correct_answers)
while score < 50:
    #establish a score counter 
    

    #The users prompt and answer for their state guess. Different wording for starting vs mid game.
    if score == 0:
        answer_state = (screen.textinput(title="Guess the State", prompt="Whats a state name?"))
        if answer_state == None:
            missing_states = [state for state in all_states if state not in correct_answers]
            missing_data = pandas.DataFrame(missing_states)
            missing_data.to_csv("states_to_learn.csv")
            sys.exit()
    else:
        answer_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="whats another state name?"))
        if answer_state == None:
            sys.exit()

    #returns the row from the csv in relation to user input
    #can return the specided data frame or an empty data frame
    answer_row = (data[data.state == answer_state.title()])

    if answer_state in correct_answers:
        print("repeat")
    elif answer_state.title() in all_states:
        correct_answers.append(answer_state.title())
        print(f"detected\n {answer_row}")
        pen.goto(answer_row.x.values[0], answer_row.y.values[0])
        pen.write(f"{answer_state.title()}", move=False, align='center', font=('Arial', 8, 'normal'))
    else:
        print("L")

screen.exitonclick()