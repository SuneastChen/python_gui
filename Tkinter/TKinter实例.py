import tkinter.messagebox
from tkinter import filedialog,colorchooser
#from tkinter import *      #后面可以不加tkinter

'''
print('------------------返回布尔类型-----------------')
a1=tkinter.messagebox.askokcancel('title..','确定发射导弹吗?')
print(a1)     #true
a1=tkinter.messagebox.askretrycancel('','你需要再试一次吗?')
print(a1)
a1=tkinter.messagebox.askyesno('','你是个好人吗?')
print(a1)
print('------------------其他消息框-----------------')
a1=tkinter.messagebox.askquestion('','你喜欢我吗?')
print(a1)    #yes or no
a1=tkinter.messagebox.showinfo('','2018新年快乐!')
print(a1)    #只有ok一个返回值
a1=tkinter.messagebox.showwarning('','你在偷懒!')
print(a1)    #只有ok一个返回值
a1=tkinter.messagebox.showerror("FishC Demo","出错啦！")
print(a1)    #只有ok一个返回值

a1=tkinter.messagebox.askokcancel('title..','确定发射导弹吗?',default='cancel',icon='error')



print('------------------文件对话框-----------------')
a2=tkinter.filedialog.askopenfilename()
print(a2)    #打开窗口-得到文件的路径加文件名
a3=tkinter.filedialog.asksaveasfilename()
print(a3)    #保存窗口-得到文件的路径加文件名


print('------------------文件对话框实例-----------------')
from tkinter import *      #后面可以不加tkinter
root = Tk()
def callback():
     fileName = filedialog.askopenfilename(filetypes=[('JPG','jpg'),('PNG','.png'),('PYTHON','.py')],initialdir='H:/图片/美女')
     print(fileName)
Button(root,text='打开文本',command=callback).pack()
mainloop()

print('------------------颜色选择对话框-----------------')

a3=colorchooser.askcolor()
print(a3)       #((255.99609375, 255.99609375, 255.99609375), '#ffffff')

print('------------------颜色选择对话框1-----------------')
from tkinter import *
root=Tk()
def callback():
    a3=colorchooser.askcolor()
    print(a3)
Button(root,text="选择颜色",command=callback).pack()
mainloop()


print('------------------第二个窗口,Label-----------------')
import tkinter as tk
root=tk.Tk()       #第二个k要小写
root.title('FishC Demo')
theLabel=tk.Label(root,text='我的第二个窗口!').pack()  #Label标签.自动调整
root.mainloop()     #主事件循环

print('------------------第二个窗口,Frame,Button,面向对象思想-----------------')
import tkinter as tk
class App:
    def __init__(self,master):   #传入一个根窗口参数
        frame=tk.Frame(master)   
        frame.pack(side=tk.LEFT,padx=50,pady=50)
        self.hi_there=tk.Button(frame,text='打个招呼吧!',fg='white',bg='orange',command=self.say_hi)
        self.hi_there.pack()
    def say_hi(self):
        tkinter.messagebox.showinfo('','大家好,我是tkinter!')
root=tk.Tk()
app=App(root)
root.mainloop()


print('------------------Label参数-----------------')
from tkinter import *
root=Tk()

textLabel=Label(root,text='此为限制级电影\n你是否满18?',justify=LEFT,padx=5,pady=5,\
    font=('迷你简行楷碑',20),fg='red')    #justify设置行与行对齐方式
textLabel.pack(side=RIGHT)    #用于调整组件 在窗口中 的位置
photo=PhotoImage(file='456.gif')     #用于Label的image参数
imgLabel=Label(root,image=photo).pack(side=LEFT)

mainloop()






from tkinter import *
root=Tk()
photo=PhotoImage(file='456.gif')     #用于Label的image参数
textLabel=Label(root,text='此为限制级电影\n你是否满18?',justify=LEFT,padx=5,pady=5,image=photo,\
    compound=CENTER,font=('楷体',20),fg='red')    #compound设置文字与图片的混合模式.默认图片在LEFT
textLabel.pack(side=RIGHT)    #用于调整组件的位置

mainloop()







from tkinter import *

def callback():
    a1.set('吹吧你,我才不信呢~')

root=Tk()
frame1=Frame(root)
frame2=Frame(root)
a1=StringVar()  #在tkinter中申明字符串变量
a1.set('此为限制级电影\n你是否满18?')  #给变量赋值
textLabel=Label(frame1,textvariable=a1,justify=LEFT,\
    font=('楷体',20),fg='red')
textLabel.pack(side=LEFT)    #用于调整组件的位置

photo=PhotoImage(file='456.gif')     #用于Label的image参数
imgLabel=Label(frame1,image=photo)
imgLabel.pack(side=RIGHT)

theButton=Button(frame2,text='我已满18了',command=callback)
theButton.pack()

frame1.pack(padx=50,pady=50)   
frame2.pack(padx=50,pady=50)

mainloop()






from tkinter import *
master=Tk()
longtext = """
Label 可以显示多行文本，你可以直接使用换行符
或使用 wraplength 选项来实现。当文本换行的时
候，你可以使用 anchor 和 justify 选项来使得
文本如你所希望的显示出来。
"""
w = Label(master, text=longtext, anchor=SW, justify=LEFT,width=50,height=20,borderwidth=5,\
    relief=RIDGE,state=ACTIVE,\
    takefocus=True,underline=5,wraplength=200)
w.pack()

photo=PhotoImage(file='456.gif')     #用于Label的image参数
imgLabel=Label(master,text='123',image=photo,anchor=W,cursor='arrow')
imgLabel.pack(side=RIGHT)
mainloop()





print('------------------Button-----------------')
from tkinter import *

master = Tk()

def callback():
    print("我被调用了！")
    return 2

b = Button(master, text="干\n 我操你一脸的蒙B!", command=callback,relief=SUNKEN,\
    activebackground='yellow',borderwidth=6,highlightcolor='red',highlightthickness=5)
b.pack()


Button.flash(b)
print(Button.invoke(b))
mainloop()




print('------------------Checkbutton多选按钮-----------------')

from tkinter import *
root=Tk()
v=IntVar()    #先定义一个整型变量v,用于存放按钮的状态
v.set("T")
c=Checkbutton(root,text='测试一下',variable=v,onvalue="T",offvalue="F").pack()      #variable=v=IntVar()=0/1
l=Label(root,textvariable=v).pack()    #用来显示选中的状态

mainloop()



print('------------------Checkbutton实例选妃-----------------')
from tkinter import *
root=Tk()
girls=['西施','貂蝉','王昭君','杨玉环']
v=[]
print(len(girls))
for i in range(len(girls)):
    v.append(IntVar())
    b=Checkbutton(root,text=girls[i],variable=v[-1])
    b.pack(anchor=W)   #pack中的对齐方式用   anchor用于设置对齐方式E,W,S,N

l0=Label(root,textvariable=v[0]).pack()    #用来显示选中的状态
l1=Label(root,textvariable=v[1]).pack()
mainloop()



print('------------------Checkbutton面向对象-----------------')

from tkinter import *
root=Tk()
class Tksl():
    def __init__(self, master):
        self.var = IntVar()
        self.c = Checkbutton(master, text="DUANG~", variable=self.var, command=self.cb)
        self.c.pack()
        Checkbutton.select(self.c)   #设为选中状态
        

    def cb(self):
        print ("variable is", self.var.get())
        Checkbutton.toggle(self.c)     #切换选中未选中状态

tk1=Tksl(root)

mainloop()













print('------------------Radiobutton实现单选按钮-----------------')
from tkinter import *
root=Tk()
v=IntVar()
Radiobutton(root,text='A.雪碧',variable=v,value=1).pack()  #将值1给v
Radiobutton(root,text='B.可乐',variable=v,value=2).pack()  #将值2给v   实现互斥
Radiobutton(root,text='C.橙汁',variable=v,value=3).pack()
Radiobutton(root,text='D.红茶',variable=v,value=3).pack()  #如果值相等,就会同时选中

mainloop()




print('------------------Radiobutton的for循环多次写入-----------------')
from tkinter import *
root=Tk()
langs=[('python',1),('perl',2),('ruby',3),('java',4)]
v=IntVar()
#v.set(1)
for lang,num in langs:
    b=Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False)  #indicatoron按钮的显示选项,用勾选或按钮
    b.pack(fill=X)

mainloop()



print('------------------Radiobutton的for循环多次写入+LabelFrame-----------------')

from tkinter import *
root=Tk()
group=LabelFrame(root,text='最好的编程语言是?',padx=10,pady=10)  #LabelFrame框架里面的文字边距
group.pack(padx=10,pady=10)   #LabelFrame组件与窗口的距离
langs=[('python',1),('perl',2),('ruby',3),('java',4)]
v=IntVar()
#v.set(1)
for lang,num in langs:
    b=Radiobutton(group,text=lang,variable=v,value=num)  
    b.pack(anchor=W)

mainloop()




print('------------------Listbox-----------------')
from tkinter import *
root=Tk()
thelb=Listbox(root,height=5,selectmode=SINGLE)   #selectmode选择模式SINGLE/MULTIPLE...
thelb.pack()
# thelb.insert(0,'北京')
# thelb.insert(0,'上海')
# thelb.insert(0,'深圳')   当很多选项时,则用for循环

for item in ['鸡蛋','鸭蛋','鹅蛋','李狗蛋']:
    thelb.insert(END,item)
print(thelb.get(1,2))

print(thelb.index(END))
thelb.selection_set(2)    #设置为选中状态
print(thelb.curselection())
print(thelb.get(ACTIVE))
#thelb.delete(1)
#thelb.delete(0,END)
def dele(x=thelb):        #设置默认参数,x为形参
    x.delete(ACTIVE)

thebutton=Button(root,text='删除选中项',command=dele).pack()
#thebutton=Button(root,text='删除选中项',command=dele(thelb)).pack()   #若在此处传参只能执行一次
#thebutton=Button(root,text='删除选中项',command=lambda x=thelb:x.delete(ACTIVE)).pack()
mainloop()






print('------------------Listbox添加滚动条-----------------')
from tkinter import *
root=Tk()
sb=Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)

lb=Listbox(root,yscrollcommand=sb.set)    #Listbox设置yscrollcommand属性为Scrollbar.set方法
for i in range(100):
    lb.insert(END,i)
lb.pack(side=LEFT,fill=BOTH)
sb.config(command=lb.yview)    #通过config来设置组件的属性,Scrollbar的command属性设置为Listbox.yview方法


mainloop()





print('------------------Scale滑块用于选择输入-----------------')
from tkinter import *
root=Tk()
s1=Scale(root,from_=0,to=42,tickinterval=10,resolution=5,length=200,label='金额',activebackground='red',background='blue',troughcolor='yellow')  #from是关键字,所以加_,tickinterval(刻度)=10,resolution(步长)=5
s1.pack()
s2=Scale(root,from_=0,to=200,orient=HORIZONTAL,length=400)  #orient(方向)=HORIZONTAL(水平方向) 设置为水平方式
s2.pack()
s1.set(20)

#获得位置
def show():
    print(s1.get(),s2.get())
    print(s1.coords())   #获得滑块相对于Scale组件左上角的坐标

Button(root,text='获取位置',command=show).pack()

mainloop()





print('------------------Entry输入框-----------------')

from tkinter import *
root=Tk()
e=Entry(root)
e.pack(padx=20,pady=20)    #e.pack()    这样后面才能接着用e
e.delete(0,END)
e.insert(0,'默认文本...默认文本...默认文本...默认文本...默认文本...默认文本...默认文本...默认文本...')
e.xview(20)
e.selection_range(0,END)
print(e.selection_present())


mainloop()





print('------------------Entry输入框的get,排版grid-----------------')

from tkinter import *
root=Tk()
Label(root,text='账号:').grid(row=0,column=0)   #不赋值只为显示
Label(root,text='密码:').grid(row=1,column=0)
v1=StringVar()
v2=StringVar()
e1=Entry(root,textvariable=v1)
e2=Entry(root,textvariable=v2,show='*')   #'*'需要加引号
e1.grid(row=0,column=1,padx=10,pady=10)
e2.grid(row=1,column=1,padx=10,pady=10)
def show():
    print('账号:%s'%e1.get())    #得到变量 输入框组件名.get()
    print('密码:%s'%e2.get())
Button(root,text='登陆',width=10,command=show).grid(row=2,column=0,sticky=W,padx=10,pady=10)  #grid中用sticky来对齐
Button(root,text='退出',width=10,command=root.quit).grid(row=2,column=1,sticky=E,padx=10,pady=10)

mainloop()






print('------------------Entry输入框的验证-----------------')

from tkinter import *
root=Tk()
root.resizable(False,False)
def test():
    if e1.get()=='小甲鱼':
        print('正确!')
        return True
    else:
        print('错误...')
        e1.delete(0,END)
        return False
def test2():
    print('我被调用了...')
    return True

v=StringVar()
e1=Entry(root,textvariable=v,validate='focusout',validatecommand=test,invalidcommand=test2)
                                              #验证函数,需返回True,False      当返回False时调用的函数    
e2=Entry(root)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)


mainloop()


print('------------------Entry输入框,validatecommand的冷却技能-----------------')

from tkinter import *
root=Tk()
def test(content,reason,name,do):
    if e1.get()=='小甲鱼':
        print('正确!')
        print(content,reason,name,do)
        return True
    else:
        print('错误...')
        e1.delete(0,END)
        print(content,reason,name,do)
        return False
def test2():
    print('我被调用了...')
    return True
testCMD=root.register(test)
v=StringVar()
e1=Entry(root,textvariable=v,validate='focusout',validatecommand=(testCMD,'%P','%v','%W','%s'),invalidcommand=test2)
                                              #验证函数,需返回True,False      当返回False时调用的函数    
e2=Entry(root)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)


mainloop()
















print('------------------计算器实例,Entry输入框的validatecommand获得自身的属性-----------------')
from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack(padx=20,pady=20)

v1=StringVar()
v2=StringVar()
v3=StringVar()
def test(content):
    return content.isdigit()   #返回True显示,False不显示
testCMD=root.register(test)    #将数用register封装起来
e1=Entry(frame,width=15,textvariable=v1,validate='key',validatecommand=(testCMD,'%P')).grid(row=0,column=0)   
Label(frame,text='+').grid(row=0,column=1)                   #%p用大写
e2=Entry(frame,width=15,textvariable=v2,validate='key',validatecommand=(testCMD,'%P')).grid(row=0,column=2)
Label(frame,text='=').grid(row=0,column=3)
e3=Entry(frame,width=15,textvariable=v3,state='readonly').grid(row=0,column=4,pady=20)
                               #  只读状态,不可修改
def calc():
    result=int(v1.get())+int(v2.get())    #因为e1.grid()故不能调用e1了,只能用v1
    v3.set(str(result))
Button(frame,text='计算结果',command=calc).grid(row=1,column=2)

mainloop()









print('------------------Text-----------------')
from tkinter import *
root=Tk()
t1=Text(root,width=50,height=10)
t1.pack()
t1.insert(INSERT,'I love python\n')
t1.insert(END,'你所看到的世界并非世界的全部!')

#Text中还可以插入按钮
def show():
    print('哟,我被点了一下!')
b1=Button(t1,text='点我啊',command=show)    #1.Button放在文本组件中
t1.window_create(INSERT,window=b1)         #2.文本组件创建一个小窗口

t1.insert(END,'\n你所看到的世界并非世界的全部!')

#Text中还可以插入图片
photo=PhotoImage(file='456.gif')   #PhotoImage是tkinter下的方法,不可直接image=photoImage('456.gif')
def insert_img():
    t1.image_create(END,image=photo,align='baseline')    #直接在文本组件中插入image
b2=Button(t1,text='插入,插!',command=insert_img)    #1.Button放在文本组件中
t1.window_create(INSERT,window=b2)         #2.文本组件创建一个小窗口

#索引1.2,INSERT,CURRENT,END
print(t1.get('2.2'))     #行数,列数索引
print(t1.get(1.2,'2.2'))
print(t1.get(1.7,"1.end"))  #end需要小写,且必须要加引号

print('------Text.mark_set()锚点-------')
t1.mark_set('aa','1.7')
t1.insert('aa',' 插1 ')
t1.insert('aa',' 入1 ')   #mark点aa也会跟着变动,默认在mark_gravity(重心)右侧,记住右侧的字符
t1.mark_gravity('aa',LEFT)
t1.insert('aa',' 插2 ')
t1.insert('aa',' 入2 ')

t1.mark_unset('aa')     #解除mark点,便不能再用了


t1.tag_add('tag1','2.2','2.end',3.6)   #增加tag标签,成对配对,剩余单独
t1.tag_add('tag2','2.2','2.end',3.6)
t1.tag_config('tag1',background='yellow',foreground='red',bg='gray12')
t1.tag_config('tag2',background='blue',foreground='white')
#注意,同一位置设置不同的tag样式,则后一个会覆盖前一个
t1.tag_lower('tag2')   #可以通过tag_raise()或tag_lower()来提高或降低优先级





t1.insert(END,'吸烟有害健康','tag2')   #当有了tag样式,便可insert使用

print('------Text.tag_bind事件绑定-------')

t1.insert(END,'\n不是你在吸烟,而是烟在吸你的生命!')
t1.tag_add('link','4.0','4.end')    #先增加tag标签
t1.tag_config('link',foreground='blue',underline=True)
def show_arrow_cursor(event):
    t1.config(cursor='arrow')    #'arrow'鼠标的箭头形状
def show_xterm_cursor(event):
    t1.config(cursor='xterm')    #'xterm'鼠标的I形状
import webbrowser
def click(event):                 #注意事件的调用加event
    webbrowser.open('https://www.baidu.com')

t1.tag_bind('link','<Enter>',show_arrow_cursor)
t1.tag_bind('link','<Leave>',show_xterm_cursor)
t1.tag_bind('link','<Button-1>',click)      #绑定事件,传入事件

print(Text.tag_names(t1))




mainloop()  






print('---------内容发生变动,提示!(小甲鱼的方法)-----------')
from tkinter import *
import hashlib
root=Tk()
text=Text(root,width=30,height=5)
text.pack()
text.insert(INSERT,'放荡不羁地生活!')
contents=text.get('1.0',END)

def getSig(contents):   #此contents为形参
    m=hashlib.md5(contents.encode())
    return m.digest()
sig=getSig(contents)    #此contents为实参

def check():
    contents=text.get(1.0,END)
    if sig!=getSig(contents):
        tk.messagebox.showerror('','警报!内容发生变动')
    else:
        tk.messagebox.showinfo('','风平浪静,内容未发生变动!')
Button(root,text='检查内容是否变化',command=check).pack()
mainloop()




print('-----------内容发生变动,提示!(我的方法)-----------')
from tkinter import *
root=Tk()
text=Text(root,width=30,height=5)
text.pack()
text.insert(INSERT,'放荡不羁地生活!')
contents0=text.get('1.0',END)

def check():
    contents1=text.get('1.0',END)
    if contents0!=contents1:
        tkinter.messagebox.showerror('','警报!内容发生变动')
    else:
        tkinter.messagebox.showinfo('','风平浪静,内容未发生变动!')
Button(root,text='检查内容是否变化',command=check).pack()
mainloop()






print('------------查找文本返回位置索引----------')
from tkinter import *
root=Tk()
text=Text(root,width=30,height=5)
text.pack()
text.insert(INSERT,'放荡不羁地生活!有情调地生活!')
def getIndex(index):
    return tuple(map(int,index.split('.')))   #将得到pos传给index参数,用'.'分割成列表,元素映射成int,成元组
start='1.0'
while 1:
    pos=text.search('地',start,stopindex=END)
    print(pos)       #1.4
    print(type(pos))  #<class 'str'>
    if not pos:
        break
    print('找到啦!位置是:',getIndex(pos))
    start=pos+'+1c' #在pos的基础上加上一个字符


mainloop()




print('------------Text中撤销,恢复的实现---------')

from tkinter import *
root=Tk()
text=Text(root,width=30,height=5,undo=True,autoseparators=False)   #1.undo=True撤销功能打开  将默认的每次完整的输入都会插入分隔符,给关闭
text.pack()
text.insert(INSERT,'放荡不羁地生活!有情调地生活!')

def callback(event):    #注意加上event
    text.edit_separator()    
text.bind('<Key>',callback)    #自定义绑定键盘事件,每次输入插入分隔符   <Key>  K要大写啊,妈的!坑爹

def show():
    text.edit_undo()    #2.实现文本的撤销功能
def show1():
    text.edit_redo()    #2.实现文本恢复功能
Button(root,text='撤销',command=show).pack(side=LEFT)
Button(root,text='恢复',command=show1).pack(side=RIGHT)
mainloop()



print('-----------------------------Canvas画布组件---------------------------')
from tkinter import *
root=Tk()
w=Canvas(root,width=200,height=100)   #创建画布
w.pack()
line1=w.create_line(25,50,175,50,fill='red',dash=(2,2),width=3)   #画条直线
            #起点坐标50,50   终点坐标150,50
line2=w.create_line(25,20,175,20,fill='pink',width=30,capstyle=ROUND)   #画条直线  大写可以不可引号,小写要加
juxing1=w.create_rectangle(50,25,150,75,fill='blue')

w.coords(line1,0,0,200,100)   #移动位置   窗口左上角为0,0 右下角为200,100
w.itemconfig(juxing1,fill='white')   #设置样式
w.delete(line1)    #删除图形
Button(root,text='全部删除',command=(lambda x=ALL:w.delete(x))).pack()
w.create_text(100,50,text='情绪波动')    #创建文字块,默认是居中显示,或anchor=W/E
w.create_oval(40,20,160,80,fill='')   #创建圆或椭圆,在矩形中创建,给矩形的四个坐标,fill=''透明色填充
w.create_polygon(100,0,0,100,200,100,outline='red',fill='')  #创建一个多边形,给定相应的坐标点
#arc(弧形,弦或扇形)bitmap(XBM格式文件,内建的位图文件)image(图片对象)window(window组件)
w.create_arc(0,0,50,50,style=ARC)   #正方形的四个点坐标,style默认为扇形PIESLICE,弓形CHORD,弧形ARC


mainloop()




print('------------Canvas画布组件,画图软件功能------------')
from tkinter import *
root=Tk()
w=Canvas(root,width=500,height=300)   #创建画布
w.pack()
def paint(event):     #画个小圆函数
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    w.create_oval(x1,y1,x2,y2,fill='red')

w.bind('<B1-Motion>',paint)   #绑定事件,按住左健拖动


mainloop()





print('-----------------------------Menu组件----------------------------------')
from tkinter import *
root=Tk()
def  callback():
    tkinter.messagebox.showinfo('','已点击了相关菜单!')

menubar1=Menu(root)  #1.创建menubar1菜单

filemenu=Menu(menubar1,tearoff=False)   #1.在menubar1中又创建菜单
filemenu.add_command(label='打开',command=callback)   #2.添加菜单项
filemenu.add('command',label='保存',command=callback)   #两种写法都可以
filemenu.add_separator()   #增加分割线
menubar1.add_cascade(label='文件',menu=filemenu)   #2.给menubar1添加级联菜单


editmenu=Menu(menubar1)
editmenu.add_command(label='剪切',command=callback)   #2.添加菜单项
editmenu.add('command',label='粘贴',command=callback)   #两种写法都可以
menubar1.add_cascade(label='编辑',menu=editmenu)   

root.config(menu=menubar1)  #最后root中配置一下

mainloop()










print('-------------Menu组件,实现右健菜单--------------')
from tkinter import *
root=Tk()
def  callback():
    tkinter.messagebox.showinfo('','已点击了相关菜单!')

menubar1=Menu(root)
menubar1.add_command(label='撤销',command=callback)
menubar1.add_command(label='剪切',command=callback)

frame=Frame(root,width=512,height=512)
frame.pack()

def popup(event):
    menubar1.post(event.x_root,event.y_root)  #位置(在屏幕坐标位置)
frame.bind('<Button-3>',popup)
mainloop()






print('-------------Menu组件,单选/多选菜单--------------')
from tkinter import *
root=Tk()
def  callback():
    print('此美女已被你上过!')


menubar1=Menu(root)  #1.创建menubar1菜单

a1=IntVar()
filemenu=Menu(menubar1,tearoff=True)   #1.在menubar1中又创建菜单
filemenu.add_radiobutton(label='西施',command=callback,variable=a1,value=1)   #2.添加菜单项
filemenu.add('radiobutton',label='貂蝉',command=callback,variable=a1,value=2)   #两种写法都可以
filemenu.add('radiobutton',label='范冰冰',command=callback,variable=a1,value=3)
menubar1.add_cascade(label='美女',menu=filemenu)   #2.给menubar1添加级联菜单

root.config(menu=menubar1)  #最后root中配置一下

mainloop()

cascade





print('-------------Menubutton组件,可以在任何地方显示菜单(不常用)--------------')
from tkinter import *
root=Tk()
def  callback():
    print('此美女已被你上过!')

mb=Menubutton(root,text='来上我啊',relief='raised') 
mb.pack(side='bottom',padx=50,pady=50)

a1=IntVar()
menu1=Menu(mb,tearoff=True)   #1.在menubar1中又创建菜单
menu1.add_radiobutton(label='西施',command=callback,variable=a1,value=1)   #2.添加菜单项
menu1.add('radiobutton',label='貂蝉',command=callback,variable=a1,value=2)   #两种写法都可以
menu1.add('radiobutton',label='范冰冰',command=callback,variable=a1,value=3)


mb.config(menu=menu1)  #最后root中配置一下

mainloop()







print('-------------OptionMenu组件,可以选择的菜单--------------')
from tkinter import *
root=Tk()


a1=StringVar()
a1.set('杨紫')
w=OptionMenu(root,a1,'杨紫','刘涛','杨幂','范冰冰')   #变成列表也是可行的,如下
w.pack()

mainloop()





from tkinter import *
root=Tk()
a1=StringVar()
a1.set('杨紫')
b1=['杨紫','刘涛','杨幂','范冰冰']

w=OptionMenu(root,a1,*b1)   #变成列表需加*list名,*在形参中起到打包作用,在实参中起到解包作用
w.pack()                   #*代表列表,元组,**代表字典
mainloop()


print('-------------组件的事件绑定--------------')
from tkinter import *
root=Tk()
def callback(event):
    print('点击位置:',event.x,event.y)     #相对于本应用程序窗口的坐标
frame=Frame(root,width=200,height=200)
frame.pack()
frame.bind('<Button-1>',callback)    #1代表左健,2代表中健,3代表右健

def callback1(event):
    print('按键是',event.keysym)  #或event.char(不全显示)
frame.bind('<Key>',callback1)
frame.focus_set()     #键盘事件必须加上此句,此组件获得焦点,不然搞不清是谁的健盘事件
#当然也可以设置frame的takefocus=True,然后用Tab键将焦点移上来

def callback2(event):
    print('鼠标拖动轨迹位置:',event.x,event.y)
frame.bind('<Motion>',callback2)     #鼠标在窗口上移动事件

mainloop()



a2='a2g5999d  dgkalj577'
a3=[i for i in a2 if i.isdigit()]
print(a3)      #[2, 5, 9, 9, 9, 5, 7, 7]






print('-------------Label的大哥,Message用于多行文本显示--------------')
from tkinter import *
root=Tk()
w1=Message(root,text='这是一则很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长的消息!',width=200)
w1.pack()
w1=Label(root,text='这是一则很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长的消息!')
w1.pack()


print('-------------Entry组件的变体Spinbox,固定范围内选择输入--------------')
w2=Spinbox(root,from_=0,to=10,increment=0.5,wrap=True)  #increment步长,wrap循环开启
w2.pack()
b1=['杨紫','刘涛','杨幂','范冰冰']
w3=Spinbox(root,value=b1)   #value=元组或列表
w3.pack()
mainloop()


print('-------------Frame的新兄弟PanedWindow,可以调整大小--------------')

from tkinter import *
root=Tk()
m1=PanedWindow(showhandle=True,sashrelief='sunken',handlesize=1,sashpad=15)  #为了显示手柄的边框,默认为左右水平分布;手柄不显示
m1.pack(fill=BOTH,expand=1)  #expand是否m1的大小可扩展,可变
left=Label(m1,text='left')
m1.add(left)

m2=PanedWindow(orient='vertical',showhandle=True,sashrelief='sunken')  #orient垂直分布
m1.add(m2)

top=Label(m2,text='top')
m2.add(top)

bottom=Label(m2,text='bottom')
m2.add(bottom)

print(m1.panes())

mainloop()




print('-------------Toplevel用于创建另一个顶层窗口--------------')
from tkinter import *
root=Tk()
def creat():
    top=Toplevel(colormap='new')
    top.attributes('-alpha',0.8)    #设置顶级窗口的属性
    top.title('我是Toplevel的标题')
    msg=Message(top,text='吸烟有害健康,坚决不再主动去买烟!')
    msg.pack()
Button(root,text='创建顶级窗口',command=creat).pack()

mainloop()


print('------------------排版.pack()详解-----------------')

from tkinter import *

root = Tk()

listbox = Listbox(root)
listbox.pack(fill=BOTH, expand=True) #fill设置填充的方向,expand设置是否填充窗口空白位置

for i in range(10):
    listbox.insert(END, str(i))

mainloop()




from tkinter import *

root = Tk()

Label(root, text="Red", bg="red", fg="white").pack(fill=Y,side=LEFT)
Label(root, text="Green", bg="green", fg="black").pack(fill=Y,side=LEFT)
Label(root, text="Blue", bg="blue", fg="white").pack(fill=Y,side=RIGHT)  

mainloop()




'''
print('------------------Entry输入框的get,排版grid详解-----------------')

from tkinter import *
root=Tk()
Label(root,text='账号:').grid(row=0,column=0,sticky=W)   #不赋值只为显示
Label(root,text='密码:').grid(row=1,column=0,sticky=W)
v1=StringVar()
v2=StringVar()
e1=Entry(root,textvariable=v1)
e2=Entry(root,textvariable=v2,show='*')   #'*'需要加引号
e1.grid(row=0,column=1,padx=10,pady=10)
e2.grid(row=1,column=1,padx=10,pady=10)
def show():
    print('账号:%s'%e1.get())    #得到变量 输入框组件名.get()
    print('密码:%s'%e2.get())
Button(root,text='登陆',width=10,command=show).grid(row=3,column=1,sticky=W,padx=10,pady=10)  #grid中用sticky来对齐
Button(root,text='退出',width=10,command=root.quit).grid(row=3,column=2,sticky=W,padx=10,pady=10)

photo=PhotoImage(file='456.gif')
Label(root,image=photo).grid(row=0,column=2,rowspan=2)   #grid合并,指定起点行列数,指定行列合并数
#e1.grid_forget()
mainloop()

'''

print('------------------排版place详解-----------------')
from tkinter import *
root=Tk()
photo=PhotoImage(file='456.gif')
label0=Label(root,image=photo)
label0.pack()
def callback():
    print('正中靶心!')
Button(label0,text='点我',command=callback).place(relx=0.5,rely=0.5,anchor=CENTER,relheight=0.3,relwidth=0.5)   #将按钮放于图片组件的中心,相对尺寸
Label(root,text='我是窗口正中心!').place(relx=0.5,rely=0.5,anchor=CENTER,relheight=0.2,relwidth=0.2)
mainloop()


''' 