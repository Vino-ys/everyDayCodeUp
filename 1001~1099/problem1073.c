//[기초 반복실행 구조] 0 입력될 때까지 무한 출력하기2(설명)
#include <stdio.h>
int main() {
	int a = 1;
	while (a != 0) {
		scanf("%d",&a);
		if(a == 0) break;
		printf("%d\n",a);
	}
	return 0;
}