# Assignment

Program No: 1

CODE: 
myList=[]
f=int(input("Enter first limit: "))
l=int(input("Enter last limt : "))
myList.append(f)
for i in range(f+1,l):
  a=f*i
  myList.append(a)
print(myList)
