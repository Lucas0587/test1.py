import random
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(19.2,10.8))

N=10
xlabel=np.arange(N)
name=[]
Chinese=[]
Math=[]
for i in range(N):
    Chinese.append(random.randint(90,100))
    Math.append(random.randint(90,100))
    name.append("G"+str(i+1))
