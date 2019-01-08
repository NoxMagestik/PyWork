from tkinter import *  # Importing tkinter as well as the modules which are needed
import random
import tkinter.font
import tkinter.messagebox

"""
To Do: 
"""


#  Initialising the tkinter window
tk = Tk()
tk.title("Yahtzee")
tk.configure(bg="black")
width_of_window = 660
height_of_window = 580

screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()

x_coordinate = (screen_width/2) - (width_of_window/2)
y_coordinate = (screen_height/2) - (height_of_window/2)
# This is used to make sure that the tkinter window is displayed in the middle of the window
tk.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

#  Button variables
button_width = 10
button_height = 4
roll_colour = "yellow"
dice_colour = "thistle"

dice_fg = "yellow"
dice_changed = "red"

Category_button_width = 10
Category_button_height = 2
Category_colour = "aqua"

Category_label_height = 2
Category_label_width = 10
Category_label_colour = "black"
Category_label_fg = "light blue"

Score_label_colour = "chartreuse"
Turns = 1
Rolls = 1

DiceNo = [0, 0, 0, 0, 0]

Dice1_keep = False
Dice2_keep = False
Dice3_keep = False
Dice4_keep = False
Dice5_keep = False
Is_chosen = False

Lower_score = 0
Upper_Score = 0
Total_score = 0
Bonus_score = False

helv = tkinter.font.Font(family="Helvetica", size=12, weight="bold")

Roll = Button(tk, text="Roll", font=helv, height=button_height, width=button_width, bg=roll_colour,
              command=lambda: roll_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll, No_rolls_label))
Roll.grid(row=1, column=0)

Dice1 = Button(tk, text=" ", font=helv, height=button_height, width=button_width, bg=dice_colour, fg=dice_fg,
               command=lambda: dice_select(Dice1))
Dice1.grid(row=1, column=1)
Dice2 = Button(tk, text=" ", font=helv, height=button_height, width=button_width, bg=dice_colour, fg=dice_fg,
               command=lambda: dice_select(Dice2))
Dice2.grid(row=1, column=2)
Dice3 = Button(tk, text=" ", font=helv, height=button_height, width=button_width, bg=dice_colour, fg=dice_fg,
               command=lambda: dice_select(Dice3))
Dice3.grid(row=1, column=3)
Dice4 = Button(tk, text=" ", font=helv, height=button_height, width=button_width, bg=dice_colour, fg=dice_fg,
               command=lambda: dice_select(Dice4))
Dice4.grid(row=1, column=4)
Dice5 = Button(tk, text=" ", font=helv, height=button_height, width=button_width, bg=dice_colour, fg=dice_fg,
               command=lambda: dice_select(Dice5))
Dice5.grid(row=1, column=5)

ones = Button(tk, text="Ones", font=helv, height=Category_button_height, width=Category_button_width,
              bg=Category_colour, command=lambda: upper_section(ones, ones_label, Upper_score_label, Total_score_label))
twos = Button(tk, text="Twos", font=helv, height=Category_button_height, width=Category_button_width,
              bg=Category_colour, command=lambda: upper_section(twos, twos_label, Upper_score_label, Total_score_label))
threes = Button(tk, text="Threes", font=helv, height=Category_button_height, width=Category_button_width,
                bg=Category_colour, command=lambda: upper_section(threes, threes_label, Upper_score_label,
                                                                  Total_score_label))
fours = Button(tk, text="Fours", font=helv, height=Category_button_height, width=Category_button_width,
               bg=Category_colour, command=lambda: upper_section(fours, fours_label, Upper_score_label,
                                                                 Total_score_label))
fives = Button(tk, text="Fives", font=helv, height=Category_button_height, width=Category_button_width,
               bg=Category_colour, command=lambda: upper_section(fives, fives_label, Upper_score_label,
                                                                 Total_score_label))
sixes = Button(tk, text="Sixes", font=helv, height=Category_button_height, width=Category_button_width,
               bg=Category_colour, command=lambda: upper_section(sixes, sixes_label, Upper_score_label,
                                                                 Total_score_label))

ones.grid(row=2, column=0, sticky=W)
twos.grid(row=3, column=0, sticky=W)
threes.grid(row=4, column=0, sticky=W)
fours.grid(row=5, column=0, sticky=W)
fives.grid(row=6, column=0, sticky=W)
sixes.grid(row=7, column=0, sticky=W)

tok = Button(tk, text="3 of a kind", font=helv, height=Category_button_height, width=Category_button_width,
             bg=Category_colour, command=lambda: lower_section(tok, tok_label, Lower_score_label, Total_score_label))
fok = Button(tk, text="4 of a kind", font=helv, height=Category_button_height, width=Category_button_width,
             bg=Category_colour, command=lambda: lower_section(fok, fok_label, Lower_score_label, Total_score_label))
fh = Button(tk, text="Full House", font=helv, height=Category_button_height, width=Category_button_width,
            bg=Category_colour, command=lambda: lower_section(fh, fh_label, Lower_score_label, Total_score_label))
ss = Button(tk, text="Small Straight", font=helv, height=Category_button_height, width=Category_button_width,
            bg=Category_colour, command=lambda: lower_section(ss, ss_label, Lower_score_label, Total_score_label))
ls = Button(tk, text="Large Straight", font=helv, height=Category_button_height, width=Category_button_width,
            bg=Category_colour, command=lambda: lower_section(ls, ls_label, Lower_score_label, Total_score_label))
yah = Button(tk, text="Yahtzee", font=helv, height=Category_button_height, width=Category_button_width,
             bg=Category_colour, command=lambda: lower_section(yah, yah_label, Lower_score_label, Total_score_label))
chance = Button(tk, text="Chance", font=helv, height=Category_label_height, width=Category_button_width,
                bg=Category_colour, command=lambda: lower_section(chance, chance_label, Lower_score_label,
                                                                  Total_score_label))

tok.grid(row=2, column=3, sticky=W)
fok.grid(row=3, column=3, sticky=W)
fh.grid(row=4, column=3, sticky=W)
ss.grid(row=5, column=3, sticky=W)
ls.grid(row=6, column=3, sticky=W)
yah.grid(row=7, column=3, sticky=W)
chance.grid(row=8, column=2)

ones_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg,
                   height=Category_label_height, width=Category_label_width)
twos_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg,
                   height=Category_label_height, width=Category_label_width)
threes_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg,
                     height=Category_label_height, width=Category_label_width)
fours_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg,
                    height=Category_label_height, width=Category_label_width)
fives_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg,
                    height=Category_label_height, width=Category_label_width)
sixes_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg,
                    height=Category_label_height, width=Category_label_width)

ones_label.grid(row=2, column=1)
twos_label.grid(row=3, column=1)
threes_label.grid(row=4, column=1)
fours_label.grid(row=5, column=1)
fives_label.grid(row=6, column=1)
sixes_label.grid(row=7, column=1)

tok_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg, height=Category_label_height,
                  width=Category_label_width)
fok_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg, height=Category_label_height,
                  width=Category_label_width)
fh_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg, height=Category_label_height,
                 width=Category_label_width)
ss_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg, height=Category_label_height,
                 width=Category_label_width)
ls_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg, height=Category_label_height,
                 width=Category_label_width)
yah_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg, height=Category_label_height,
                  width=Category_label_width)
chance_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Category_label_fg,
                     height=Category_label_height,width=Category_label_width)

tok_label.grid(row=2, column=4)
fok_label.grid(row=3, column=4)
fh_label.grid(row=4, column=4)
ss_label.grid(row=5, column=4)
ls_label.grid(row=6, column=4)
yah_label.grid(row=7, column=4)
chance_label.grid(row=8, column=3)


Lower_score_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Score_label_colour,
                          height=Category_label_height, width=Category_label_width)
Upper_score_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Score_label_colour,
                          height=Category_label_height, width=Category_label_width)
Total_score_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg=Score_label_colour,
                          height=Category_label_height, width=Category_label_width)
No_rolls_label = Label(tk, text="0", font=helv, bg=Category_label_colour, fg="yellow",
                       height=Category_label_height, width=Category_label_width)

Lower_score_text = Label(tk, text="Lower Score: ", bg=Category_label_colour, fg=Score_label_colour, font=helv,
                         height=Category_button_height,
                         width=Category_button_width)
Upper_score_text = Label(tk, text="Upper Score: ", bg=Category_label_colour, fg=Score_label_colour, font=helv,
                         height=Category_button_height,
                         width=Category_button_width)
Total_score_text = Label(tk, text="Total Score: ", bg=Category_label_colour, fg=Score_label_colour, font=helv,
                         height=Category_button_height,
                         width=Category_button_width)
No_rolls_text = Label(tk, text="Rolls: ", font=helv, bg=Category_label_colour, fg="yellow",
                      height=Category_button_height, width=Category_button_width)


Lower_score_label.grid(row=10, column=1)
Upper_score_label.grid(row=10, column=3)
Total_score_label.grid(row=10, column=5)
No_rolls_label.grid(row=11, column=1)

Lower_score_text.grid(row=10, column=0)
Upper_score_text.grid(row=10, column=2)
Total_score_text.grid(row=10, column=4)
No_rolls_text.grid(row=11, column=0)


def roll_dice(die1, die2, die3, die4, die5, roll_die, roll_label):
    global Rolls
    global Turns
    global Is_chosen
    global DiceNo
    global Dice1_keep
    global Dice2_keep
    global Dice3_keep
    global Dice4_keep
    global Dice5_keep

    if Turns < 14:
        Is_chosen = False
        change_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)
        if Rolls <= 3:
            roll_label["text"] = Rolls
            print("Turns: ", Turns)
            if Dice1_keep is False:
                die1["text"] = random.randint(1, 6)
                DiceNo[0] = die1["text"]

            if Dice2_keep is False:
                die2["text"] = random.randint(1, 6)
                DiceNo[1] = die2["text"]

            if Dice3_keep is False:
                die3["text"] = random.randint(1, 6)
                DiceNo[2] = die3["text"]

            if Dice4_keep is False:
                die4["text"] = random.randint(1, 6)
                DiceNo[3] = die4["text"]

            if Dice5_keep is False:
                die5["text"] = random.randint(1, 6)
                DiceNo[4] = die5["text"]

            if Rolls == 3:
                die1.configure(state=DISABLED, bg=dice_changed)
                die2.configure(state=DISABLED, bg=dice_changed)
                die3.configure(state=DISABLED, bg=dice_changed)
                die4.configure(state=DISABLED, bg=dice_changed)
                die5.configure(state=DISABLED, bg=dice_changed)
                roll_die.configure(state=DISABLED, bg=dice_changed)
            Rolls += 1
    else:
        restart()


def dice_select(die):
    global Dice1_keep
    global Dice2_keep
    global Dice3_keep
    global Dice4_keep
    global Dice5_keep

    if die == Dice1 and Dice1_keep is True:
        die.configure(bg=dice_colour)
        Dice1_keep = False
    elif die == Dice1 and die["text"] != " ":
        Dice1_keep = True
        die.configure(bg="red")

    if die == Dice2 and Dice2_keep is True:
        die.configure(bg=dice_colour)
        Dice2_keep = False
    elif die == Dice2 and die["text"] != " ":
        Dice2_keep = True
        die.configure(bg="red")

    if die == Dice3 and Dice3_keep is True:
        die.configure(bg=dice_colour)
        Dice3_keep = False
    elif die == Dice3 and die["text"] != " ":
        Dice3_keep = True
        die.configure(bg="red")

    if die == Dice4 and Dice4_keep is True:
        die.configure(bg=dice_colour)
        Dice4_keep = False
    elif die == Dice4 and die["text"] != " ":
        Dice4_keep = True
        die.configure(bg="red")

    if die == Dice5 and Dice5_keep is True:
        die.configure(bg=dice_colour)
        Dice5_keep = False
    elif die == Dice5 and die["text"] != " ":
        Dice5_keep = True
        die.configure(bg="red")


def upper_section(category, category_label, upper_label, total_label):
    global Rolls
    global Turns
    global DiceNo
    global Upper_Score
    global Total_score
    global Is_chosen

    if category == ones and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        ones_score = DiceNo.count(1)
        Upper_Score += ones_score
        Total_score += ones_score
        category_label["text"] = ones_score
        upper_label["text"] = Upper_Score
        total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)
    elif category == twos and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        twos_score = DiceNo.count(2) * 2
        Upper_Score += twos_score
        Total_score += twos_score
        category_label["text"] = twos_score
        upper_label["text"] = Upper_Score
        total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)
    elif category == threes and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        threes_score = DiceNo.count(3) * 3
        Upper_Score += threes_score
        Total_score += threes_score
        category_label["text"] = threes_score
        upper_label["text"] = Upper_Score
        total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)
    elif category == fours and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        fours_score = DiceNo.count(4) * 4
        Upper_Score += fours_score
        Total_score += fours_score
        category_label["text"] = fours_score
        upper_label["text"] = Upper_Score
        total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)
    elif category == fives and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        fives_score = DiceNo.count(5) * 5
        Upper_Score += fives_score
        Total_score += fives_score
        category_label["text"] = fives_score
        upper_label["text"] = Upper_Score
        total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)
    elif category == sixes and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        sixes_score = DiceNo.count(6) * 6
        Upper_Score += sixes_score
        Total_score += sixes_score
        category_label["text"] = sixes_score
        upper_label["text"] = Upper_Score
        total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)


def lower_section(category, category_label, lower_label, total_label):
    global Rolls
    global Turns
    global DiceNo
    global Lower_score
    global Is_chosen
    global Total_score

    if category == tok and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        if DiceNo.count(1) >= 3 or DiceNo.count(2) >= 3 or DiceNo.count(3) >= 3 or \
                DiceNo.count(4) >= 3 or DiceNo.count(5) >= 3 or DiceNo.count(6) >= 3:
            tok_total = sum(DiceNo)
            Lower_score += tok_total
            Total_score += tok_total
            category_label["text"] = tok_total
            lower_label["text"] = Lower_score
            total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)

    elif category == fok and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        if DiceNo.count(1) >= 4 or DiceNo.count(2) >= 4 or DiceNo.count(3) >= 4 or \
                DiceNo.count(4) >= 4 or DiceNo.count(5) >= 4 or DiceNo.count(6) >= 4:
            fok_total = sum(DiceNo)
            Lower_score += fok_total
            Total_score += fok_total
            category_label["text"] = fok_total
            lower_label["text"] = Lower_score
            total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)

    elif category == fh and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        sorted_dice = sorted(DiceNo)
        if sorted_dice.count(sorted_dice[0]) == 3 and sorted_dice.count(sorted_dice[3]) == 2:
            fh_total = 25
            Lower_score += fh_total
            Total_score += fh_total
            category_label["text"] = fh_total
            lower_label["text"] = Lower_score
            total_label["text"] = Total_score
        elif sorted_dice.count(sorted_dice[0]) == 2 and sorted_dice.count(sorted_dice[2]) == 3:
            fh_total = 25
            Lower_score += fh_total
            Total_score += fh_total
            category_label["text"] = fh_total
            lower_label["text"] = Lower_score
            total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)
    elif category == ss and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        sorted_dice1 = sorted(DiceNo)
        if sorted_dice1[0] + 1 == sorted_dice1[1] and sorted_dice1[1] + 1 == sorted_dice1[2] and \
                sorted_dice1[2] + 1 == sorted_dice1[3]:
                ss_total = 30
                Lower_score += ss_total
                Total_score += ss_total
                category_label["text"] = ss_total
                lower_label["text"] = Lower_score
                total_label["text"] = Total_score
        elif sorted_dice1[1] + 1 == sorted_dice1[2] and sorted_dice1[2] + 1 == sorted_dice1[3] and \
                sorted_dice1[3] + 1 == sorted_dice1[4]:
                ss_total = 30
                Lower_score += ss_total
                Total_score += ss_total
                category_label["text"] = ss_total
                lower_label["text"] = Lower_score
                total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)

    elif category == ls and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        if DiceNo.count(1) == 1 and DiceNo.count(2) == 1 and DiceNo.count(3) == 1 and DiceNo.count(4) == 1 and \
                DiceNo.count(5) == 1:
                    ls_total = 40
                    Lower_score += ls_total
                    Total_score += ls_total
                    category_label["text"] = ls_total
                    lower_label["text"] = Lower_score
                    total_label["text"] = Total_score
        elif DiceNo.count(2) == 1 and DiceNo.count(3) == 1 and DiceNo.count(4) == 1 and DiceNo.count(5) == 1 and \
                DiceNo.count(6) == 1:
                    ls_total = 40
                    Lower_score += ls_total
                    Total_score += ls_total
                    category_label["text"] = ls_total
                    lower_label["text"] = Lower_score
                    total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)

    elif category == yah and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        if DiceNo.count(1) == 5 or DiceNo.count(2) == 5 or DiceNo.count(3) == 5 or \
                DiceNo.count(4) == 5 or DiceNo.count(5) == 5 or DiceNo.count(6) == 5:
            yah_total = 50
            Lower_score += yah_total
            Total_score += yah_total
            category_label["text"] = yah_total
            lower_label["text"] = Lower_score
            total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)

    elif category == chance and Is_chosen is False:
        category.configure(bg="blue", state=DISABLED)
        Is_chosen = True
        chance_total = sum(DiceNo)
        Lower_score += chance_total
        Total_score += chance_total
        category_label["text"] = chance_total
        lower_label["text"] = Lower_score
        total_label["text"] = Total_score
        reset_dice(Dice1, Dice2, Dice3, Dice4, Dice5, Roll)


def reset_dice(die1, die2, die3, die4, die5, roll_die):
    global Dice1_keep
    global Dice2_keep
    global Dice3_keep
    global Dice4_keep
    global Dice5_keep
    global Is_chosen
    global Turns
    global Rolls

    Turns += 1
    Rolls = 1
    die1.configure(state=DISABLED, bg=dice_colour)
    Dice1_keep = False
    die2.configure(state=DISABLED, bg=dice_colour)
    Dice2_keep = False
    die3.configure(state=DISABLED, bg=dice_colour)
    Dice3_keep = False
    die4.configure(state=DISABLED, bg=dice_colour)
    Dice4_keep = False
    die5.configure(state=DISABLED, bg=dice_colour)
    Dice5_keep = False
    roll_die.configure(state=NORMAL, bg=roll_colour)


def change_dice(die1, die2, die3, die4, die5, roll_die):
    die1.configure(state=NORMAL)
    die2.configure(state=NORMAL)
    die3.configure(state=NORMAL)
    die4.configure(state=NORMAL)
    die5.configure(state=NORMAL)
    roll_die.configure(state=NORMAL)


def restart():
    restart1 = tkinter.messagebox.askquestion("Restart", "Would you like to restart?")
    if restart1 == "yes":
        print("Restarting")
    elif restart1 == "no":
        tk.quit()


tk.mainloop()
