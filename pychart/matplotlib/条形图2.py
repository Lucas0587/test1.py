import random
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(9.6,5.4))

N=6
xlabel=np.arange(N)
name=[]
Chinese=[]
Math=[]
width=0.2
for i in range(N):
    Chinese.append(random.randint(89,97))
    Math.append(random.randint(89,97))
    name.append("G"+str(i+1))
p1=ax.bar(xlabel+width/2,Chinese,width,color="#ff11ff")
p2=ax.bar(xlabel-width/2,Math,width,color="#11ff11")

ax.bar_label(p1,padding=3)
ax.bar_label(p2,padding=3)
#Axes.bar_label(container, labels=None, *, fmt='%g', label_type='edge'(default)/'center', padding=0, **kwargs)


plt.show()