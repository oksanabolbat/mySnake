from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("#000")
screen.title("WELCOME !")

screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()
