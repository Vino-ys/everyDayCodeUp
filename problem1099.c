#include <stdio.h>
int main() {
	int arr[12][12];
	int x = 2, y = 2;
	for(int i = 1; i < 11; i++) for(int j = 1; j < 11; j++) scanf("%d", &arr[i][j]);
	
	while(1) {
		
		if(arr[x][y] == 2) {
			arr[x][y] = 9;
			break;
		}
		
		arr[x][y] = 9;
		
		if(arr[x][y + 1] != 1) y++;
		else if(arr[x + 1][y] != 1) x++;
		else break;
		
		}
	

	for(int i = 1; i < 11; i++) {
		for(int j = 1; j < 11; j++) printf("%d ", arr[i][j]);
		printf("\n");
	}
	
	return 0;
}