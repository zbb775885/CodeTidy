#!/usr/bin/python
#-*- coding:utf-8 -*-
from tkinter import *
from tkinter.ttk import *
import types
import string

class App (Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        #self.pack()
        #初始化需要转换的数据框
        #self.entryData = Entry(self, width = 100)
        #self.entryData.pack()
        #self.entryData.grid(row=0, column=0, sticky=N)
        self.inputText = Text(self, width = 200, height = 10)
        self.inputText.insert(INSERT, '请输入需要转换的数据')
        self.inputText.grid(row=0, column=0, sticky=N)
        
        self.outText = Text(self, width = 200, height = 10)
        self.outText.grid(row=11, column=0, sticky=N)
        
        #初始化转换类型的框
        #self.entryTranType = Entry(self, width = 100)
        #self.entryTranType.pack()
        self.cmbEditComboList = ['1：函数命名转换','2：变量命名转换', '3：全局变量命名转换', '4：函数转换']
        self.cmbEditCombo = Combobox(values=self.cmbEditComboList)
        self.cmbEditCombo.set('请选择转换类型')
        self.cmbEditCombo['state'] = 'readonly'
        #self.cmbEditCombo.pack()
        self.cmbEditCombo.grid(row=21, column=0, sticky=N)
        
        #初始化按钮
        self.buttonStart = Button(self, text = "Start", command = self.work)
        #self.buttonStart.pack()
        self.buttonStart.grid(row=2, column=0, sticky=N)
      
        #self.buttonStart.pack()
        self.buttonStart.grid(row=2, column=0, sticky=N)
        
        
        self.grid()
        
        
        #将dataCtx作为输入框的参数输入
        #self.dataCtx = StringVar()
        #self.dataCtx.set("请输入需要转换的数据")
        #self.entryData.config(textvariable = self.dataCtx) 
        
        #将transCtx作为输入框的参数输入
        #self.transCtx = StringVar()
        #self.transCtx.set("1：函数命名转换， 2：变量命名转换 3：全局变量命名转换")
        #self.entryTranType.config(textvariable = self.transCtx)
       
        
        #self.entryData.bind('<Key-Return>', self.printCtx)
        #self.entryTranType.bind('<Key-Return>', self.printCtx)
    
    #字符串第一个字母大写其余小写
    def upFirstCode(self, List):
        strTmp = ''
        for i in List:
            strTmp += i[0].upper() + i[1:]
        return strTmp
      
        
    #函数名字转换
    def funcNameChg(self, str):
        print(str)
        str = str.lower()
        if ('gst_h265_' in str) == False:
            if('gst_vaapi_' in str) == True:
                str = 'gst_h265_dec' + str[len('gst_vaapi_'):]
            elif ('vaapi_' in str) == True:
                str = 'gst_h265_dec' + str[len('VAAPI_'):]
            else:
                str = 'gst_h265_dec' + str
        else:     
            str = 'gst_h265_dec' + str[len('gst_h265_')] 
        
        List = str.split('_')
        List = List[1:]
        
        strTmp = 'Vaapi_'
        strTmp += self.upFirstCode(List)  + '\n'
        #self.dataCtx.set(strTmp)
        #self.inputText.delete(0.0, END)
        self.outText.insert(INSERT,strTmp)
        print(strTmp)
        
    
    #变量命名转换
    def VarNameChg(self, str, extStr):
        chgDict = {'UCHAR': 'uc', 'CHAR': 'c',
                   'USHORT': 'us', 'SHROT': 's',
                   'ULONG': 'ul', 'LONG': 'l',
                   'ULLONG': 'ull', 'LLONG': 'll',
                   'UINT': 'ui', 'INT': 'i',
                   'FLOAT': 'f', 'DOUBLE': 'd',
                   'BOOL_VA': 'b', 'VOID_VA': 'v'
                   }
                   
        strTmp = ''
        List = str.split(' ')
        try:
            List[1] = List[1].lower()
        except:
            messagebox.showinfo('Error', '请确认输入格式正确')
            return
       
        if '' != extStr:
            strTmp += 'g'
        if '[' in str and ']' in List[1]:
            strTmp += 'a'
            List[1] = List[1][0:List[1].rindex('[')]
        
        listCnt = List[1].count('*')
        for i in range(listCnt):
            List[1] = List[1].strip('*')
            strTmp += 'p'
        
        if '_S' in List[0][-2:]:
            strTmp += 'st'
        elif '_E' in List[0][-2:]:
            strTmp += 'st'   
        else:
            try:
                strTmp += chgDict[List[0]]
            except:
                messagebox.showinfo('Error', '请确认输入格式正确')
                return
            
        strTmp += extStr
        List = List[1].split('_')
        strTmp += self.upFirstCode(List)
        
        #self.dataCtx.set(strTmp)
        #self.inputText.delete(0.0, END)
        self.outText.insert(INSERT,strTmp)
    
    
    #处理输入的数据包括功能选取，框数据获取
    def work(self):
        
        #str = self.dataCtx.get()
        str = self.inputText.get(0.0, END)     
        try:
            type = int(self.cmbEditCombo.get()[0])
        except:
            messagebox.showinfo('Error', '请选择转换类型')
            return 
        #print(str, type)
        str = str.replace('\r', '')
        listTmp = str.split('\n')
        for i in listTmp:
            #print('cnt: ', i)
            if type == 1:
                self.funcNameChg(i)
            elif type == 2:
                self.VarNameChg(i, '')
            elif type == 3:
                self.VarNameChg(i, 'H265')
            elif type == 4:
                self.funcNameChg(i)
    
    def printCtx(self, event):
        #print(self.dataCtx.get())
        #print(self.transCtx.get())
        print(self.inputText.get(INSERT, END))

root = App()
root.master.title('代码规范转换工具')
root.mainloop()





























































