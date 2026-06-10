#include <stdio.h>
int main() {
    double h,b,c,s;
    scanf("%lf %lf %lf %lf",&h,&b,&c,&s);
    
    printf("%.1lf MB",((h * b * c * s) / 8) / 1024000);
    return 0;
}

// #include <stdio.h>

// int main() {

//     double h,b,c,s;

//     scanf("%lf %lf %lf %lf",&h,&b,&c,&s);

    

//     printf("%.1lf MB",((h * b * c * s) / 8) / 1024000);

//     return 0;

// } 정답이 32000 16 2 240 에 29.3 이 나와야 하는데 30.0이나와 ㅜㅜ