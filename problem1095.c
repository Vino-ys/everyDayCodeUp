#include <stdio.h>
int main() {
	int num,min= 25;
	int arr[10000] = {};
	
	scanf("%d", &num);
	
	for(int i = 0;i < num; i++) scanf("%d", &arr[i]);
	
	for(int i = 0;i < num; i++ ) if(min > arr[i]) min = arr[i];
	printf("%d", min);
	return 0;
}