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
        self.entryData = Entry(self, width = 100)
        #self.entryData.pack()
        self.entryData.grid(row=0, column=0, sticky=N)
        
        #初始化转换类型的框
        #self.entryTranType = Entry(self, width = 100)
        #self.entryTranType.pack()
        self.cmbEditComboList = ['1：函数命名转换','2：变量命名转换', '3：全局变量命名转换']
        self.cmbEditCombo = Combobox(values=self.cmbEditComboList)
        self.cmbEditCombo.set('请选择转换类型')
        self.cmbEditCombo['state'] = 'readonly'
        #self.cmbEditCombo.pack()
        self.cmbEditCombo.grid(row=1, column=0, sticky=N)
        
        #初始化按钮
        self.buttonStart = Button(self, text = "Start", command = self.work)
        #self.buttonStart.pack()
        self.buttonStart.grid(row=2, column=0, sticky=N)
        
        self.grid()
        #将dataCtx作为输入框的参数输入
        self.dataCtx = StringVar()
        self.dataCtx.set("请输入需要转换的数据")
        self.entryData.config(textvariable = self.dataCtx) 
        
        #将transCtx作为输入框的参数输入
        #self.transCtx = StringVar()
        #self.transCtx.set("1：函数命名转换， 2：变量命名转换 3：全局变量命名转换")
        #self.entryTranType.config(textvariable = self.transCtx)
       
        
        self.entryData.bind('<Key-Return>', self.printCtx)
        #self.entryTranType.bind('<Key-Return>', self.printCtx)
    
    def upFirstCode(self, List):
        strTmp = ''
        for i in List:
            strTmp += i[0].upper() + i[1:]
        return strTmp
    def funcNameChg(self, str):
        print('ffggf')
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
        strTmp += self.upFirstCode(List)
        self.dataCtx.set(strTmp)
        
        print(strTmp)
        
    
    
    def VarNameChg(self, str, extStr):
        print('fdsfs')
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
        List[1] = List[1].lower()
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
            strTmp += chgDict[List[0]]
            
        strTmp += extStr
        List = List[1].split('_')
        strTmp += self.upFirstCode(List)
        
        self.dataCtx.set(strTmp)
    
    def work(self):
        
        str = self.dataCtx.get()
        try:
            type = int(self.cmbEditCombo.get()[0])
        except:
            messagebox.showinfo('Error', '请选择转换类型')
        print(str, type)
        if type == 1:
            self.funcNameChg(str)
        elif type == 2:
            self.VarNameChg(str, '')
        elif type == 3:
            self.VarNameChg(str, 'H265')
    
    def printCtx(self, event):
        print(self.dataCtx.get())
        #print(self.transCtx.get())

root = App()
root.master.title('Foo')
root.mainloop()





























































