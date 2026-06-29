#include <stdio.h>
int main() {
    int w,h,b;
	double s;
    scanf("%d %d %d",&w,&h,&b);
    s = w * h * b;
    printf("%.2lf MB",((s/8) / 1024) / 1024);
    return 0;
}