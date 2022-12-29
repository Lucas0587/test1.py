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

p1=ax.bar(xlabel-width/2,Chinese,width,color="#ff11ff",label="Chinese",tick_label=name)
p2=ax.bar(xlabel+width/2,Math,width,color="#11ff11",label="Math",yerr=2)

ax.bar_label(p1,padding=3)
ax.bar_label(p2,padding=3)
#ax.set_xticks(xlabel,name)
ax.legend()

fig.tight_layout(pad=3)

plt.show()

'''
(1) Axes.bar_label(container, labels=None, *, fmt='%g', label_type='edge'(default)/'center', padding=0, **kwargs)
    #fmt:A format string for the label.

(2) tight_layout(*, pad=1.08, h_pad=None, w_pad=None, rect=None)
    #h_pad、w_pad默认大小pad
    #rect: tuple (left, bottom, right, top), default: (0, 0, 1, 1)

(3) Axes.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
    #color、edgecolor、linewidth(边距)、tick_label(ax.set_xticks)、label、xerr, yerr(误差线长度)、ecolor(误差线颜色)、capsize(误差线工字宽度)
    #error_kw：字典，error_kw=error_params1，error_params1=dict(elinewidth=3,ecolor='red',capsize=10)，设置误差标记参数 #log(科学计数法)
'''