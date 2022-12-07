myList=[]
n=int(input("Enter the limit : \t"))
for i in range(0,n+1):
  a=int(input())
  myList.append(a)
print("List is : ",myList)
myList.sort()
print("Sorted list is : ",myList)
