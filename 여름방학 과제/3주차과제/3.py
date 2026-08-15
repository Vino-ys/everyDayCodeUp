seat, reserve = map(int, input().split())
arr = ['O'] * seat

reserveSeat = list(map(int, input().split()))

for i in reserveSeat:
	arr[i - 1] = 'X'

for i in range(seat):
	print(arr[i], end = '')