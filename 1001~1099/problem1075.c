// [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기(설명)
#include <stdio.h>
int main() {
	int a = 1;
	scanf("%d",&a);
	a -= 1;
	while(a != 0) {
		printf("%d\n",a);
		a -= 1;
	}
	printf("0\n");
	return 0;
}