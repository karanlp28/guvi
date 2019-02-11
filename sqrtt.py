import math
a,b=map(int,input().split())
c=a*b
i=int(math.sqrt(c))
if c== i*i:
    print("ÿes")
else:
    print("no")
