day = int(input())

record = list(map(int, input().split()))
mDayStart = 0
mDayFinish = 0
count = 0
maxCount = 0

for i in range(len(record)):
	
	if record[i] == 1:
		count += 1
	else:
		if count > maxCount:
			maxCount = count
			mDayFinish = i
			mDayStart = i - count + 1
			count = 0
	
print(maxCount, mDayStart, mDayFinish)