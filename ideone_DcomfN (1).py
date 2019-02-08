n=int(input())
li=[int(x) for x in input().split()]
a=sorted(li)
if len(a)%2==0:
	b=(len(a)//2) - 1
	print(a[b])
else:
	b=len(a)//2
	print(a[b])