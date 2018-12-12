# Program for the Yahtzee game
# Author SLW   Date Aug 2018
# A prototype game for Reading School
 
# Import libraries
import tkinter as tk
from tkinter import messagebox
import random
 
# Define program wide variables
button_names = []
button_textboxes = []

# Function to display the window in the centre of the screen
def centre_window(win_width, win_height):
    x = (window.winfo_screenwidth() // 2) - (win_width // 2)
    y = (window.winfo_screenheight() // 2) - (win_height // 2)
    # DEBUG print("Screen width {} & screen height {}".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    window.geometry('{}x{}+{}+{}'.format(win_width, win_height, x, y))
 

# Parse the game move
def click_button(button):
    
    if button == button_names[0]:  # Process button 1
        button_textboxes[0].insert(1.0, "1")
        show_dice(button)

    if button == button_names[1]:  # Process button 2
        button_textboxes[1].insert(1.0, "2")
        show_dice(button)
 
    if button == button_names[2]:  # Process button 3
        button_textboxes[2].insert(1.0, "3")
        show_dice(button)
 
    if button == button_names[3]:  # Process button 4
        button_textboxes[3].insert(1.0, "4")
        show_dice(button)

    if button == button_names[4]: # Process button 5
        button_textboxes[4].insert(1.0, "5")
        show_dice(button)
 

# Display the buttons
def display_button():
    for i in range(0, 5):
        button_names.append(tk.Button(button_frame, image=blank, bg="lightblue"))
        button_textboxes.append(tk.Text(button_frame, width=1, height=1))
 
        button_names[-1].grid(row=1, column=i, sticky='e')
        button_names[-1].configure(command=lambda b=button_names[-1]: click_button(b))

        # Show the button names as they are made
        print(button_names[-1], i)
        
        button_textboxes[-1].grid(row=2, column=i)
        button_textboxes[-1].insert(tk.INSERT, "0")


# Display the dice image on the button
def show_dice(theButton):
    number = random.randint(1,6)
    print("The number of the dice is " + str(number)) # DEBUG to check the dice value
    if number == 1:
        theButton.configure(image=photo1)
    elif number == 2:
        theButton.configure(image=photo2)
    elif number == 3:
        theButton.configure(image=photo3)
    elif number == 4:
        theButton.configure(image=photo4)
    elif number == 5:
        theButton.configure(image=photo5)
    else:
        theButton.configure(image=photo6)
        

# Create the main window frame
window = tk.Tk()
 
# Set the main window title
window.title("Example of Buttons and text display")
 
# Set the main window size in pixels and centre it
centre_window(500, 400)

# Ensure the user cannot change the size of the window
window.resizable(width=False, height=False)
 
# Add a heading
heading = tk.Label(text="Showing the use of buttons", fg="purple")
heading.grid(column=0, row=0)
 
# Reserve space for the dice
button_frame = tk.Label(window)
button_frame.grid(columnspan=6, rowspan=3)

# Load images for the dice 
blank = tk.PhotoImage(file="Press.png")
photo1 = tk.PhotoImage(file="Press1.png")
photo2 = tk.PhotoImage(file="Press2.png")
photo3 = tk.PhotoImage(file="Press3.png")
photo4 = tk.PhotoImage(file="Press4.png")
photo5 = tk.PhotoImage(file="Press5.png")
photo6 = tk.PhotoImage(file="Press6.png")

display_button()


# Display the main window
window.mainloop()
