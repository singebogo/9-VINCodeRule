#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import time

from VehicleIdentificationNumber import vin_numbers, get_normal_vin, check_vin

LOG_LINE_NUM = 0


class MainGUI(object):
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.init_datas()

    #################################数据定义#############################################################
    def init_datas(self):
        pass

    #############################################GUI设置###########################################
    # 设置窗口
    def set_init_window(self):
        self.winTitle()
        self._centerWindow(380, 500)
        self._setWindowStyle()
        self._showBehaid()
        # menu
        # self.menu()
        # 全局标志
        self.golbalInit()
        # title
        self.clientTitle()
        # 布局
        self.initFrame()
        # 日志
        # self.initLog()

    def winTitle(self):
        self.init_window_name.title("Vin 9 rules@kxw")  # 窗口名

    def _centerWindow(self, width, height):
        sw = self.init_window_name.winfo_screenwidth()
        # 得到屏幕宽度
        sh = self.init_window_name.winfo_screenheight()
        # 得到屏幕高度
        x = (sw - width) / 2
        y = (sh - height) / 2
        self.init_window_name.geometry("%dx%d+%d+%d" % (width, height, x, y))

    def _setWindowStyle(self):
        self.init_window_name["bg"] = "white"  # 窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        self.init_window_name.attributes("-alpha", 0.9)  # 虚化，值越小虚化程度越高
        self.init_window_name.resizable(False, False)  # 禁止用户调整窗口大小

    def _showBehaid(self):
        pass


    def golbalInit(self):
        self.number = 10
        self.vintext= 'vin:'

    def clientTitle(self):
        ###定义一个`label`显示`on the window`
        # self.fm1 = Frame(self.init_window_name)
        # self.titleLabel = Label(self.fm1, text='gener vin 9 rules')
        # self.titleLabel.pack()
        # self.fm1.pack(side=TOP)
        pass

    # 菜单
    def menu(self):
        ##创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
        menubar = Menu(self.init_window_name)

        # 菜单一
        filemenu = Menu(menubar, tearoff=0)

        # 一级菜单
        # filemenu.add_separator()  # 分割线
        filemenu.add_command(label='Exit', command=self.init_window_name.quit)
        # 一级菜单
        menubar.add_cascade(label='File', menu=filemenu)

        self.init_window_name.config(menu=menubar)

    # 日志
    def initLog(self):
        self.frame2 = Frame(self.init_window_name, width=1068)
        self.log_data_Text = Text(self.frame2, width=1068, height=9)
        self.log_data_Text.pack(side=TOP)  # 日志框
        self.frame2.pack(side=TOP)

    def initCheck(self, labFrame):
        self.vintextL = StringVar()
        self.vintextL.set("vin:")
        self.vinL = Label(labFrame, text="vin:", textvariable=self.vintextL)
        self.vinL.grid(row=0, column=0)

        self.vintext = StringVar()
        self.vin = Entry(labFrame, width=17, textvariable=self.vintext)
        self.vin.grid(row=0, column=1)
        self.vin.bind('<Key>', lambda e: self.TextChange(e, self.vintext))  # 给输入框绑定键盘敲击事件，把绑定的变量传入回调函数中
        # 设置文本框只能输入数字
        self.vin.config(validate="key",
                        validatecommand=(self.init_window_name.register(lambda P: P.isascii()), "%P"))

        btn = Button(labFrame, text="Check", command=self.checkCallBack)
        btn.grid(row=0, column=2)
        self.isRulesVin = Entry(labFrame, fg='red', width=10, state='readonly')
        self.isRulesVin.grid(row=0, column=3)

    def initGenerVin(self, labFrame):
        numberL = Label(labFrame, text="vin nums:")
        numberL.grid(row=1, column=0)

        textEntry = StringVar()
        textEntry.set(self.number)
        self.number = Entry(labFrame, textvariable=textEntry, width=15)
        self.number.grid(row=1, column=1)

        # 设置文本框只能输入数字
        self.number.config(validate="key",
                           validatecommand=(self.init_window_name.register(lambda P: P.isdigit()), "%P"))

        generBtn = Button(labFrame, text="Gener", command=self.generBtnCallBack)
        generBtn.grid(row=1, column=2)

        generBtn = Button(labFrame, text="G-One", command=self.generOneBtnCallBack)
        generBtn.grid(row=1, column=3)

    def initText(self, labFrame):
        scrollbar_v = Scrollbar(self.init_window_name)
        scrollbar_v.pack(side=RIGHT, fill=Y)
        scrollbar_h = Scrollbar(self.init_window_name, orient=HORIZONTAL)
        scrollbar_h.pack(side=BOTTOM, fill=X)
        self.text1 = Text(self.init_window_name, yscrollcommand=scrollbar_v.set, xscrollcommand=scrollbar_h.set,
                          wrap=NONE)
        self.text1.pack(expand=YES, fill=BOTH)
        scrollbar_v.config(command=self.text1.yview)  # 垂直滚动条绑定text
        scrollbar_h.config(command=self.text1.xview)  # 水平滚动条绑定text

    # 布局
    def initFrame(self):
        labFrame = LabelFrame(self.init_window_name, text="Vin Data Validation")  # 创建框架标签
        #
        self.initCheck(labFrame)
        self.initGenerVin(labFrame)

        labFrame.pack(padx=2, pady=10, ipadx=2, ipady=2)
        self.initText(labFrame)


    ##################################功能函数######################################################################

    def checkCallBack(self):
        if(self.vin.get()):
            self.vintextL.set('vin: '+ str(len(self.vin.get())))
            self.isRulesVin.config(state='normal')
            self.isRulesVin.delete(0, END)
            msg = check_vin(self.vin.get())
            self.isRulesVin.insert(END, msg if msg.find('-') == -1 else msg[msg.find('-') + 1:] )
            self.isRulesVin.config(state='readonly')
            self.text1.insert(END, msg + "\n")

    def generBtnCallBack(self):
        if(self.number.get()):
            self.text1.delete(1.0, END)
            vins = vin_numbers(int(self.number.get()))
            for vin in vins:
                self.text1.insert(END, vin+"\n")

    def generOneBtnCallBack(self):
        self.text1.delete(1.0, END)
        self.text1.insert(END, get_normal_vin())  # END实际就是字符串'end'

    def TextChange(self, event, widgetVar):
        self.vintextL.set('vin: ' + str(len(self.vin.get())))

    def do_job(self):
        pass

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 8:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)


#############################################启动函数##########################################
def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MainGUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


#################################主函数################################################
if __name__ == '__main__':
    gui_start()
