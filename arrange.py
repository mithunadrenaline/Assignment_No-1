myList=[]
n=int(input("Enter the limit : "))
for i in range(0,n+1):
  a=int(input())
  myList.append(a)
print(myList)
print("""Select an operation 
      1) Arrange list in ascending oreder 
      2) Arrange list in descending order """)
a=int(input())
if a==1:
  myList.sort()
  print(myList)
elif a==2:
  myList.sort()
  myList.reverse()
  print(myList)
else:
  print("Your request is not found")
