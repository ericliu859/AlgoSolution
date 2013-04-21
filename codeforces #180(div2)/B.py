n,sx,sy,ex,ey = map(int,raw_input().split())
string=raw_input()
step1=0
step2=0
flag=0
if sx<=ex and sy<=ey :
	for i in range(n):
		if string[i]=='E' and step1<ex-sx :
			step1+=1
		if string[i]=='N' and step2<ey-sy :
			step2+=1
		if step1==ex-sx and step2==ey-sy :
			print i+1
			flag = 1
			break 
	if flag == 0:
		print -1
elif sx<=ex and sy>=ey :
	for i in range(n):
		if string[i]=='E' and step1<ex-sx :
			step1+=1
		if string[i]=='S' and step2<sy-ey :
			step2+=1
		if step1==ex-sx and step2==sy-ey :
			print i+1
			flag = 1
			break 
	if flag ==0:
		print -1
elif sx>=ex and sy<=ey :
	for i in range(n):
		if string[i]=='W' and step1<sx-ex :
			step1+=1
		if string[i]=='N' and step2<ey-sy :
			step2+=1
		if step1==sx-ex and step2==ey-sy :
			print i+1
			flag = 1
			break
	if flag ==0:
		print -1
else:
	for i in range(n):
		if string[i]=='W' and step1<sx-ex :
			step1+=1
		if string[i]=='S' and step2<sy-ey :
			step2+=1
		if step1==sx-ex and step2==sy-ey :
			print i+1
			flag = 1
			break
	if flag ==0:
		print -1

