num = int(input())
numList = list(map(int, input().split()))
numList.sort()

checkarr = []
count = 0

for i in range(len(numList)):
	
	if numList[i] not in checkarr:
		num = numList[i]
		checkarr.append(num)
	
		for j in range(len(numList)):
			if num == numList[j]:
				count += 1
			
		print(num, count)
		count = 0