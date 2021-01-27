from tkinter import *
import random

expression = ""
information = 'Press +,  -,  *  or / to start test'
input_answer = ""
IC_status = ""
setting_num = ""
mode = None
range_set = False
allow_set = False
range_AS = 100
range_T = 10
range_D = 100
a = 0
b = 0
total_Q = 0
correct_Q = 0

# functions
def input_options(number, message):
    global information, mode, input_answer, allow_set
    k = number
    if k == '+':
        mode = 0
        input_answer = ""
        information ='Addition: "Que" --- start; "Set" --- set range'
    if k == '-':
        mode = 1
        input_answer = ""
        information = 'Subtraction: "Que" --- start; "Set" --- set range'
    if k == '*':
        mode = 2
        input_answer = ""
        information = 'Multiplication: "Que" --- start; "Set" --- set range'
    if k == '/':
        mode = 3
        input_answer = ""
        information = 'Division: "Que" --- start; "Set" --- set range'
    message.set(information)

def show_question(mode, equation, message): # Que
    global expression, a, b, input_answer, total_Q, information, range_AS, range_D, range_T, setting_num, range_set
    input_mode = mode
    input_answer = ""
    if input_mode == 0: # Addition
        a = random.randrange(0, range_AS)
        b = random.randrange(0, range_AS)
        while a + b > range_AS:
            a = random.randrange(0, range_AS)
            b = random.randrange(0, range_AS)
        total_Q += 1
        information = 'Input answer, and press "Ent"'
        expression = str(a) + '+' + str(b) + '='
    if input_mode == 1: # Subtraction
        a = random.randrange(0, range_AS)
        b = random.randrange(0, range_AS)
        total_Q += 1
        information = 'Input answer, and press "Ent"'
        if a > b:
            expression = str(a) + '-' + str(b) + '='
        else:
            expression = str(b) + '-' + str(a) + '='
    if input_mode == 2: # Multiplication
        a = random.randrange(1, range_T)
        b = random.randrange(1, range_T)
        total_Q += 1
        information = 'Input answer, and press "Ent"'
        expression = str(a) + '*' + str(b) + '='
    if input_mode == 3: # Division
        a = random.randrange(1, range_D)
        b = random.randrange(1, range_D)
        k = round(a/b)
        while k<2:
            a = random.randrange(1, range_D)
            b = random.randrange(1, range_D)
            k = round(a / b)
        a = k*b
        total_Q += 1
        information = 'Input answer, and press "Ent"'
        expression = str(a) + '/' + str(b) + '='
    if input_mode == None:
        information = 'Press +,  -,  *  or / to start test'
        expression = ""
    message.set(information)
    equation.set(expression)

def clear_input(equation): # Clr
    global expression, input_answer, information
    expression = ""
    input_answer = ""
    equation.set(expression)

def setting_range(equation, message): # Set
    global information, range_set
    info_set = 'Enter the upper limit, and press "Ent"'
    mess_set = 'Range: ?'
    range_set = True
    equation.set(mess_set)
    message.set(info_set)


def delete_input(equation): # Del
    global expression, input_answer
    if "rect" in expression:
        pass
    else:
        expression = expression.replace(input_answer, '')
        input_answer = ""
    equation.set(expression)

def input_number(number, equation):
   # accessing the global expression variable
   global expression, input_answer, number_ctr, setting_num, range_set
   input_answer = input_answer + str(number)
   if "rect" in expression:
       pass
   elif expression != "":
        expression = expression + str(number)
   else:
       pass

   if range_set:
       setting_num = setting_num + str(number)
       equation.set(setting_num)
   else:
        equation.set(expression)

def evaluate(mode, equation, message): # Enter
    global expression, a, b, input_answer, correct_Q, total_Q, IC_status, information, range_set, range_AS, range_D, range_T, setting_num
    input_mode = mode
    if range_set:
        if input_mode == 0 or input_mode == 1:
            range_AS = int(setting_num)
        elif input_mode == 2:
            range_T = int(setting_num)
        elif input_mode == 3:
            range_D = int(setting_num)
        else:
            pass
        information = 'Range is set, press "Que" to start test'
        expression = 'Range: ' + setting_num
        range_set = False
        setting_num = ""

    else:
        if input_mode == None:
            information = 'Press +,  -,  *  or / to start test'
        elif expression == "":
            information = 'Press "Que" to get a question'
        elif "rect" in expression:
            information = 'Press "Que" to get next question'
        elif input_answer == "":
            information = 'Enter your answer'
        else:
            if input_mode == 0:
                c = a + b
                if str(c) == input_answer:
                    IC_status = '       Correct'
                    correct_Q += 1
                else:
                    IC_status = '       Incorrect'
            elif input_mode == 1:
                if a > b:
                    c = a - b
                else:
                    c = b - a
                if str(c) == input_answer:
                    IC_status = '       Correct'
                    correct_Q += 1
                else:
                    IC_status = '       Incorrect'
            elif input_mode == 2:
                c = a * b
                if str(c) == input_answer:
                    IC_status = '       Correct'
                    correct_Q += 1
                else:
                    IC_status = '       Incorrect'
            elif input_mode == 3:
                c = a / b
                if str(c) == input_answer:
                    IC_status = '       Correct'
                    correct_Q += 1
                else:
                    IC_status = '       Incorrect'
            else:
                expression = ""
            result = correct_Q / total_Q
            percentage = round((result * 100), 2)
            information = 'Total: ' + str(total_Q) + '      ' + 'Correct: ' + str(correct_Q) + '      ' + 'Your score: ' + str(percentage) + '%'
            expression = expression + IC_status
        IC_status = ""
    message.set(information)
    equation.set(expression)

# creating the GUI
def gui():
   # main window
   window = Tk()
   # setting the title of GUI window
   window.title("Math Quize for Kids")
   # set the configuration of GUI window
   # varible class instantiation
   equation = StringVar()
   # input field for the expression
   input_field = Entry(window, font=('arial', 20, 'bold'), textvariable=equation, bd=10, insertwidth=4, bg='powder blue', justify='left').grid(columnspan=4, ipadx=190, ipady=8)
   message = StringVar()
   display_field = Entry(window, font=('arial', 20, 'bold'), textvariable=message, bd=10, insertwidth=4, bg='white', justify='left').grid(column=0, row=6, columnspan=4, ipadx=190, ipady=8)

   message.set(information)
   equation.set("")

   # creating buttons and placing them at respective positions
   _1 = Button(window, text='1', fg='black', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_number(1, equation), height=1, width=10).grid(row=1, column=0)
   _2 = Button(window, text='2', fg='black', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_number(2, equation), height=1, width=10).grid(row=1, column=1)
   _3 = Button(window, text='3', fg='black', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_number(3, equation), height=1, width=10).grid(row=1, column=2)
   _4 = Button(window, text='4', fg='black', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_number(4, equation), height=1, width=10).grid(row=2, column=0)
   _5 = Button(window, text='5', fg='black', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_number(5, equation), height=1, width=10).grid(row=2, column=1)
   _6 = Button(window, text='6', fg='black', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_number(6, equation), height=1, width=10).grid(row=2, column=2)
   _7 = Button(window, text='7', fg='black', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_number(7, equation), height=1, width=10).grid(row=3, column=0)
   _8 = Button(window, text='8', fg='black', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_number(8, equation), height=1, width=10).grid(row=3, column=1)
   _9 = Button(window, text='9', fg='black', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_number(9, equation), height=1, width=10).grid(row=3, column=2)
   _0 = Button(window, text='0', fg='black', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_number(0, equation), height=1, width=10).grid(row=4, column=0)
   plus = Button(window, text='+', fg='blue', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_options('+', message), height=1, width=10).grid(row=1, column=3)
   minus = Button(window, text='-', fg='blue', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_options('-', message), height=1, width=10).grid(row=2, column=3)
   multiply = Button(window, text='*', fg='blue', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_options('*', message), height=1, width=10).grid(row=3, column=3)
   divide = Button(window, text='/', fg='blue', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: input_options('/', message), height=1, width=10).grid(row=4, column=3)
   evalu = Button(window, text='Ent', fg='red', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: evaluate(mode, equation, message), height=1, width=10).grid(row=4, column=2)
   enter = Button(window, text='Que', fg='green', bg='powder blue', font = ('arial', 20, 'bold'), bd=1, command=lambda: show_question(mode,equation, message), height=1, width=10).grid(row=4, column=1)
   delet = Button(window, text='Del', fg='purple', bg='powder blue', font = ('arial', 20, 'bold'), command=lambda: delete_input(equation), height=1, width=10).grid(row=5, column=1)
   clear = Button(window, text='Clr', fg='purple', bg='powder blue', font = ('arial', 20, 'bold'), command=lambda: clear_input(equation), height=1, width=10).grid(row=5, column=0)
   setting = Button(window, text='Set', fg='blue', bg='powder blue', font=('arial', 20, 'bold'), command=lambda: setting_range(equation, message), height=1, width=10).grid(row=5, column=3)
   # showing the GUI
   window.mainloop()


# start of the program
if __name__ == '__main__':
      gui()