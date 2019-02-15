a=input()
flagg=0
msd=["d","h","o","n","i"]
for x in range(len(a)):
  if(x not in ms or ms.count(a[x])!=a.count(a[x])):
    flagg=1
  else:
    flag=0
if flag==0:
  print("yes")
else:
  print("no")
    
