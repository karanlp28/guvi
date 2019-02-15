q,w=map(int,input().split())
for i in range(1,20):
  e=w**i
  if e==q:
    print("yes")
    break
else:
  print("no")
