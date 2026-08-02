student = int(input())

score = list(map(int, input().split()))
avg = 0
count = 0
high = 0

for i in score:
	avg += i
	count += 1

avg /= count

for i in score:
	if i > avg: high += 1

print(high)