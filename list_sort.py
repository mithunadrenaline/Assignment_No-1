myList=[]
n=int(input("Enter the limit : \t"))
for i in range(0,n+1):
  a=int(input())
  myList.append(a)
myList.sort()
print(myList)
