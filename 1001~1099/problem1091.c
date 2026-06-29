#include <stdio.h>
int main() {
	long long int a,r,d,n;
	scanf("%lld %lld %lld %lld", &a, &r, &d, &n);
	for(int i = 1; i < n;i++ ) {
		a *= r;
		a += d;
	}
	printf("%lld", a);
	return 0;
}