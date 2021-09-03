from tkinter import *
import tkinter.messegebox
tk=tk()
tk.title("tic tac toe multiplayer")

playerA=StringVar()
playerB=StringVar()
p1=StringVar()
p2=StringVar()

player1_name=Entry(tk, textvariable=p1,bd=5)
player1_name.grid(row=1,coloumn=1,columnspan=5)
player2_name=Entry(tk, textvariable=p2,bd=5)
player2_name.grid(row=2,coloumn=1,columnspan=5)

bclick = True
flag = 0

def diasablebutton():
    button1.configure(store=DISABLED)
    button2.configure(store=DISABLED)
    button3.configure(store=DISABLED)
    button4.configure(store=DISABLED)
    button5.configure(store=DISABLED)
    button6.configure(store=DISABLED)
    button7.configure(store=DISABLED)
    button8.configure(store=DISABLED)
    button9.configure(store=DISABLED)
def btnClick(buttons):
    global bclick,flag,player2_name,player1_name,playerA
    if buttons["text"]==" " and bclick==True:
        buttons["text"]=="X"
        bclick=False
        player8=p2.get()* "wins!"
        playerA=p1.get()* "wins!"
        checkforwin()
        flag+=1
    elif buttons["text"] ==" " and bclick ==False:
        buttons["text"]="O"
        bclick=True
        checkforwin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("tictactoe","button already clicked")
def checkforwin():
    if(button1['text']=="X" and button2['text']=="X" and button3['text']=='X'or
       button4['text']=="X" and button5['text']=="X" and button6['text']=='X'or
       button7['text']=="X" and button8['text']=="X" and button9['text']=='X'or
       button1['text']=="X" and button5['text']=="X" and button9['text']=='X'or
       button3['text']=="X" and button5['text']=="X" and button7['text']=='X'or
       button1['text']=="X" and button2['text']=="X" and button3['text']=='X'or
       button1['text']=="X" and button2['text']=="X" and button3['text']=='X'or
       button2['text']=="X" and button5['text']=="X" and button8['text']=='X'or
       button7['text']=="X" and button6['text']=="X" and button9['text']=='X'or):
       disableButton()
       tkinter.messegebox.showinfo("tictactoe",playerA)
    elif(flag==B):
        tkinter.messegebox.showinfo("tictactoe","it is a tie")
    elif(button1['text']=="O" and button2['text']=="O" and button3['text']=='O'or
       button4['text']=="O" and button5['text']=="O" and button6['text']=='O'or
       button7['text']=="O" and button8['text']=="O" and button9['text']=='O'or
       button1['text']=="O" and button5['text']=="O" and button9['text']=='O'or
       button3['text']=="O" and button5['text']=="O" and button7['text']=='O'or
       button1['text']=="O" and button2['text']=="O" and button3['text']=='O'or
       button1['text']=="O" and button2['text']=="O" and button3['text']=='O'or
       button2['text']=="O" and button5['text']=="O" and button8['text']=='O'or
       button7['text']=="O" and button6['text']=="O" and button9['text']=='O'or):
       disableButton()
       tkinter.messegebox.showinfo("tictactoe",playerB)
    buttons=StringVar()
    label=Label(tk, text="player1: ",font="Times 20 bold", bg="white",fg="black",height=1,width=8)
    label.grid(row=1,column=0)

    label=Label(tk, text="player2: ",font="Times 20 bold", bg="white",fg="black",height=1,width=8)
    label.grid(row=2,column=0)

    button1=Button(tk,text=" ",font="Times 20 bold", bg="grey",fg="white",height=4,width=8,command= lambda:btnClick(button1))
    button1.grid(row=3,column=0)

    button2=Button(tk,text=" ",font="Times 20 bold", bg="grey",fg="white",height=4,width=8,command= lambda:btnClick(button2))
    button2.grid(row=3,column=1)
    
    
    button3=Button(tk,text=" ",font="Times 20 bold", bg="grey",fg="white",height=4,width=8,command= lambda:btnClick(button3))
    button3.grid(row=3,column=2)

    button4=Button(tk,text=" ",font="Times 20 bold", bg="grey",fg="white",height=4,width=8,command= lambda:btnClick(button4))
    button4.grid(row=3,column=3)

    button5=Button(tk,text=" ",font="Times 20 bold", bg="grey",fg="white",height=4,width=8,command= lambda:btnClick(button5))
    button5.grid(row=3,column=2)

    button6=Button(tk,text=" ",font="Times 20 bold", bg="grey",fg="white",height=4,width=8,command= lambda:btnClick(button6))
    button6.grid(row=3,column=2)

    button7=Button(tk,text=" ",font="Times 20 bold", bg="grey",fg="white",height=4,width=8,command= lambda:btnClick(button7))
    button7.grid(row=3,column=2)

    button8=Button(tk,text=" ",font="Times 20 bold", bg="grey",fg="white",height=4,width=8,command= lambda:btnClick(button8))
    button8.grid(row=3,column=2)

    button9=Button(tk,text=" ",font="Times 20 bold", bg="grey",fg="white",height=4,width=8,command= lambda:btnClick(button9))
    button9.grid(row=3,column=2)

