n = int(input())
arr = list(map(int, input().split()))
negative = 0
positive = 0
zero = 0

for i in range(n):
	if(arr[i] < 0): negative += 1
	elif(arr[i] > 0): positive += 1
	else: zero += 1

print(positive, negative, zero)
	