//문제1072: [기초-반복실행구조] 정수 입력받아 계속 출력하기(설명)
#include <stdio.h>
int main() {
	int a = 0;
	int b = 0;
	scanf("%d",&b);
	goto notyung;
	notyung:
	scanf("%d",&a);
	if(b-- == 0) {
		return 0;
	}
	printf("%d\n",a);
	goto notyung;
}