#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    int leng;
    int flag = 1;
    scanf("%d",&leng);
    char *match = (char *)malloc((leng + 1) * sizeof(char));
    char xr[50][100] = {};
    for (int i = 0; i < 50; ++i) {
        strcpy(xr[i], "\0");
    }
    
    for (int x=0;x<leng;) {
        scanf("%s",xr[x]);
        x++;
    }
    
    for (int i=0;i<leng;i++) {
        for (int x=0;'\0'!=xr[i][x];) {
            if (flag) {
                match[x] = xr[i][x];
            }
            else {
                if (match[x] != xr[i][x]) match[x] = '?';
            }
            //printf("%c",xr[i][x]);
            //match[x] = xr[i][x];
            x++;
        }
        flag = 0;
    }
    printf("%s",match);
}