#include <stdio.h>

int main(void) {
    int arr[6];
    int ans[6] = {0,};
    int orign[6] = {1,1,2,2,2,8};
    
    scanf("%d %d %d %d %d %d",&arr[0],&arr[1],&arr[2],&arr[3],&arr[4],&arr[5]);
    
    for (int x=0; x<6 ; x++) {
        while (arr[x]<orign[x]) {
            arr[x]++;
            ans[x]++;
        }
        while (arr[x]>orign[x]) {
            arr[x]--;
            ans[x]--;
        }
    }
    
    for (int x=0;x<6;x++) {
        printf("%d ",ans[x]);
    }
}