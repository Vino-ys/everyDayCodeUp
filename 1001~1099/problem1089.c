#include <stdio.h>
int main() {
	int s,d,l;
	scanf("%d %d %d", &s, &d, &l);
	for(int i = 1; i < l;i++ ) s += d;
	printf("%d", s);
	return 0;
}