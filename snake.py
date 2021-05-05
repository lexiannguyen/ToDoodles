import turtle
import time
import random

# border = turtle.Turtle()
# border.color("grey")
# border.penup()
# border.pensize(5)
# border.setpos(345,240)
# border.pendown()
# border.setpos(345,-240)
# border.setpos(-355,-240)
# border.setpos(-355,240)

# WIDTH = 700
# HEIGHT = 700
# win = turtle.Screen()
# win.setup(width = WIDTH, height = HEIGHT)

turtle.bgcolor("white")
#turtle.bgpic("./littleTurt/map2.gif")

ref = turtle.Turtle()
ref.hideturtle()
ref.penup()
ref.setpos(-250, 180)


snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.speed(0)
snake.penup()
snake.direction = "stop" #dont go anywhere mf


food = turtle.Turtle()
food.penup()
food.shape("circle")
food.color("brown")
food.shapesize(0.7)

color_list = ["blue", "red", "orange","gold","green","violet","tan", "pink","turquoise", "brown"]
snake_box = [snake]

window = turtle.Screen() #create a varbiable in charge of the window
window.tracer(0) # this doesnt delay our graphics from being updated

def move_up():
    snake.direction = "up"
def move_down():
    snake.direction = "down"
def move_left():
    snake.direction = "left"
def move_right():
    snake.direction = "right"

def move():
    x = snake.xcor()
    y = snake.ycor()

    if snake.direction == "up":
        snake.sety(y+20)
    if snake.direction == "down":
        snake.sety(y-20)
    if snake.direction == "left":
        snake.setx(x-20)
    if snake.direction == "right":
        snake.setx(x+20)

def random_food_location():
    x = random.randint(-220,220)
    y = random.randint(-220,220)
    food.sety(y)
    food.setx(x)

def check_bounds():
    x = snake.xcor()
    y = snake.ycor()
    if x > 280:
        snake.setx(-280)
    if x < -280:
        snake.setx(280)
    if y > 240:
        snake.sety(-240)
    if y < -240:
        snake.sety(240)

def check_food():
    x_food = food.xcor()
    y_food = food.ycor()
    x = snake.xcor()
    y = snake.ycor()
    if((abs(x_food - x) <= 10) and (abs(y_food-y)<=10)):
        return True
    
def display_score(score):
    ref.clear()
    ref.color(random.choice(color_list))
    ref.write(f"score: {score}", font=("arial",25,"italic"))

def add_turtle():
    snake_x = snake.xcor()
    snake_y = snake.ycor()
    snake_butt = turtle.Turtle()
    snake_butt.penup()
    snake_butt.shape("square")
    snake_butt.color(random.choice(color_list))
    #snake_butt.setpos(snake_x-20, snake_y)
    snake_butt.speed(10)
    snake_box.append(snake_butt)
    #snake_box[0].setpos(snake.xcor(), snake.ycor())
    #snake_box[0].setpos(snake_x-20, snake_y)


window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

snakes_alive = True
score = 0

random_food_location()

while snakes_alive:
    window.update()
    move()
    check_bounds()
    if check_food() == True:
        score += 1
        display_score(score)
        random_food_location()
        add_turtle()
        #snake_box[0].setpos(snake.xcor(), snake.ycor())

    x=20

    for s in range(len(snake_box)-1,0,-1):
        #snake_box[0].setpos(snake.xcor()-20, snake.ycor())
        #snake_box[s].setpos(snake.xcor()-x, snake.ycor())
        x+=20

        
        snake_box[s].setpos(snake_box[s-1].xcor(),snake_box[s-1].ycor())
    

    time.sleep(0.1)




turtle.mainloop()