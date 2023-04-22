from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btncleatrDisplay():
    global operator
    operator = ""
    text_input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator =""


cal = Tk()
cal.title("Calculator")
operator = ""
text_input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue",
                   justify='right').grid(columnspan=4)

btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7", bg="powder blue",
              command=lambda: btnClick(7)).grid(row=1, column=0)

btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", bg="powder blue",
              command=lambda: btnClick(8)).grid(row=1, column=1)

btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", bg="powder blue",
              command=lambda: btnClick(9)).grid(row=1, column=2)

addition = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="+", bg="powder blue",
                  command=lambda: btnClick("+")).grid(row=1, column=3)

################################### kalyan #####################################################################

btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4", bg="powder blue",
              command=lambda: btnClick(4)).grid(row=2, column=0)

btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5", bg="powder blue",
              command=lambda: btnClick(5)).grid(row=2, column=1)

btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", bg="powder blue",
              command=lambda: btnClick(6)).grid(row=2, column=2)

multiply = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", bg="powder blue",
                  command=lambda: btnClick("*")).grid(row=2, column=3)

##################################++++ kalyan ++++++++++++++++++==================++++++++++++++====================+++++++++++++++++++++++++++++++++++

btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20, 'bold'),text="1",bg="powder blue",
            command=lambda :btnClick(1)).grid(row=3,column=0)

btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20, 'bold'),text="2",bg="powder blue",
            command=lambda :btnClick(2)).grid(row=3,column=1)

btn3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",
            command=lambda :btnClick(3)).grid(row=3,column=2)

subtraction=Button (cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20, 'bold'),text="-", bg="powder blue",
                    command=lambda : btnClick("-")).grid(row=3,column=3)

#######################++++++++++++++++++++++++++++++++++++++++++######################################++++++++++++++++++++++++++++++

btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",
            command=lambda :btnClick(0)).grid(row=4,column=0)

btncleatr=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="powder blue",
                 command=lambda :btncleatrDisplay()).grid(row=4,column=1)

btnEquals=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",
                 command=btnEqualsInput).grid(row=4,column=2)

Division=Button(cal,bg="powder blue",fg="black",pady=16,padx=16,bd=8,font=('black',20,'bold'),text="/",
command=lambda :btnClick("/")).grid(row=4,column=3)

#######################################+++++++++++++++++++++++++++++++++++++++++++++++++########################################################

#btn00=Button(cal,bg="powder blue",pady=16,padx=16,fg=8,font=('black',20,'bold'),text="00",command=lambda :btnClick("00")).grid(row=4,column=3)
cal.mainloop()
