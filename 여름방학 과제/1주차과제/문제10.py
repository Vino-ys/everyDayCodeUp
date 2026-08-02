n = int(input())
str = 'a'
long = 'a'
count = 0
longCount = 0

for i in range(n):
	
	str = input()
	
	for j in range(len(str)): count += 1
		
	if count > longCount:
		longCount = count
		long = str
		
	count = 0

print(long, longCount)