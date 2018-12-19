
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
messi=mean(n)
print(messi)
print(n)
import matplotlib.pyplot as vishnu
y=[]
for i in range(len(n)):
    y.append(5)
vishnu.plot(n,y,'rd')
vishnu.ylabel("values")
vishnu.xlabel("Estimated values")
vishnu.plot(60,5,'g^')  # RED dot is actual value
vishnu.plot(messi,5,'bs')   #Estimated value