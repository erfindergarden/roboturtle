# Micro-Workshop 2: Writing Python Programs to Control Decision-Making Robots

**Note:** This workshop is intended to follow *Micro-Workshop 1*.

**Note:** This Workshop is not yet completed.

## Workshop Description

**Duration**: 45-60 Minutes

**Target Audience**: Complete Beginners, ages 8-80

**Recommended Class Size**: 2-8.  At least one robot per pair of participants is strongly recommended.

**Learning Goals**:

  - Build on Python's Core Syntax and Learn New Programming Concepts, including:
    - Binary Operators and Logical Operations
    - Control Flow (if-else Statements)
    - While-Loops
    - Function Creation
  - Writing and Running Python Scripts
  - Successfully Use Python to:
    - Create a Mouse-Chasing Turtle
    - Create a Light-Chasing Robot
    - Create a spelling robot

## Logical Operations: True and False

In logic, things are either **True**, or they are **False**--there's no middle ground.  In Python, you can make a logical
value (called a "**bool**" variable) directly, or you can have Python make it for you by giving it a logical statement.

Direct True/False Creation.  *Note*: It's important that the T and F are capital letters:

```python
x = True
y = False
```

Logical Experessions.  To make them, use the **<** ("is-less-than"), **>** ("is-greater-than"), **==** ("is-equal-to"),
operators:

```python
3 > 2

3 > 5

3 == 3

x = 4 < 2
```

### Logical Operations Exercises

  1. Is 42 times 51 less than 41 * 52?
  2. There are also the **<=**, **>=**, and **!=** operators.  What do they do?


## Making Decisions: If Statements

Up until now, your code will always do the thing.  Let's try something new:

```python
x = 5
if x > 3:
    print('x is bigger than 3!')
```

Just like for-loops, if statements have colons (**:**) and spaces to tell Python what code belongs to the statement.
Try changing this code, starting with the value of **x**, to change what the code does!

### Else and Elif Statements

If you want your code to do something if "if" is False, you can add an **else** statement:

```python
x = 5
if x > 3:
    print('x is bigger than 3!')
else:
    print('x is not bigger than 3.')
```

You're not limited to only 2 options, of course.  You can add additional options with **elif** (pronounced "else if"):

```python
x = 5
if x > 3:
    print('x is bigger than 3!')
elif x == 3:
    print('x is equal to 3!')
else:
    print('x is not bigger than 3.')
```

### Elif Challenge Puzzle:

What numbers will be printed by the following code?

```python
x = 5
if x > 0:
    print(0)
elif x > 1:
    print(1)
else:
    print(2)

if x > 3:
    print(3)
if x > 4:
    print(4)
elif x > 5:
    print(5)

if x > 6:
    print(6)

```

## While Loops

We can also use logical statements to tell Python whether to loop or not.  This is done using **while** loops, **which will repeat
as long as the logical statement is true**.  What will this code do?

```python
x = 0
while x < 4:
    print(x)
    x = x + 1
```

### Infinite Loops

If something is always True, the code will keep looping until the end of time!  If this is done accidentally, you can stop
the code from continuing by pressing **Ctrl-C**.

Sometimes, though, we want infinite loops!  A common way to write this is like so:

```python
while True:
    print('Still running...')
```

You can also stop a loop with the **break** statement.  This is called "breaking out of a loop".  Like this:

```python
x = 0
while True:
    x = x + 1
    if x > 5:
        break
```

### Loop Exercise: Collecting Data

**Goal**: Write a while-loop that continuously prints the current mouse pointer position using the **turtle** package.

*Tip*: The mouse position-getting functions can be obtained using the following code:

```python
import turtle
screen = turtle.Screen()  # Makes a Screen directly
canvas = screen.getcanvas()  # All the low-level functions are found in the Canvas object.

mouse_position = canvas.winfo_pointerxy()  # gets the x, y positions of the mouse
```

### Exercise: Create a Light-Chasing Robot

Our RoboTurtles have two light sensors!  Write a Script that tells the robot to turn left when the light is brighter on its
left side, and to turn right when it is brighter on its right side.

**Note**: The instructor will help you connect to the robots so you can control them from your computer.

## Defining Your Own Functions

### Exercise: Write a letter-writing turtle function

Let's make our turtle Graphics Turtles draw letters on the screen, making a different function for each letter!
The function should have the following form:

```python
def draw_a(turtle):
    # Commands
```

## Saving Your Code: Creating A Script


## Creating and Importing Your Own Python Modules

### Exercise: Combine Everyone's Functions to Spell Your Name in Turtle





