vo=['a','e','i','o','u']
s=input()
for i in range(len(s)):
	if s[i] in vo:
		print("yes")
		break
else:
	print("no")