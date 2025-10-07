#---------------------------------------------------------

#LIBRARIES

#tkinter for GUI interface
import tkinter as tk 
#random for the number
import random as rnd 

#---------------------------------------------------------

#DICE ROLLING

def roll_dice():
    #number between 1-6 coresponding to the picture
    number=rnd.randint(1,6) 
    return number #return which face

#---------------------------------------------------------

#GUI INTERFACE

def gui():

    #1) window
    #initialization
    root=tk.Tk()
    #color
    root.configure(bg="lightblue")
    #window title
    root.title("Dice Roller 🎲")
    #title on the window 
    title_label = tk.Label(root, 
                           text="Welcome to Dice Roller!",  #text
                           font=("Segoe UI", 16, "bold"), #font
                           bg="lightblue") #background
    title_label.pack(pady=10)

    # 2) list with images for each dice face
    dice_images = [
        tk.PhotoImage(file="dice.png"),
        tk.PhotoImage(file="dice1.png"),
        tk.PhotoImage(file="dice2.png"),
        tk.PhotoImage(file="dice3.png"),
        tk.PhotoImage(file="dice4.png"),
        tk.PhotoImage(file="dice5.png"),
        tk.PhotoImage(file="dice6.png")
    ]

    #3) image label
    #show image
    dice_label = tk.Label(root, 
                          image=dice_images[0], #for display - first img
                          bg="lightblue", #background
                          bd=5, #border
                          relief="solid")
    #format the image
    dice_label.pack(pady=20)

    #4)text label
    result_label = tk.Label(root,
                             text="", #text
                             font=("Segoe UI", 12), #font and size
                             bg="lightblue") #background
    result_label.pack()

    #5) button action
    def roll_action():
        number=roll_dice()
        #when the button is clicked show the random dice face
        dice_label.config(image=dice_images[number]) 
        #font color based on the result
        if number>=5:
            color="green"
        elif number>=3:
            color="orange"
        else:
            color="red"
        #show text
        result_label.config(text=f"You rolled a {number}!", fg=color)
    
    #6) button formating
    tk.Button(root,
              text="Roll Dice", #button text
              command=roll_action, #at click run roll_action() 
              font=("Arial", 10, "bold"), #font size and bold
              bg="grey", #background color
              fg="white" #font color
              ).pack(pady=10) #format
    
    #6)keep the window open
    root.mainloop()

#---------------------------------------------------------

#MAIN

def main():
    gui()

#---------------------------------------------------------

#CALL

main()