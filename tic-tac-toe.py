import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk

LARGEFONT = ("Arial",18)
NORMALFONT = ("Arial",12)

class TicTacToe(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self,default="icon.ico")

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (MainMenu,NewGame,GameHelp):
            frame = F(container,self)
            self.frames[F] = frame
            frame.configure(background="#161616")
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainMenu(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        img = ImageTk.PhotoImage(Image.open("ttt_logo.png"))
        label = tk.Label(self,image=img,borderwidth=0,highlightthickness=0,relief="sunken")
        label.image = img
        label.pack(padx=10,pady=40)

        label2 = tk.Label(self,text="MAIN MENU",font=LARGEFONT,bg="#161616",fg="white")
        label2.pack(padx=10,pady=30)

        button1 = ttk.Button(self,text="NEW GAME",command=lambda: controller.show_frame(NewGame))
        button1.pack(padx=10,pady=10)
        button3 = ttk.Button(self,text="HELP",command=lambda: controller.show_frame(GameHelp))
        button3.pack(padx=10,pady=10)
        button4 = ttk.Button(self,text="EXIT",command=lambda: exit(0))
        button4.pack(padx=10,pady=10)

class NewGame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        p1=tk.StringVar()
        p2=tk.StringVar()
        flag=0
        bclick=True

        def disable():
            button1.configure(state=tk.DISABLED)
            button2.configure(state=tk.DISABLED)
            button3.configure(state=tk.DISABLED)
            button4.configure(state=tk.DISABLED)
            button5.configure(state=tk.DISABLED)
            button6.configure(state=tk.DISABLED)
            button7.configure(state=tk.DISABLED)
            button8.configure(state=tk.DISABLED)
            button9.configure(state=tk.DISABLED)

        def win_check():
            #to check who wins
            if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
                button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
                button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
                button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
                button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
                button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
                button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
                button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
                button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
                disable()
                showinfo("Tic-Tac-Toe", p1)
            elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
                button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
                button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
                button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
                button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
                button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
                button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
                button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
                button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
                disable()
                showinfo("Tic-Tac-Toe", p2)
            elif (flag == 8):
                disable()
                showinfo("Tic-Tac-Toe","It ends in a tie")

        global button
        button = tk.StringVar()

        def btnClick(buttons):
            nonlocal bclick,p1Name,p2Name,flag,p1,p2
            if buttons["text"] == " " and bclick == True:
                buttons["text"] = "X"
                bclick = False
                p1 = p1Name.get() + " Wins!"
                win_check()
                flag = flag+1
            elif buttons["text"] == " " and bclick == False:
                buttons["text"] = "O"
                bclick = True
                p2 = p2Name.get() + " Wins!"
                win_check()
                flag = flag+1
            else:
                showinfo("Tic-Tac-Toe", "Button already Clicked!")

        def reset():
            nonlocal bclick,flag
            button1["text"] = " "
            button2["text"] = " "
            button3["text"] = " "
            button4["text"] = " "
            button5["text"] = " "
            button6["text"] = " "
            button7["text"] = " "
            button8["text"] = " "
            button9["text"] = " "
            bclick = True
            flag = 0
            button1.configure(state=tk.NORMAL)
            button2.configure(state=tk.NORMAL)
            button3.configure(state=tk.NORMAL)
            button4.configure(state=tk.NORMAL)
            button5.configure(state=tk.NORMAL)
            button6.configure(state=tk.NORMAL)
            button7.configure(state=tk.NORMAL)
            button8.configure(state=tk.NORMAL)
            button9.configure(state=tk.NORMAL)

        #taking input through entry box
        p1Name = tk.Entry(self, textvariable=p1, bd=5)
        p1Name.grid(row=1, column=1, columnspan=8)
        p2Name = tk.Entry(self, textvariable=p2, bd=5)
        p2Name.grid(row=2, column=1, columnspan=8)

        #creates labels for Player 1 and Player 2
        label1 = tk.Label(self,text = " Player 1 (X)", height = 1, width = 8, bg="#161616", fg="white")
        label1.grid(row=1,column=0)
        label2 = tk.Label(self,text = " Player 2 (O)", height = 1, width = 8, bg="#161616", fg="white")
        label2.grid(row=2,column=0)

        #creates buttons 1 to 9
        button1 = tk.Button(self,text = " ",font='Times 20 bold',height=4,width=8,command=lambda: btnClick(button1))
        button1.grid(row=3,column=0)
        button2 = tk.Button(self,text = " ",font='Times 20 bold',height=4,width=8,command=lambda: btnClick(button2))
        button2.grid(row=3,column=1)
        button3 = tk.Button(self,text = " ",font='Times 20 bold',height=4,width=8,command=lambda: btnClick(button3))
        button3.grid(row=3,column=2)
        button4 = tk.Button(self,text = " ",font='Times 20 bold',height=4,width=8,command=lambda: btnClick(button4))
        button4.grid(row=4,column=0)
        button5 = tk.Button(self,text = " ",font='Times 20 bold',height=4,width=8,command=lambda: btnClick(button5))
        button5.grid(row=4,column=1)
        button6 = tk.Button(self,text = " ",font='Times 20 bold',height=4,width=8,command=lambda: btnClick(button6))
        button6.grid(row=4,column=2)
        button7 = tk.Button(self,text = " ",font='Times 20 bold',height=4,width=8,command=lambda: btnClick(button7))
        button7.grid(row=5,column=0)
        button8 = tk.Button(self,text = " ",font='Times 20 bold',height=4,width=8,command=lambda: btnClick(button8))
        button8.grid(row=5,column=1)
        button9 = tk.Button(self,text = " ",font='Times 20 bold',height=4,width=8,command=lambda: btnClick(button9))
        button9.grid(row=5,column=2)

        button10 = ttk.Button(self,text="Reset Game",command=lambda: reset())
        button10.grid(row=6,column=1,padx=10,pady=10)

        button11 = ttk.Button(self,text="Back to Main Menu",command=lambda: controller.show_frame(MainMenu))
        button11.grid(row=7,column=1,padx=10,pady=10)

class GameHelp(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="HELP",font=LARGEFONT,bg="#161616",fg="white")
        label.pack(padx=10,pady=30)
        
        rules = "Welcome to Tic-Tac-Toe\nThe Rules of the game are pretty simple\nThe aim is to make a straight line out of 3-O or 3-X"
        label = tk.Label(self,text=rules,font=NORMALFONT,bg="#161616",fg="white")
        label.pack(padx=10,pady=50)

        button1 = ttk.Button(self,text="Back to Main Menu",command=lambda: controller.show_frame(MainMenu))
        button1.pack()

app = TicTacToe()
app.title("tik-tac-toe")
app.resizable(width=False,height=False)
app.mainloop()