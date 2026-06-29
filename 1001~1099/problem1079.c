#include <stdio.h>
int main() {
	char txt;
	while(txt != 'q') {
		scanf(" %c",&txt);
        //     ^- 여기에 공백 안넣어주면 오류 ㅜ 
		printf("%c\n",txt);
	}
	return 0;
}