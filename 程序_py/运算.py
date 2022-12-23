'''运行结束后记得删除'''

B=[[0,80*10,95*10,138*10,182*10]]
A=[[30,0,20,32,45],[80,0,95,138,182]]
for i in range(1,10):
    seed=A[0][0]*i+A[1][0]*(10-i)
    product_normal=A[0][2]*i+A[1][2]*(10-i)
    product_silver=A[0][3]*i+A[1][3]*(10-i)
    product_gold=A[0][4]*i+A[1][4]*(10-i)
    B.append([i,seed,product_normal,product_silver,product_gold])
    #print("seed:",seed," product_normal:",product_normal," product_silver:",product_silver," product_gold:",product_gold)
print(B)
maxprice=max(max(B))
for i in range(0,10):
    if max(max(B))>maxprice:
        maxprice=B[i][2]
print(maxprice)