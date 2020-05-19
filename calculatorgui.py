from tkinter import *
from addsub import add, sub
from multdiv import div, mult, mod
##pylint goes crazy here, dont worry about it
##the "*" makes creating any buttons or items much much easier. dont have to refence tkinter everytime.
window = Tk()

window.title("Calculator by Luke and Ben")

## this section contains the operation-------------------------------------------------------

topframe = Frame(window) ##stays on the top of application
topframe.pack(side = TOP)

entrytextT1 = StringVar() ## allows it to be updated
entrytext1 = Label(topframe, textvariable=entrytextT1)
entrytext1.pack(side = LEFT)

equalsign = Label(topframe, text="=")
equalsign.pack(side = LEFT)

outputtextT1 = StringVar()
outputtext = Label(topframe, textvariable=outputtextT1)
outputtext.pack(side = LEFT)

firstNumber = str()
operation = []
secondNumber = str()

##------------------------------------------------------------------------------------------

def clean(): #cleans everything in terms of varaibles.
    global firstNumber
    global secondNumber
    entrytextT1.set("")
    operation.clear()
    outputtextT1.set("")
    firstNumber = str()
    secondNumber = str()

def changeOperation(op):##Checks if anything is in the operation list and stops them from adding anymore than 1 operation.
    if operation:
        print("Only one operation at a time.")
    if not operation:
        operation.append(op)
        z = entrytextT1.get()
        z += str(op) 
        entrytextT1.set(z)

def changeEntryAndVars(btnNum): ##determines what the first number and what the second number is. updates in terminal every button press
    if not operation: ##if nothing is in the list
        global firstNumber
        s = firstNumber
        s += str(btnNum)
        firstNumber = s
        print("This is the first number: "+ str(firstNumber))
    if operation: ##if anything is in the list
        global secondNumber
        t = secondNumber
        t += str(btnNum)
        secondNumber = t
        print("This is the second number: "+ str(secondNumber))
    z = entrytextT1.get()
    z += str(btnNum) ##updates the text on left side of screen.
    entrytextT1.set(z)

def solve(): ## prints what operation it is doing and what the answer is.
    print(operation)
    global firstNumber ##uses global varaibles instead of local
    global secondNumber
    if "+" in operation:
        print(add(int(firstNumber), int(secondNumber)))
        output = add(int(firstNumber), int(secondNumber))
    elif "-" in operation:
        print(sub(int(firstNumber), int(secondNumber)))
        output = sub(int(firstNumber), int(secondNumber))
    elif "*" in operation:
        print(mult(int(firstNumber), int(secondNumber)))
        output = mult(int(firstNumber), int(secondNumber))
    elif "/" in operation:
        print(div(int(firstNumber), int(secondNumber)))
        output = div(int(firstNumber), int(secondNumber))
    elif "%" in operation:
        print(mod(int(firstNumber), int(secondNumber)))
        output = mod(int(firstNumber), int(secondNumber))
    else:
        print("Invalid input.")
    outputtextT1.set(output)
    operation.clear()
    entrytextT1.set("") ## cleans text after solving
    firstNumber = str()
    secondNumber = str()



## this one contains the functions of math--------------------------------------------------

leftframe = Frame(window) #stays on very left side of window
leftframe.pack(side = LEFT)

addbtn = Button(leftframe, text="+", width=2, height=1, command=lambda: changeOperation("+"))
addbtn.grid(column=4, row=1)

subtract = Button(leftframe, text="-", width=2, height=1, command=lambda: changeOperation("-"))
subtract.grid(column=4, row=2) 

multiply = Button(leftframe, text="*", width=2, height=1, command=lambda: changeOperation("*"))
multiply.grid(column=4, row=3) 

divide = Button(leftframe, text="/", width=2, height=1, command=lambda: changeOperation("/"))
divide.grid(column=4, row=4) 

modbtn = Button(leftframe, text="mod", width=2, height=1, command=lambda: changeOperation("%"))
modbtn.grid(column=3, row=4) 

equal = Button(leftframe, text="=", width=4, height=1, bg="lime", command=lambda: solve())
equal.grid(column=5, row=4) 

clear = Button(leftframe, text="Clear", bg="red", command=lambda: clean())
clear.grid(column=5, row=3) 
##--------------------------------------------------------------------------------------------
## this one contains numbers------------------------------------------------------------------



btn1 = Button(leftframe, text="1", width=2, height=1, command=lambda: changeEntryAndVars(1))
btn1.grid(column=1, row=1) ##numbers are organized by column and rows here

btn2 = Button(leftframe, text="2", width=2, height=1, command=lambda: changeEntryAndVars(2))
btn2.grid(column=2, row=1)

btn3 = Button(leftframe, text="3", width=2, height=1, command=lambda: changeEntryAndVars(3))
btn3.grid(column=3, row=1)

btn4 = Button(leftframe, text="4", width=2, height=1, command=lambda: changeEntryAndVars(4))
btn4.grid(column=1, row=2)

btn5 = Button(leftframe, text="5", width=2, height=1, command=lambda: changeEntryAndVars(5))
btn5.grid(column=2, row=2)

btn6 = Button(leftframe, text="6", width=2, height=1, command=lambda: changeEntryAndVars(6))
btn6.grid(column=3, row=2)

btn7 = Button(leftframe, text="7", width=2, height=1, command=lambda: changeEntryAndVars(7))
btn7.grid(column=1, row=3)

btn8 = Button(leftframe, text="8", width=2, height=1, command=lambda: changeEntryAndVars(8))
btn8.grid(column=2, row=3)

btn9 = Button(leftframe, text="9", width=2, height=1, command=lambda: changeEntryAndVars(9))
btn9.grid(column=3, row=3)

btn0 = Button(leftframe, text="0", width=2, height=1, command=lambda: changeEntryAndVars(0))
btn0.grid(column=2, row=4)

btnNeg = Button(leftframe, text="neg", width=2, height=1, command= lambda: changeEntryAndVars("-"))
btnNeg.grid(column=1, row=4)

##--------------------------------------------------------------------------------------------


window.mainloop()