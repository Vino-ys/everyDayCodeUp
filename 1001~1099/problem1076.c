// [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)
#include <stdio.h>
int main() {
	char ap;
	char b = 'a';
	scanf(" %c",&ap);
	do {
		if(b > ap){
			break;
		}
		printf("%c ",b);
			b += 1;
	}while(b < 'z' + 1);
	return 0;
}