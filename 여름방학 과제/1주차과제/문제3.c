#include <stdio.h>
int main() {
	int r, c, k, count = 1;
	int arr[1001][1001];

	scanf("%d %d %d", &r, &c, &k);

	for(int i = 0; i < r; i++) for(int j = 0; j < c; j++) {
		arr[i][j] = count;
		count += 1;
	}
	
	for(int i = 0; i < r; i++) for(int j = 0; j < c; j++){
		if(arr[i][j] == k) printf("%d %d", r - 1, c - 1);
	}
	
	return 0;
}
