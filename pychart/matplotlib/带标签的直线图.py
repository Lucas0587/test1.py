import random
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(19.2,10.8))

N=20
xlabel=np.arange(N)
name=[]
Chinese=[]
Math=[]
English=[92, 93, 96, 95, 96, 97, 93, 97, 96, 93]
for i in range(N):
    Chinese.append(random.randint(90,100))
    Math.append(random.randint(90,100))
    name.append("G"+str(i+1))

p1=ax.bar(xlabel,Chinese,width=0.3,yerr=4,color="#ff11ff")
p2=ax.bar(xlabel,Math,width=0.3,yerr=4,bottom=Chinese,color="#11ff11")
#p3=ax.bar(xlabel,English,width=0.5,yerr=4,bottom=Math)
ax.set_xticks(xlabel,labels=name)
ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p2)

plt.show()

