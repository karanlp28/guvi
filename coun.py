n=input()
b=int(n)
count=0
for i in range(len(n)):
    rem=b%10
    count+=1
    b=b//10
print(count)
