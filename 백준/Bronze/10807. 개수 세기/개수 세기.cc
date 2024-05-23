#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int acc,v;
    scanf("%d",&acc);
    int *array = (int *)malloc(acc * sizeof(int));
    
    for(int x=0;x<acc;x++) {
        scanf("%d",&array[x]);
    }
    scanf("%d",&v);
    
    int trigger = 0;
    for (int x=0;x<acc;x++)  {
        if (v == array[x]) trigger++;
    }
    
    printf("%d",trigger);
}