n = int(input())
score = {}

for i in range(n):
	name, num = input().split()
	num = int(num)

	score[name] = num

newScore = sorted(score.items(), key = lambda x:(-x[1], x[0]))

for key, value in newScore:
	print(key)