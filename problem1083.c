#include <stdio.h>
int main() {
	int i,num;
	scanf("%d",&num);
	for(i = 1; i <= num; i++){
		if(i % 3 == 0) {
			printf("X ");
		}
		else {
			printf("%d ", i);
		}
	}
	return 0;
}