# import modules needed GUI app building
from tkinter import *
from tkinter import messagebox


root = Tk()  #define tkinter instance
root.geometry("1350x600+0+0")  #set dimensions of window app
root.title("Data Storage") #set window app title
root.iconbitmap("data.ico") #set the title icon of window app
root.configure(background = "blue") #set the background color of window app

#set main Frame widgets
TopFrame = Frame(root, width = 1350, height = 50, bd=16, relief = "raise")
TopFrame.pack(side=TOP)
BottomFrame = Frame(root, width = 1350, height = 700, bd = 16, relief = "raise")
BottomFrame.pack(side=BOTTOM)

#set Label widget with title of converter app
labeltitle = Label(TopFrame, font = ("Arial", 32, "bold"), fg = "blue", text = "Computer Data Storage Unit Converter",
                       bd = 14).grid(row=0, column=0)

#set Frame widgets for leftFrame, rightFrame
frBottom1 = Frame(BottomFrame, width = 400, height = 300, relief = "raise")
frBottom1.pack(side=BOTTOM)

frBottom2 = Frame(BottomFrame, width = 900, height = 400, bd = 16,relief = "raise")
frBottom2.pack(side=BOTTOM)

# set Frame widgets for Radiobuttons
leftFrame = Frame(frBottom2, width = 1350, height = 400, bd = 16, relief = "raise")
leftFrame.pack(side=LEFT)
rightFrame = Frame(frBottom2, width = 1350, height = 400, bd = 16, relief = "raise")
rightFrame.pack(side=RIGHT)

#set Frame widgets for input value, output value and Convert, Exit and Reset buttons
frameButtons = Frame(frBottom1, width = 1350, height = 100, bd = 16, relief = "raise")
frameButtons.pack(side=BOTTOM)
resultButtons = Frame(frBottom1, width = 1350, height = 200, bd = 16, relief = "raise")
resultButtons.pack(side=BOTTOM)

#function that gives functionality to the Convert button 
#to perform the conversion from one measure to another
def calculate():
    
    if var1.get() == 1:
        val = float(value_input.get())
        res = val * 1024
        value_result.set(res)

    elif var1.get() == 2:
        val = float(value_input.get())
        res = val * 1048576 
        value_result.set(res)

    elif var1.get() == 3:
        val = float(value_input.get())
        res = val * 1073741824   
        value_result.set(res)

    elif var1.get() == 4:
        val = float(value_input.get())
        res = val * 1099469408151 
        value_result.set(res)

    elif var1.get() == 5:
        val = float(value_input.get())
        res = val * 0.0009765625  
        value_result.set(res)

    elif var1.get() == 6:
        val = float(value_input.get())
        res = val * 9.536743164063 * pow(10,-7) 
        value_result.set(res)

    elif var1.get() == 7:
        val = float(value_input.get())
        res = val * 9.313225746155 * pow(10,-10) 
        value_result.set(res)

    else:
        val = float(value_input.get())
        res = val * 9.095296263695 * pow(10,-13) 
        value_result.set(res)
        

# function that gives the Exit button the property to exit the application
def exit_command():
      ExitBox = messagebox.askquestion ("Exit Application","Do you want to exit the app?")
      if ExitBox == "yes":
          root.destroy()
        
def reset_command():
    value_input.set("")
    value_result.set("")
    
#declaring and setting of tkinter variables
var1 = IntVar()
value_input = IntVar()
value_result = IntVar()

value_input.set("")
value_result.set("")

# set Radiobutton widgets
KB_B = Radiobutton(leftFrame, text = "Kilobyte (KB) -> Byte (B) ", variable=var1, value=1,
                               font = ("Arial",12,"bold"), fg = "blue").grid(row=0, sticky=W)
MB_B = Radiobutton(leftFrame, text = "Megabyte (MB) -> Byte (B) ", variable=var1, value=2,
                               font = ("Arial",12,"bold"), fg = "blue").grid(row=1, sticky=W)
GB_B = Radiobutton(leftFrame, text = "Gigabyte GB) -> Byte (B) ", variable=var1, value=3,
                               font = ("Arial",12,"bold"), fg = "blue").grid(row=2, sticky=W)
TB_B = Radiobutton(leftFrame, text = "Terabyte (TB) -> Byte (B) ", variable=var1, value=4,
                               font = ("Arial",12,"bold"), fg = "blue").grid(row=3, sticky=W)

B_KB = Radiobutton(rightFrame, text = "Byte (B)  -> Kilobyte (KB)", variable=var1, value=5,
                               font = ("Arial",12,"bold"), fg = "blue").grid(row=0, sticky=W)
B_MB = Radiobutton(rightFrame, text = "Byte (B)  -> Megabyte (MB)", variable=var1, value=6,
                               font = ("Arial",12,"bold"), fg = "blue").grid(row=1, sticky=W)
B_GB = Radiobutton(rightFrame, text = "Byte (B)  -> Gigabyte GB)", variable=var1, value=7,
                               font = ("Arial",12,"bold"), fg = "blue").grid(row=2, sticky=W)
B_TB = Radiobutton(rightFrame, text = "Byte (B)  -> Terabyte (TB)", variable=var1, value=8,
                               font = ("Arial",12,"bold"), fg = "blue").grid(row=3, sticky=W)

#set Label widget and Entry widget for input value
lblInput = Label(resultButtons, font=("Arial", 14, "bold"), text = "Input value" ,
                     fg = "blue", bd = 16).grid(row=0, column=0, sticky=W)

lblEntry = Entry(resultButtons,  font=("Arial", 14, "bold"), bd= 5, width = 32, bg = "white", fg = "blue",
                      textvariable = value_input, relief = "sunken", justify = "center").grid(row=0, column=1)

#set Label widgets for output value
lblTextResult = Label(resultButtons, font=("Arial", 14, "bold"), text = "Output value" ,
                             fg = "blue", bd = 16).grid(row=2, column=0, sticky=W)
lblConvertedResult = Label(resultButtons, font=("Arial", 14, "bold"), bd= 5, width = 30, bg = "white", fg = "blue",
                                             textvariable = value_result, relief = "sunken").grid(row=2, column=1, sticky =W)

#set Convert, Exit and Reset buttons
ConvertButton = Button(frameButtons, font = ("Arial", 14, "bold"), pady=8, bd = 6 , fg = "blue",text = "Convert",
                                  bg = "white", width = 12, command=calculate).grid(row=0, column=0)
ExitButton = Button(frameButtons, font = ("Arial", 14, "bold"), pady=8, bd = 6 , fg = "blue",text = "Exit",
                                  bg = "white", width = 12, command=exit_command).grid(row=0, column=1)
ResetButton = Button(frameButtons, font = ("Arial", 14, "bold"), pady=8, bd = 6 , fg = "blue",text = "Reset",
                                  bg = "white", width = 12, command=reset_command).grid(row=0, column=2)


root.mainloop()
