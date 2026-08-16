n = int(input())
fileHjj = {}

for i in range(n):
	file = input()
	for j in range(len(file)):
		if file[j] == ".":
			Hjj = file[j+1:]
			if Hjj in fileHjj:
				fileHjj[Hjj] += 1
			else:
				fileHjj[Hjj] = 1
				
fileHjj_HJJ = sorted(fileHjj.items(), key = lambda x:x[1])

for key, value in fileHjj_HJJ:
	print(key, value)