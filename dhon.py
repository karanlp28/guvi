a=input()
flagg=0
msd=["d","h","o","n","i"]
for x in range(len(a)):
  if(x not in msd or msd.count(a[x])!=a.count(a[x])):
    flagg=1
  else:
    flagg=0
if flagg==0:
  print("yes")
else:
  print("no")
    
