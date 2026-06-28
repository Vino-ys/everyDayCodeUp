#include <stdio.h>

int main() {
    int h, w, n, l, d, x, y;
    int arr[101][101];
    
    scanf("%d %d", &h, &w);
    
    for(int i = 1; i <= h; i++) for(int j = 1; j <= w; j++) arr[i][j] = 0;
    
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++) {
        scanf("%d %d %d %d", &l, &d, &x, &y);
        
        for(int j = 0; j < l; j++) {
            if(d == 0) arr[x][y + j] = 1;
            else arr[x + j][y] = 1;
        }
    }
    
    for(int i = 1; i <= h; i++) {
        for(int j = 1; j <= w; j++) printf("%d ", arr[i][j]);
        printf("\n");
    }
    
    return 0;
}