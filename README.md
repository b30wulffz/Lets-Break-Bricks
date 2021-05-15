# DASS Assignment 2 - Lets Break Bricks

As per the name suggests, this is a bricks breaking game. This game consists of a paddle, ball, and a few bricks. The ball is launched from the paddle, gets reflected upon touching the walls, and breaks the bricks. Simple? Game makes use of several powerups and special bricks, to make it more challenging and fun. Wanna experience the same? Then checkout the instructions below.

There are 6 types of bricks:

- Easy Brick [Yellow]: 100 Points: 1 Hit
- Medium Brick [Cyan]: 200 Points: 2 Hits
- Hard Brick [Magenta]: 300 Points: 3 Hits
- Unbreakable Brick [White]: 50 Points: Cannot be broken without powerup or superbrick
- Super Brick [Blue]: 400 Points: 1 Hit: Upon exploding, it breaks all the neighbours too, irrespective of their health
- Rainbow Brick: A special type of brick which keeps on changing its level(among Easy, Medium, Hard) until hit for the first time

## Instructions

Here we are going to use Python 3:

- In the directory, where game is stored, open the terminal and type `python main.py`.
- Game will start, and the timer will start ticking.
- Press `q` to quit the game.
- Press `a` to move the paddle to the left.
- Press `d` to move the paddle to the right.
- Press `w` to release the ball.
- The game will end when:
  - once all the bricks (except unbreakable bricks) are destroyed and boss is defeated.
  - when all the lives are finished.
- There are 3 lives per game.
- A life is lost, when there are no balls left on the board.
- A ball gets destoyed once it touches the bottom of the board.
- Powerups can be collected by moving the paddle below the dropping powerup.
- Powerups get reset when a life is lost.
- When a brick is destroyed, its points are added in the score.
- When the game gets over, you can see your total score and the total time elapsed.
- If you want to replay the game after the game gets over, you need to quit the game, and then restart it using the first instruction.
- [For Debug] Press `p` to switch the levels.

## Levels

The game is divided into 3 levels. And yeah, successor is even more challenging than the predecessor.

- Level 1: The simplest level among all, contains four rows of bricks, which need to be cleared in order to proceed to level 2.
- Level 2: This level is a little more challenging than the previous one. It consists of 5 rows along with a twist. The rules to pass to next level are same as the previous one.
- Level 3: This is the final and the toughest level. It consists of 5 rows of bricks as well as a Boss enemy. These 5 rows needs to be cleared and the boss enemy should be defeated in order to win the game.
  - Boss Enemy: This is actually a UFO which keeps on flying on top of the screen. It follows the paddle's movement, and keeps shooting bullets at some time interval. If these bullets hit the paddle, then the player will lose one life. It has health of 10 units. Moreover, it will spawn a layer of bricks underneath him twice when his health reaches 5 units and 2 units. These spawned bricks will not release any powerups.

### Falling Bricks

This feature makes gameplay even more challenging. In this, The layer of bricks falls by 1 unit after a fixed time interval. <br>
Hence when the bricks reach the level of paddle, the game gets over, irrespective of the number of lives left. <br>
The time interval varies for each level in the following order: `Level 1 > Level 3 > Level 2`. <br>

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
Multiple powerups can be active at the same time. <br>
Powerup follows the gravity effect after being released from the brick. <br>

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

### 7. Shooting Paddle

Identifier: 7 <br>
A cannon gets setup at the start and end of the paddle, which keeps on firing bullets at regular time interval. <br>
Each bullet causes damage equal to one ball strike. <br>
This powerup lasts for 5 seconds. <br>

### 8. Fireball

Identifier: 8 <br>
This powerup works the same as the super brick i.e. once it strikes, it explodes the current brick as well its neighbours irrespective of their health. <br>
This powerup lasts for 10 seconds. <br>

## Dependencies:

- Python 3
- colorama (Python Library)
- os (For playing music effects)
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
