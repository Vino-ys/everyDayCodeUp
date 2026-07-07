#include <stdio.h>
int main() {
	char name[11], s;
	int age;
	float pi;
	scanf("%s", &name);
	scanf("%d", &age);
	scanf(" %c", &s);
	scanf("%f", &pi);
	
	printf("%s\n", name);
	printf("%d\n", age);
	printf("%c\n", s);
	printf("%g\n", pi);
	
    return 0;
}