#include <stdio.h>
int main() {
	int n, min, max, nn = 0, h = 0;
	int arr[101];

	scanf("%d %d %d", &n, &min, &max);

	for(int i = 0; i < n; i++) scanf("%d", &arr[i]);

	for(int i = 0; i < n; i++) {
		if(arr[i] < min) nn++;
		else if(arr[i] > max) h++;
	}

	printf("%d %d", nn, h);
	return 0;
}
