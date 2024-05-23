#include <stdio.h>

int main(void) {
    int a;
    int b;
    scanf("%d %d", &a, &b);
    for (int x=0;x<b;x++) {
        for (int q=0;q<a;q++) printf("*");
        printf("\n");
    }
    return 0;
}