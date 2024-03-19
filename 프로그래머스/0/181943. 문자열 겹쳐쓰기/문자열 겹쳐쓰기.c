#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string, const char* overwrite_string, int s) {
    int my_string_len = strlen(my_string);
    int overwrite_len = strlen(overwrite_string);
    int new_string_len = my_string_len - overwrite_len + 1; // 새로운 문자열의 길이

    // 새로운 문자열을 저장할 메모리 할당
    char* answer = (char*)malloc(sizeof(char) * (my_string_len + 1)); // NULL 문자를 포함하여 할당

    int i, x;
    for (i = 0; i < my_string_len; i++) {
        if (i == s) {
            for (x = 0; x < overwrite_len; x++) {
                answer[i] = overwrite_string[x];
                i++;
            }
            i--;
        }
        else {
            answer[i] = my_string[i];
        }
    }
    answer[i] = '\0';

    return answer;
}
