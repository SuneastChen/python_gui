from tkinter import *
import tkinter.simpledialog    as dl
import tkinter.messagebox as mb
root=Tk()      #tkinter必须省略
w=Label(root,text="")
w.pack()


mb.showinfo("welcome","欢迎来到我的游戏世界!")
number=9



for i in range(6):
    guess=dl.askinteger("输入框标题","请猜一个数字")
    if guess==number:
        mb.showinfo("bt","你猜对了!")
        break
    elif guess>number:
        mb.showinfo("bt","大了,大了!你还有%d次机会"%(5-i))
        
    else: 
        mb.showinfo("bt","小了,小了!你还有%d次机会"%(5-i))
        
