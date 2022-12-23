import matplotlib.pyplot as plt
fig,ax=plt.subplots()

time=[0,3,6,9,12,15,18,21,24,27]
data=[16.05,15.15,14.60,13.40,12.15,11.50,10.20,9.55,9.05,7.55]

ax.bar(time,data,color=["#ff11ff","#11ff11"])
ax.set_ylabel("data")
ax.set_xlabel("time")
ax.set_title("data-time graph")

plt.show()