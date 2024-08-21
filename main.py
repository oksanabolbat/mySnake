from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("#000")
screen.title("WELCOME !")

screen.tracer(0)
snake = Snake()

food = Food()
game_score = Scoreboard()


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
    if snake.head.distance(food) <= 15:
        food.refresh_position()
        game_score.add_point()
        snake.extend_snake()
        screen.update()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        game_score.game_over()
    for tail in snake.segments[1:]:
        if snake.head.distance(tail) < 10:
            game_is_on = False
            game_score.game_over()
screen.exitonclick()
