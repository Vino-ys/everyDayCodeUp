count = 0
n = int(input())

firstSet = set(input().split())

n = int(input())

secondSet = set(input().split())

result = sorted(firstSet & secondSet)

for _ in result:
	count += 1
	
print(count)
for i in result:
	print(i, end = " ")