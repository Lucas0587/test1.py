import requests
import os,shutil,glob,fitz,imghdr,time
imgType_list = {'jpg', 'bmp', 'png', 'jpeg', 'rgb', 'tif'}
'''def stopp(img_dir):
    for img in sorted(glob.glob("{}/*".format(img_dir))):  # 读取图片，确保按文件名排序
        if'''
def changename(i):
    if i < 10:
        file_path = "0" + str(i) + '.png'
    else:
        file_path = str(i) + '.png'
    return file_path
def delete(img):
    if imghdr.what(img) in imgType_list:
        os.remove(img)
def pdff(img_dir,mkpath,name):
    doc=fitz.open()
    count=0
    for img in sorted(glob.glob("{}/*".format(img_dir))):   #读取图片，确保按文件名排序
        print(img)
        imgdoc=fitz.open(img)   #打开图片
        pdfbytes=imgdoc.convertToPDF()  #使用图片创建单页的PDF
        imgpdf=fitz.open("pdf",pdfbytes)
        doc.insertPDF(imgpdf)
        names=name+".pdf"
        if os.path.exists(names):
            os.remove(names)
        doc.save(names)   #保存pdf文件
        count+=1
        print("正在准备第",count,"，请稍等")
    r=os.path.abspath(names)
    doc.close()
    shutil.move(r,mkpath)
    print("文件："+names+"下载完成，位于："+r)
def download(file_path,picture_url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44",
    }
    r=requests.get(picture_url,headers=headers)
    with open(file_path,"wb") as f:
        f.write(r.content)
    time.sleep(0.1)
def mkdir_zi (path,name):
    path=path+'\\'+name
    os.makedirs(path)
    return path
def mkdir(path,name):
    path = path.strip()     # 去除首位空格
    path = path.rstrip("\\")       # 去除尾部 \ 符号
    isExists = os.path.exists(path)     # 判断路径是否存在   # 判断结果
    if not isExists:    # 如果不存在则创建目录    # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return 1     # 存在 True
    else:   # 如果目录存在则不创建，并提示目录已存在
        q=int(input(path + ' 目录已存在，按1更换文件夹，按0继续，按2将创建一个子文件夹：'))
        if q==1:
            return 0
        elif q==2:
            return 2
        else:
            return 1
def main():
    url=""
    prefix_url=input("请输入最后一页图片链接,例如：https://s3.ananas.chaoxing.com/doc/fd/46/62/901cfcf9e7e9029a981e29819044f18e/thumb/18.png\n")
    prefix_url_list=prefix_url.split('/')
    for i in range(len(prefix_url_list)-1):
        url=url+prefix_url_list[i]+"/"
    n=int(prefix_url_list[len(prefix_url_list)-1].replace(".png"," ").strip())
    '''prefix_url="https://s3.ananas.chaoxing.com/doc/fd/46/62/901cfcf9e7e9029a981e29819044f18e/thumb/"
    n=18'''
    name = input("请输入文件名：")
    mkpath = input("请选择目录：")  # 定义要创建的目录
    while mkdir(mkpath,name)==0: # 调用函数
        mkpath = input("请重新选择目录：")# 定义要创建的目录
    for i in range(1,n+1):
        file_path=changename(i)
        picture_url=url+str(i)+'.png'
        #print(picture_url)
        download(file_path,picture_url)
        shutil.move(file_path,mkpath)
        print("正在下载第"+str(i)+"张图片，请耐心等待")
        #stopp(mkpath)
    print("图片下载完毕")
    img_dir=mkpath
    print(img_dir)
    pdff(img_dir,mkpath,name)
    if int(input("输入0删除保存的图片，输入1不进行删除操作:"))==0:
        for img in sorted(glob.glob("{}/*".format(img_dir))):   #读取图片，确保按文件名排序
            delete(img)
    print("完成！")
if __name__=='__main__':
    main()