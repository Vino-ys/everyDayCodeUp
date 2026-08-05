n = int(input())
name = []
price = []
printName = []
find = False

for i in range(n):
	na, pr = input().split()
	name.append(na)
	price.append(int(pr))

num = int(input())

for i in range(num):
	printName.append(input())

for i in range(num):
	for j in range(n):
		if printName[i] == name[j]:
			print(price[j])
			find = True
	if find == False:
		print(-1)
	find = False