#include <stdio.h>

int main(void) {
    int a;
    double b;
    scanf("%d %lf", &a, &b);
    printf("%.9lf", a / b);
    return 0;
}
