# Micro-Workshop 1: Learning Python with Turtle Graphics

*Lesson Goals*:

  - Become familiar with Python's main syntax, including:
    - Variable Assignment and Operators
    - Functions and Methods
    - Importing Modules
  - Write a working Python Script
  - Successfully Use Python to:
    - Solve Math Problems
    - Draw Pictures
    - Control Robots

## Installing and Running Python

Python comes built-in with Linux and Mac!  It can also be downloaded and installed from the Python Web Page https://www.python.org/downloads/

*Note*: The newest version of Python (Python 3) is recommended, but either version wil work for this workshop.

*To Run Python*:
  1. Open a terminal program:
    - Mac: Open Spotlight Search (apple+space) and type "Terminal".  This program will launch.
    - Linux: Use the Keyboard shortcut Ctrl+Alt+T, or open the program "Terminal"
    - Windows: Open the program called "Command Window" or "Powershell Terminal"

  2. Run the iPython Interactive REPL (Command-Line Interface), by typing: **python** and pressing the enter key.

![Alt text](_static/img/terminal.png "Optional title")

That's it! You're now in Python, one of the most popular general-purpose proramming languages in the world.

## Programming-Language-As-Calculator

Let's try doing the first thing everyone does when using computers: making math easier by using them as calculators!

Try using Python to solve these math problems:

### Math Exercises

   1. What is 1 + 1?
   2. What is 8 * 32?
   3. Let's make x = 7.
       - What is x * 5?
       - x * 32?
       - x / 3.2?
       - x + 555?
   4. Let's make apples = 8, pears = 10, and bananas = 12.
       - What is pears * apples?
       - apples + bananas?
       - bananas + apples?
       - apples * 3 + pears?
  

To make Python do more, we need to **import** modules.  These will give Python new **functions**.

Let's give Python more advanced math functions by importing the **math** module.  Enter the following into Python:

```python
import math
```
Now the math module is loaded! To get access to the abilities inside the math package, you need to use the **dot (.)**:

```python
math.sqrt(x)  # the square root of x
math.sin(x)  # The sine of x
math.exp(x)  # the exponent of x (e to the x'th power)
```
Notice the pattern above:  **PackageName.FunctionName(InputName)**.

To see a list of all the functions available in the math module, type:

```python
dir(math)
```

To read what a function does, use the **help** function, like so:

```python
help(math.sqrt)
```

To exit the help text, simply type the letter "**q**"

*Note*: Don't worry if you don't understand everything yet--that will come!

### Math Module Exercises

Answer the following questions:

  1. What is the square root of 32?
  2. What is the cosine of 1.72?
  3. what is the 5th digist of pi?
  4. What is the log of 18271?
  5. What is the log of the cosine of the square root of pi?


## Drawing with Turtle Graphics

The **turtle** module is a drawing application where you move Alex the **Turtle** around the screen.  Alex has a pen tied to his tail, and he leaves a trail wherever he goes!

To use this package, first, import it, then use these two lines to make alex the turtle::

```python
import turtle
alex = turtle.Turtle()
```

Alex can do lots of things.  He can move **forward** some distance, for example::

```python
alex.forward(100)
```

He can do other things, to!  Let's take some time now and use the skills you've learned so far to figure out what kinds of things you can do with Alex!

*Hint*: The **dir()** function will work on Alex, too.

### Turtle Graphics Exercises

  - Make a Triangle
  - Make a Bigger Triangle.
  - Clear the Screen.  (Hint: it is a function in the **turtle** module, not part of Alex.)
  - Make a Square.
  - Change the color of the turtle's pen.
  - Make a second turtle, and set his starting position to (10, 20), where he should draw a triangle, too.


## Saving Your Code: Writing Scripts

When you quit Python, all your hard work will be lost!  This is terribly sad, but if you put your code in a text file (named my_turtle_art.py), you can always run the code and the computer will make your beautiful artwork again!  Let's make a couple scripts together.

(10 Minutes: Live, Joint coding session)


# Making Your Own Functions.  

Have you noticed how you keep writing the same thing, over and over again?  Have you gotten tired of it yet?  Well, Python provides a way to make your own functions, which will automatically do several steps for you--once you've made it, all you have to do is tell it to do **MyFunction()**!

Here's how to write a function in Python:

```python

def function_name():
    step1
    step2
    step3

```

That's it!  Note each part of the above code: the **def** statement, the colon (**:**), and spaces before each line under the **def** are all important.  Let's make a couple of functions:

  - Make a **triangle()** function.
  - Make a **square()** function.
  - Make a **triangle(size)** function that takes a **size** input, which makes bigger triangles when bigger numbers are put in them!  This hasn't been introduced, but I bet you can figure out how to do this!

# Making Loops

## While Loops

(Lesson here)

## For Loops

(Lesson here)


# Tinker! 

Okay, now you're free from this guided lesson!  Take the next 20 minutes to make something you like!

# Control the RoboTurtle

In the Erfindergarden, we have our very own RoboTurtle--he is a wonderful artist, whose life purpose is to draw your Turtle Graphics art on his canvas!  He is controlled via a tiny computer called the **Raspberry Pi**.  We'll make a Python script that controls him, so he can paint our scripts!

To make your script work with the RoboTurtle, first make a copy of your script.  Then add the following at the top:

```python
import roboturtle
```

This won't work on your computer, but our Raspberry Pi has the **roboturtle** package, and it will work there.  Finally, you need to change your **alex = turtle.Turtle()** line to:

```python
alex = roboturtle.Roboturtle()
```

That's it!  Now your turtle has been Robo-fied!  Give your new robot script to your instructor, and he'll see how our RoboTurtle does with your art!


