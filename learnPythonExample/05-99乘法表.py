#-*- conding:utf-8 -*-
print("下面是9*9乘法表：")
i = 1
while i<=9:
	j = 1
	while j<=i:
		print("%dx%d=%d "%(j,i,j*i),end="")	
		j+=1
	print("")
	i+=1

	
