# **Pong Game**

## **Video Demo:**
[Live Demo](https://youtu.be/Jdq0lGXcUm4)

## **Description:**

### Technologies used:

- Pygame
- Python

### Concepts in the project:

- Data strucutre (list, tuple)
- Object-Oriented Programming (OOP)
- Conditional statements
- Function from pygame library

### About this project
'Pong Game' is a game where the object is to hit the ball so that it goes over the course of the opponent's half of the table in such a way that the opponent cannot reach it or return it correctly. Two-player starts with 0 points, and the player who gets to 10 points first will win the game.
\
\
The 'Pong Game' idea is from Youtuber 'Tech With Tim'. The video tutorial on making pong games in pygame from the channel includes the general layout and function. My project has been reorganised to be the best fit for a friendly UI, such as building the main menu and the end scene and improving the collision between the ball and the paddle.
\
\
The solution for the project is coded in python using the pygame library. It includes seven functions that control how the users interact with the game, and two objects, the ball and paddle, have their own attributes and methods. The project includes some concepts such as data structure, class and object, conditional statement and function from pygame.
\
\
In the main function, I use a while loop to keep the program running until the user quits, then I display all the ball, paddles and elements on the screen with function from the pygame library. This main function also checks if there is a winner and stops the program. This function also checks if the ball hit the wall or the paddle to change its direction.
\
\
In the program, I created two objects, a ball and a paddle object, for the convenience of having the class's variable and function. Each object has a draw function that can draw itself on the screen. Some attributes of the ball object are location (x, y), radius and velocity. Some attributes of the paddle object are location (x, y), width and height.
\
\
I created three different draw functions, draw, draw_start and draw_end, to display different elements at different times in the program. These draw functions first fill the background with black colour and then add other elements on top. At the end of these functions, the functions from pygame update all the changes on the screen.
\
\
The handle_coll and handle_key functions in the program control the movement of the paddle and the ball by changing it y location and checking if the ball location hit the wall or the paddle location.
\
\
Note: pygame library need to be installed before running this project.
