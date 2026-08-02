student = int(input())
score = list(map(int,input().split()))

maxScore = 0
num = 0
count = 1

for i in score:
	
	if i > maxScore:
		maxScore = i
		num = count
	
	count += 1

print(maxScore, num)