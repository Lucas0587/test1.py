import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageGrab

def SavePicture(img):
    try:
        img_fath = filedialog.asksaveasfile(title=u'保存', filetypes=[("PNG", '.png')])  # 获取保存路径
        fpath=img_fath.name + ".png"
        print(fpath)
        img.save(fpath)  # 默认png保存。
        # #P.S.我还没有找到其他方法选择格式进行保存
    except:
        img.save("./你没有选择文件位置.png")

def all_pic_catch():
    global win  # 设置全局变量win
    win.withdraw()
    time.sleep(0.15)
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    SavePicture(img)
    win.wm_deiconify()

def area_pic_catch(win):
    win.withdraw()
    time.sleep(0.25)
    win.wm_deiconify()

def quit():
    exit()

win = tk.Tk()  # 创建tk窗口
win.title("主窗口")  # 设置窗口名称
win.geometry('500x400+300+300')  # 设置窗体大小及位置

tk.Label(win, text="该程序为简易的截屏&录屏软件\n\n请选择你需要的功能：",
         pady=10, font=("楷体", 15), bg="#e3b4b8").pack(pady=20)  # Label介绍窗体功能
fram1 = Frame(win)      #fram1组件包含一个Label和两个Button
tk.Label(fram1, text="截屏", width=15, font=("楷体", 15)).pack()
Button(fram1, text="全屏截图", width=15, height=2, font=("黑体", 15),
       command=all_pic_catch, bg="#5cb3cc").pack(side="left", pady=10, padx=10)
Button(fram1, text="区域截图", width=15, height=2, font=("黑体", 15),
       command=lambda: area_pic_catch(win), bg="#41ae3c").pack(side="left", pady=10, padx=10)
fram1.pack()
fram2 = Frame(win)      #fram1组件包含一个Label和两个Button
tk.Label(fram2, text="录屏", width=15, font=("楷体", 15)).pack()
Button(fram2, text="全屏截图", width=15, height=2, font=("黑体", 15),
       command=lambda :all_pic_catch, bg="#5cb3cc").pack(side="left", pady=10, padx=10)
Button(fram2, text="区域截图", width=15, height=2, font=("黑体", 15),
       command=lambda :area_pic_catch, bg="#41ae3c").pack(side="left", pady=10, padx=10)
fram2.pack()
Button(win, text="录屏", width=20).pack()
tk.Label(win, text="退出", width=20, font="宋体").pack()
Button(win, text="退出", width=20, command=quit).pack()
win.mainloop()



