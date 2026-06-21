#include <stdio.h>
int main() {
	int num,num2;
	int arr[24] = {};
	
	scanf("%d", &num);
	for(int i = 1; i <= num; i++) {
		scanf("%d", &num2);
		arr[num2] += 1;
	}
	
	for(int i = 1; i <= 23; i++) {
		printf("%d ", arr[i]);
	}
	return 0;
}