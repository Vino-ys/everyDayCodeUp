// [기초-반복실행구조]0 입력될 때까지 무한 출력하기1(설명)
#include <stdio.h>
int main() {
	int a = 0;
	goto notyung;
	notyung:
	scanf("%d",&a);
	if(a == 0) {
		return 0;
	}
	printf("%d\n",a);
	goto notyung;
}