n=input()
a=int(n)
sum=0
for i in range(0,len(n)):
    rem=a%10
    sum+=rem
    a=a//10
print(sum)
