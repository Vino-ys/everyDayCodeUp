text = input()
count = 1
for i in range(len(text)):

	if i == len(text) -1 or text[i] != text[i + 1]:
		print(text[i], end = "")
		print(count, end = " ")
		count = 1
	else: count += 1