'''
Python program to create a GUI
calculator using Tkinter
Here begining the program
'''
# import everything from tkinter module and math
from tkinter import * 
# from math import *

# create a GUI window
view = Tk()

# StringVar() is the variable class
# we create an instance of this class
screen_items = StringVar()

# declare the number variable globally
numbers = ""

def main():

    width = 400  # The width and height
    height = 560 #  that my program will have
    
    #set the title of GUI window
    view.title("Kevin's Calculator")

    # set the configuration of GUI window
    view.geometry(f"{width}x{height}")

    # set that does not get wider or taller
    view.resizable(False, False)

    # set the background colour of GUI window
    view.configure(bg="#59B2F5")

    #Set the buttons color 
    color_btn = "#FFF"
    #Set the buttons width 
    len_w = 10
    #Set the buttons height
    len_h = 3 
   
    # create the text entry box for
    # showing the numbers and give it a font type 
    screen = Entry(view, font=("Helvetica",20, "bold"), width=22, borderwidth=10, \
            background="#FFFFFF", textvariable=screen_items)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    screen.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

    '''
    Here I declare the 4 variables that each one of them 
    will execute a function in the calculator, to the function click() I give the parameter 
    of numbers which will later be passed by reference when it is declared below. the buttons_rows 
    function had 4 parameters, the window or (GUI) where it will be, the color, the height and when 
    the button is declared it will be indicated by the grid method in which place or position it 
    will be located.
    '''
    clear_screen()
    click(numbers)
    result()
    buttons_rows(view, color_btn, len_w, len_h)
    
    # start the GUI
    view.mainloop()


# Function to clear the contents
# of text entry box
def clear_screen():
    global numbers
    numbers = ""
    #when they click the clear button (C) it will make all
    # the elements in the screen be erased
    screen_items.set(numbers)

# Function to clear the contents
# of text entry box
def click(n):
    # point out the globl numbers variable
    global numbers 

    # concatenation of string
    numbers += str(n)

    # update the numbers by using set method
    screen_items.set(numbers)

# Function to evaluate the final expression
def result():

    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error

    try: 
        global numbers

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        result = str(eval(numbers))
        screen_items.set(result)
        # initialize the expression variable
        # by empty string
        numbers = ""

        # if error is generate then handle
        # by the except block
    except:                                                 	
        if numbers == ZeroDivisionError:                         
           raise screen_items.set("ERROR")
        numbers = ""
   

# create a Buttons and place at a particular
# location inside the root window .
# when user press the button, the command or
# function affiliated to that button is executed .
def buttons_rows(display, color, len_w, len_h): 

    #firts row buttons
    btn_1 = Button(display, text="1", bg=color, width=len_w, height=len_h, command=lambda:click(1))\
        .grid(row=1, column=0, pady=10,) 
    btn_2 = Button(display, text="2", bg=color, width=len_w, height=len_h, command=lambda:click(2))\
        .grid(row=1, column=1, pady=10,) 
    btn_3 = Button(display, text="3", bg=color, width=len_w, height=len_h, command=lambda:click(3)).grid(row=1, column=2, pady=10,) 
    
    btn_clear = Button(display, text="C", bg=color, width=len_w, height=len_h, command=lambda:clear_screen())\
        .grid(row=1, column=3, pady=10,)     
    # Second row buttons
    btn_4 = Button(display, text="4", bg=color, width=len_w, height=len_h, command=lambda:click(4))\
    .grid(row=2, column=0, pady=10,) 
    btn_5 = Button(display, text="5", bg=color, width=len_w, height=len_h, command=lambda:click(5))\
    .grid(row=2, column=1, pady=10) 
    btn_6 = Button(display, text="6", bg=color, width=len_w, height=len_h, command=lambda:click(6))\
    .grid(row=2, column=2, pady=10) 
    btn_pi = Button(display, text="π", bg=color, width=len_w, height=len_h, command=lambda:click("pi"))\
    .grid(row=2, column=3, pady=10)     
    # Third row buttons        
    btn_7 = Button(display, text="7", bg=color, width=len_w, height=len_h, command=lambda:click(7))\
    .grid(row=3, column=0, pady=10) 
    btn_8 = Button(display, text="8", bg=color, width=len_w, height=len_h, command=lambda:click(8))\
    .grid(row=3, column=1, pady=10) 
    btn_9 = Button(display, text="9", bg=color, width=len_w, height=len_h, command=lambda:click(9))\
    .grid(row=3, column=2, pady=10) 
    btn_subt = Button(display, text="-", bg=color, width=len_w, height=len_h, command=lambda:click("-"))\
    .grid(row=3, column=3, pady=10,)     
    # Fourth row buttons 
    btn_sum = Button(display, text="+", bg=color, width=len_w, height=len_h, command=lambda:click("+"))\
    .grid(row=4, column=0, pady=10,) 
    btn_0 = Button(display, text="0", bg=color, width=len_w, height=len_h, command=lambda:click(0))\
    .grid(row=4, column=1, pady=10,) 
    btn_mult = Button(display, text="X", bg=color, width=len_w, height=len_h, command=lambda:click("*"))\
    .grid(row=4, column=2, pady=10,) 
    btn_div = Button(display, text="÷", bg=color, width=len_w, height=len_h, command=lambda:click("/"))\
    .grid(row=4, column=3, pady=10)     
    #Fiveth row buttons 
    btn_sqrt = Button(display, text="√", bg=color, width=len_w, height=len_h, command=lambda:click("sqrt"))\
    .grid(row=5, column=0, pady=10,) 
    btn_dot = Button(display, text=".", bg=color, width=len_w, height=len_h, command=lambda:click("."))\
    .grid(row=5, column=1, pady=10,) 
    btn_exp = Button(display, text="EXP", bg=color, width=len_w, height=len_h, command=lambda:click("exp"))\
    .grid(row=5, column=2, pady=10,) 
    btn_equal = Button(display, text="=", bg=color, width=len_w, height=len_h, command=lambda:result())\
    .grid(row=5, column=3, pady=10,)     
    # Sixth row buttons
    btn_letf_parent = Button(display, text="(", bg=color, width=len_w, height=len_h, command=lambda:click("("))\
    .grid(row=6, column=0, pady=10,) 
    btn_right_parent = Button(display, text=")", bg=color, width=len_w, height=len_h, command=lambda:click(")"))\
    .grid(row=6, column=1, pady=10,) 
    btn_mod = Button(display, text="%", bg=color, width=len_w, height=len_h, command=lambda:click("%"))\
    .grid(row=6, column=2, pady=10,) 
    btn_div = Button(display, text="LN", bg=color, width=len_w, height=len_h, command=lambda:click("log"))\
    .grid(row=6, column=3, pady=10,)        
                
if __name__ == "__main__":
    main()