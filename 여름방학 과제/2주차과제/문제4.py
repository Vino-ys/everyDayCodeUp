count = 0
success = []

student, line = map(int, input().split())

for i in range(student):
	name, score = input().split()
	score = int(score)
	
	if score >= line:
		count += 1
		success.append(name)

if count == 0:
	print("NONE")
else:
	print(count)
	for i in range(len(success)):
		print(success[i], end = " ")