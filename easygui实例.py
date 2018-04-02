'''
如何安装外部模块?
C:\python\Script中有pip运行程序,将此路径加入环境变量path中
cmd命令中输入pip install easygui
测试是否安装成功?
    cmd中输入python
    import easygui  未提示错误则安装成功

easygui安装后的路径C:\Python\Lib\site-packages\easygui
'''

import easygui as eg

#常用参数:msg='信息提示文字',title='我是标题',default='我是默认值',image='',root=None

'''
#eg.egdemo()    #各种实例

#消息框
eg.msgbox("显示的文字",'标题')
eg.msgbox(msg='your message goes here',title='your title',ok_button='点我啊',image='')


print('-----------------用户选择-------------------')

#文字单选择对话框
choices = ['愿意', '不愿意', '有钱的时候愿意']
reply = eg.choicebox('你愿意购买资源打包支持小甲鱼吗？', choices = choices)
print(reply)
#文字多选对话框
multchoicebox()









#继续or取消 对话框    返回1(选中continue)或者0(选中cancel) 不是布尔型的
if eg.ccbox('继续对话框'):
    print('点了继续')
else:
    print('取消了')
#两个选择按钮对话框

import sys

if eg.ccbox('要再来一次吗？', choices=('要啊要啊^_^', '算了吧T_T')):
        eg.msgbox('不给玩了，再玩就玩坏了......')
else:
        sys.exit() # 记得先 import sys 哈





eg.ynbox()   #yes no对话框,返回True/False
eg.boolbox()  #yes no对话框,返回True/False
eg.indexbox()      #选择第一个yes返回0,选择no返回1




#多个按钮选择对话框

eg.buttonbox(msg='按钮选择对话框?',title='',choices=('a','b','c','d'),image='123.gif')



#图片仅支持gif格式


print('-----------------用户输入-------------------')


#单个用户输入文本对话框
a1=eg.enterbox(msg='请输入内容:',title='',default='我是默认值',strip=True,image=None)
print(a1)
#密码输入框
eg.passwordbox()



#用户输入数字对话框
eg.integerbox(lowerbound=5,upperbound=10)

#多文本输入框
a2=eg.multenterbox(msg='消息提示:',title='',fields=['第一个框','第二个框'],values=[])
print(a2)      #['123', '456']


#用户名密码输入框
a4=eg.multpasswordbox(fields=['用户名','密码'],values=[])
print(a4)      #['陈旭东', '123456']


print('-----------------显示文本-------------------')

eg.textbox(msg='提示内容:',title='',text='在苏州双塔街道沧浪亭社区，有一位居民，\
把自家的金毛犬训练成了一只爱捡瓶子的环保狗。\
这只金毛犬，可不是简单的只会叼一只瓶子在嘴里，\
而是一边游泳一边捡瓶子。它的水性非常好，体力也非常棒。\
来源：姑苏晚报',codebox=0)   #codebox=0 设置为自动换行

eg.codebox(msg='提示内容:',title='',text='在苏州双塔街道沧浪亭社区，有一位居民，\
把自家的金毛犬训练成了一只爱捡瓶子的环保狗。\
这只金毛犬，可不是简单的只会叼一只瓶子在嘴里，\
而是一边游泳一边捡瓶子。它的水性非常好，体力也非常棒。\
来源：姑苏晚报')  #同上,只是不能设置自动换行参数,不能换行


print('-----------------目录与文件-------------------')

#得到路径名,不含文件
a5=eg.diropenbox(msg='',title='',default=None)
print(a5)    #E:\党校\CAD上机题\我的图块

#得到路径文件
a6=eg.fileopenbox(msg='要打开哪个文件呢?',title='我是标题',default='*',filetypes=['*.txt'])
print(a6)    #E:\视频\同学\终级理化班.avi
#default='C:\\fishc\*.py' 默认路径
#filetype=['*.txt','*.py']  适用于通配符,显示所有py文件 点击下方下拉列表可以显示


#弹出保存对话框,得到路径
eg.filesavebox()     #参数同上




print('-----------------捕获异常-------------------')

try:
        print('I Love FishC.com!')
        int('FISHC') # 这里会产生异常
except:
        eg.exceptionbox('有异常了哦!','标题')


'''

print('-----------------最后实例-------------------')
import easygui as g
import sys

while 1:
        g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")

        msg ="请问你希望在鱼C工作室学习到什么知识呢？"
        title = "小游戏互动"
        choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
        
        choice = g.choicebox(msg, title, choices)  #文本选择对话框


        g.msgbox("你的选择是: " + str(choice), "结果")

        msg = "你希望重新开始小游戏吗？"
        title = "请选择"
        
        if g.ccbox(msg, title):     #继续或取消两个按钮 选择对话框
                pass  #点击继续,进入下一次循环
        else:
                sys.exit(0)     # user chose Cancel

































