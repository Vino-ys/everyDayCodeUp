n = int(input())
nlist = list(map(int, input().split()))
ndict = {}
q = int(input())
qarr = list(map(int, input().split()))

result =  []
for idx, value in enumerate(nlist):
		ndict[value] = idx + 1

for i in qarr:
	if i in ndict:
		print(ndict[i], end = " ")
	else:
		print('-1', end = " ")