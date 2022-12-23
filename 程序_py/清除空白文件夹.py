import os,shutil
from os.path import join,getsize

def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size

def solve(fpath):
    for i in os.listdir(fpath):
        fpath_1=fpath+'\\'+i
        if getdirsize(fpath_1)==0:
            shutil.rmtree(fpath_1)
        else:
            for j in os.listdir(fpath_1):
                fpath_2=fpath_1+'\\'+j
                if getdirsize(fpath_2) == 0:
                    try:
                        shutil.rmtree(fpath_2)
                    except:
                        print("存在下属文件夹")
                else:
                    for k in os.listdir(fpath_2):
                        fpath_3 = fpath_2 + '\\' + k
                        if getdirsize(fpath_3) == 0:
                            shutil.rmtree(fpath_3)
                        else:
                            print("此路径非空：",fpath_3)


if __name__ == '__main__':
    fpath='C:\\Users\HP\Documents\WeChat Files\wxid_ra1d0r2jelq222\FileStorage\MsgAttach'
