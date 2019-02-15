q=input()
flag=0
ms=["d","h","o","n","i"]
for i in range(len(q)):
  if(i not in ms or ms.count(q[i])!=q.count(q[i])):
    flag=1
  else:
    flag=0
if flag==0:
  print("yes")
else:
  print("no")
    
