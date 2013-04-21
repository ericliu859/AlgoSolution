a=raw_input()
b=raw_input()
num1=0
num2=0
for i in range(len(a)):
	if a[i]=='1':
		num1+=1
if num1%2:
	num1+=1
for i in range(len(b)):
	if b[i]=='1':
		num2+=1
if num1>=num2:
	print "YES"
else:
	print "NO"
