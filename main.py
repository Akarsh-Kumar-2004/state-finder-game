import turtle
import pandas
screen = turtle.Screen()
screen.title("Guess The U.S Game")
image = "./turtlevenv/state_finder/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./turtlevenv/state_finder/50_states.csv")
states = data["state"].to_list()

guessed_states = []







while len(guessed_states)<50:
    user_input = screen.textinput(title =f"{len(guessed_states)}/50 states",prompt="what's the state name ?").title()
    if user_input == "Exit":
        missing_states = []
        for s in states:
            if s not in guessed_states:
                missing_states.append(s)
        result = pandas.DataFrame(missing_states)
        result.to_csv("./turtlevenv/state_finder/missing_state.csv")
        break
    
    if user_input in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_input]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(user_input)
        
        
        
        
        
screen.exitonclick()