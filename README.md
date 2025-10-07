1.Dice Roller – GUI Dice Simulator (Tkinter)

A simple Python project that simulates rolling a dice using a graphical user interface (GUI).
When you press the “Roll Dice” button, the app will:
Generate a random number between 1 and 6.
Display the corresponding dice face image.
Show a message with a color depending on the result (green for high rolls, orange for medium, red for low).

2. Technologies Used
Python 3.x
Tkinter – for the GUI (window, button, labels, images)
random – for generating random numbers
Images (dice.png, dice1.png … dice6.png) – each representing a dice face

3. Requirements
Python 3.x installed
Tkinter (included by default with Python on most systems)
Image files for the dice faces (dice.png, dice1.png, … dice6.png)

4. How the Program Works

The roll_dice() function generates a random number between 1 and 6.
The GUI (created with Tkinter) displays a window with:
A button to roll the dice
An image label to show the dice face
A text label to display the result in different colors depending on the roll
Each button click calls the roll_action() function, which updates both the dice image and the text message.
