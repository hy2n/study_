#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* code) {
    int mode = 1;
    char* answer = (char*)malloc(strlen(code)*sizeof(char));
    int ans = 0;
    for (int x=0;code[x]!='\0';x++) {
        if (mode) { //Mode = True
            if (code[x] == '1') {
                mode = 0;
            }
            else {
                if ((x%2)==0) {
                    answer[ans] = code[x];
                    ans++;
                }
            }
        } else { //Mode = False
            if (code[x] == '1') {
                mode = 1;
            }
            else {
                if ((x%2)!=0) {
                    answer[ans] = code[x];
                    ans++;
                }
            }
        }
    }
    if (ans == 0) {
            return "EMPTY";
        } else answer[ans] = '\0';
    return answer;
}