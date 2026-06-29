#include <stdio.h>
int main() {
	int sum = 0,num = 0,last;
	scanf("%d",&num);
	for(int i = 0;sum < num;i++){
		sum += i;
		last = i;
	}
	printf("%d",last);
	return 0;
}