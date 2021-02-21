# DASS Assignment 2 - Lets Break Bricks

As per the name suggests, this is a bricks breaking game. This game consists of a paddle, ball, and a few bricks. The ball is launched from the paddle, gets reflected upon touching the walls, and breaks the bricks. Simple? Game makes use of several powerups and special bricks, to make it more challenging and fun. Wanna experience the same? Then checkout the instructions below.

There are 5 types of bricks:

- Easy Brick [Yellow]: 100 Points: 1 Hit
- Medium Brick [Cyan]: 200 Points: 2 Hits
- Hard Brick [Magenta]: 300 Points: 3 Hits
- Unbreakable Brick [White]: 50 Points: Cannot be broken without powerup or superbrick
- Super Brick [Blue]: 400 Points: 1 Hit: Upon exploding, it breaks all the neighbours too, irrespective of their health

## Instructions

Here we are going to use Python 3:

- In the directory, where game is stored, open the terminal and type `python main.py`.
- Game will start, and the timer will start ticking.
- Press `q` to quit the game.
- Press `a` to move the paddle to the left.
- Press `d` to move the paddle to the right.
- Press `w` to release the ball.
- The game will end when:
  - once all the bricks (except unbreakable bricks) are destroyed.
  - when all the lives are finished.
- There are 3 lives per game.
- A life is lost, when there are no balls left on the board.
- A ball gets destoyed once it touches the bottom of the board.
- Powerups can be collected by moving the paddle below the dropping powerup.
- Powerups get reset when a life is lost.
- When a brick is destroyed, its points are added in the score.
- When the game gets over, you can see your total score and the total time elapsed.
- If you want to replay the game after the game gets over, you need to quit the game, and then restart it using the first instruction.

## Paddle

A logic for ball paddle reflection is as follows:

- Angle of reflection of the ball from paddle depends on where the ball hits on paddle.
- If the ball hits a point which is closer to the center of the paddle(< 50%), then the change in angle of reflection is small.
- If the ball hits a point which is farther from the center of paddle(>=50%), then the change in angle of reflection is large.
- If the ball hits on left side of paddle, then x velocity of ball is decreased(increased towards negative value).
- If the ball hits on right side of paddle, then x velocity of ball is increased.

## Powerups

Each powerup has a number associated with it, also known as identifier(here). This number is written on the powerup. <br>
Each powerup lasts for a certain time interval. <br>
Once the paddle collects a power up, the timer of powerup starts. <br>
Collecting the same powerup again, increases the time interval to that of newer powerup (except for Ball Multiplier powerup). <br>
Multiple powerups can be active at the same time.

### 1. Expand Paddle

Identifier: 1 <br>
It expands the paddle by 6 units. <br>
This powerup lasts for 10 seconds. <br>

### 2. Shrink Paddle

Identifier: 2 <br>
It shrinks the paddle by 6 units. <br>
This powerup lasts for 10 seconds. <br>
If both expand and shring paddle powerups are active simultaneously, then the width of the paddle will remain same as the initial width. <br>

### 3. Ball Multiplier

Identifier: 3 <br>
It multiplies the ball, which is farthest from the base of the board, into two balls. <br>
This powerup lasts for 10 seconds. <br>
Once the powerup is finished, the ball nearest to the base of the board disappears. <br>

### 4. Fast Ball

Identifier: 4 <br>
The speed of the ball gets multiplied by 2. <br>
This powerup lasts for 5 seconds. <br>

### 5. Thru Ball

Identifier: 5 <br>
Ball passes through any type of bricks, destroying it (even through Unbreakable Brick). <br>
This powerup lasts for 5 seconds. <br>

### 6. Paddle Grab

Identifier: 6 <br>
This grabs the ball falling on the board. <br>
`w` should be pressed in order to release the ball. <br>
Ball maintains the same velocity as it had before grabbing. <br>
This powerup lasts for 10 seconds. <br>
If the powerup is active, it will hold the ball again and again. <br>
It can hold only one ball at a time. <br>
If the powerup is finished, held ball gets launched without user interaction. <br>

## Dependencies:

- Python 3
- colorama (Python Library)
- Linux-based terminal (in fullscreen mode)

Game is developed purely in Python and follows the concept of Object Oriented Programming, which includes Abstraction, Inheritence, Polymorphism and Encapsulation.

# Machine Specifications

Details of the machine on which the game was tested:

- Operating System: Elementary OS 5.1 (Hera)
- Terminal: Bash
- Processor: Intel Core i7-8750H CPU @ 2.20 GHz 2.21 GHz
- RAM: 16 GB

# Developed by

- Shlok Pandey
- Email: shlok.pandey@research.iiit.ac.in
- Roll Number: 2020121008
