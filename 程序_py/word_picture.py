import tkinter as tk, os,datetime,zipfile,shutil
from tkinter import filedialog
from tkinter import messagebox as msgbox
from PIL import Image

def changename(picpath,newname):        #修改文件名
    os.chdir(picpath)       #定位到图片所在的文件夹
    for file in os.listdir(picpath):
        try:
            os.rename(os.path.abspath(file),newname+' '+(os.path.basename(file))[5:]) #去掉原图片里面的image字样
        except IOError:
            print("去除image字样有误")
    for file in os.listdir(picpath):
        img = Image.open(file)
        fi_name, fi_type = os.path.splitext(file)  # 获取图片格式
        try:
            if fi_type=='.jpg'  or fi_type=='.png' or fi_type=='.jpeg' or fi_type=='.gif':
                continue        #如果是jpg、png、jpeg三者之一，不做改动
            else:
                img.save("%s.png"%(fi_name))        #如果是其他格式，则改成png格式
                os.remove(picpath+'\\'+os.path.basename(file))      #删除图片原文件
        except IOError:
            print("修改图片格式有误，请在最后检查一下图片是否有缺少")

def extract_zip(zip_path):      # 一个用来解压文件的函数
    os.chdir(os.path.dirname(zip_path))  # 需要进入到这个路径下，这样解压的文件，才在这个路径下
    a = zipfile.ZipFile(zip_path)  # 调用zipfile.ZipFile()函数,创建一个ZipFile对象
    a.extractall()
    a.close()

def draw(f_path,fpath,fname):
    oldname=fname.replace('.docx','')
    oldname=oldname.replace('.doc','')     #设置文件夹名字
    picpath=fpath+"\\"+ oldname    #存储图片的文件夹
    if not os.path.exists(picpath):
        os.makedirs(picpath)        #判断是否存在存储图片的文件夹
    extract_zip(f_path)         # 不用改后缀，直接解压docx文件
    temppath=fpath+'\\word\\media'      #word里的图片存储于此文件夹内
    os.chdir(temppath)      #跳转至该文件夹
    for file in os.listdir(temppath):
        shutil.move(file,picpath)       #将图片移动至指定文件夹内
    os.chdir(fpath)     #跳转至fpath
    shutil.rmtree(fpath+'\\_rels')
    shutil.rmtree(fpath + '\\docProps')
    shutil.rmtree(fpath + '\\word')
    os.remove(fpath+'\\[Content_Types].xml')        #删除其余文件
    return picpath      #返回图片所在文件夹路径

def project():
    root=tk.Tk()
    root.withdraw()
    f_path = (filedialog.askopenfilename()).replace("/", "\\")  # 读取文件位置，并输出正确的绝对路径
    while f_path=="":
        msgbox.showerror('警告','您未选中文件，请重新选择')
        f_path = (filedialog.askopenfilename()).replace("/", "\\")  # 检查是否选中文件
    name,type=os.path.splitext(f_path)
    while type!='.doc' and type!='.docx' :
        msgbox.showerror('警告','您选择的不是word文件，请重新选择')
        f_path = (filedialog.askopenfilename()).replace("/", "\\")
        name, type = os.path.splitext(f_path)       #检查选中的是否是word文件
    print("文件路径为：", f_path)  # 输出文件路径
    newname = input("请输入新的图片名，如果按0则默认抓取当前日期：")  # 统一图片名
    if newname=="0":
        newname=str(datetime.date.today())       #抓取当前日期
    fpath, fname = os.path.split(f_path)  # 获取文件的路径和名字
    picpath=draw(f_path,fpath,fname)      #将图片提取出来
    changename(picpath,newname)     #修改文件名
    return fpath

def main():
    print("欢迎使用本程序，本程序可实现从word中按次序提取出图片")
    print("请按1开始使用，按0退出")
    count=0
    a=input("请输入：")       #输入开启程序的数字 “1”
    while a!="0":       #判断输入
        if a=="1":
            count=count+1
            fpath=project()       #判断输入是1,运行程序
            '''if os.chdir(fpath+"\\customXml"):
                os.remove(fpath+"\\customXml")'''
                #在不同电脑上测试发现有些电脑还会多出一个文件夹，此句是为了删除这个文件夹
            a=input("是否继续，按1继续，按0终止:")
        else:
            a=input("请重新输入:")       #判断输入不是1，重新输入
    if a=='0':
        #print("记得将文件夹移出操作区，防止下次出现意外情况")
        msgbox.showinfo('温馨提示','记得将文件夹移出操作区，防止下次出现意外情况')

if __name__ == '__main__':
    main()