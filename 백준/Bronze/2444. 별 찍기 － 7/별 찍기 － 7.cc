#include <stdio.h>

int main(void) {
    int stars;
    int space;
    int routes = 0;
    int flag = 0;
    
    scanf("%d",&stars);
    space = stars - 1;
    for (int x=stars;x>0;) {
        for (int i=space;i>0;i--) {
            printf(" ");
        }
        for (int i=(space==stars-1)?1 :(stars-x)*2+1;i>0;i--) {
            printf("*");
        }
        printf("\n");
        if ((space == 0)&&(flag == 0)) flag = 1;
        (flag == 1) ? space++:space--;
        (flag == 1) ? x++:x--;
        if(routes>(stars*2)-2) return 0;
        routes++;
    }
}