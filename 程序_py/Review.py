fpath="C:\\Users\HP\Desktop\\test.txt"
sum=0
count=0
list=[[" "]*3 for i in range(10)]
with open(fpath,'r+',encoding="utf-8") as f:
    file=f.readlines()
    print(file)
    print(type(file))
for j in range(len(file)):
    print(file[j].split())
for j in range(len(file)):
    if ('\t' in file[j])==0:
        sum=0
        list[count][0]=file[j].split()
        count+=1
    else:
        list[count-1][sum+1]=file[j].split()
        sum+=1
print(list)
for j in range(len(list)):
    print(list[j][0],":",list[j][1],"\t",list[j][2])


'''import os
fpath="C:\\Users\HP\Desktop\\name.txt"
with open(fpath,"r",encoding="utf-8") as f:
    file=f.readlines()
ocpath="C:\\Users\HP\Desktop\\物理系学术讲座安排"
os.listdir(ocpath)
for i in range(len(file)):
    a=str(file[i].split()).replace("'"," ").replace("["," ").replace("]"," ").replace("  "," ")
    os.mkdir(ocpath+'\\'+'物理系学术讲座'+'第'+str(i+1)+'期 '+a)'''
