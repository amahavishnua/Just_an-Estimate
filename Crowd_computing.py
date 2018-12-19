
#This is a programme to demonstrate the accuracy of group opinion towards an expert opinion
#CROWD COMPUTING

from statistics import mean
n=[0]
sum=0
for i in range(112):
    
    n.append(i)
n.sort()
i=len(n)*0.1
i=int(i)
k=len(n)*0.9
k=int(k)
print(i)
print(k)
n=n[i:k]

print(mean(n))
print(n)