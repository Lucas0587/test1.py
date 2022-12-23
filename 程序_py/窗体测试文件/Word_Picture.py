import os,shutil,glob,fitz,imghdr,tkinter as tk,docx,re
from tkinter import filedialog,messagebox
from tkinter import *
def q():
    exit()
def name():     #用于修改文件名
    top = Tk()
    top.geometry('300x300+100+100')  # 创建窗口top，用于输入文件名
    L1 = Label(top, text="请输入图片名：")
    L1.pack(side=LEFT)      #输入前面的引语
    E1 = Entry(top, bd=5)
    E1.pack(side=LEFT)  # 输入文件名
    def GetName():
        result=E1.get()
        print(result)
    Button(top, text="确认",command=GetName).pack(padx=10)        #确认键
    Button(top,text="退出",command=q)
    top.mainloop()
def project():      #提取图片 主函数
    f_path = (filedialog.askopenfilename()).replace("/","\\")   #读取文件位置，并输出正确的绝对路径
    tk.messagebox.showinfo('提示', f_path)    #弹窗显示文件路径
    #print(f_path)  #打印f_path
    NewName = name()
    print("Name is:",NewName)
def main():
    window = tk.Tk()
    window.geometry('640x360+600+300')  # 设置窗体大小及位置
    window.title("主窗口")
    Button(window, text="提取图片", command=project).pack(padx=10, pady=10)     #按钮1：主功能
    Button(window, text="退出", command=q).pack(padx=10, pady=10)     #按钮2：退出
    window.mainloop()

if __name__ == '__main__':
    print("Hello World")
    main()