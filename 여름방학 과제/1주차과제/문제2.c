#include <stdio.h>
int main() {
	int num, max, sum = 0, isbig = 0;
	int arr[101];
	scanf("%d %d", &num, &max);

	for(int i = 0; i < num; i++) scanf("%d", &arr[i]);

	for(int i = 0; i < num; i++) sum += arr[i];

	for(int i = 0; i < num; i++){
		if(sum > max) isbig = 1;
		else isbig = 0;
	}
	if(isbig) {
		printf("%d ", max);
		printf("%d ", sum - max);
	}
	else printf("%d", sum);
	
	return 0;
}