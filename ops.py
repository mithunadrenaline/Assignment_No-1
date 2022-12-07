myList=[]
f=int(input("Enter first range : "))
l=int(input("Enter last range : "))
myList.append(f)
for i in range(f+1,l):
  a=f*i
  myList.append(a)
print(myList)
