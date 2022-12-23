import matplotlib
from matplotlib import pyplot as plt

square=[]
input_value=[]
ran=10
for i in range (1,ran):
    input_value.append(i)
    square.append(i**2)
plt.style.use('seaborn-whitegrid')
'''
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 
'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 
'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 
'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
'''
fig,ax=plt.subplots()   #subplot()表示绘制图表，其中fig表示图片，ax表示图表
ax.plot(input_value,square,linewidth=3)     #根据给定数据绘制图表,linewidth表示线条粗度
ax.set_title("Square Number",fontsize=18,font="arial")
ax.set_xlabel("x",fontsize=15,font="arial")
ax.set_ylabel("y",fontsize=15,font="arial")
#ax.axis([0,10,-5,85])
ax.scatter(input_value,square,c='blue')
#ax.scatter(input_value,square,c=square,cmap=plt.cm.Greens)
plt.show()