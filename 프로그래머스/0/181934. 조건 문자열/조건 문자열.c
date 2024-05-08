#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
int solution(const char* ineq, const char* eq, int n, int m) {
    if (strcmp(ineq, ">") == 0) {
        if (strcmp(eq, "=") == 0) {
            if (n >= m) return 1;
            else return 0;
        } else if (strcmp(eq, "!") == 0) {
            if (n > m) return 1;
            else return 0;
        } else {
            return -1; // Unknown equality condition
        }
    } else if (strcmp(ineq, "<") == 0) {
        if (strcmp(eq, "=") == 0) {
            if (n <= m) return 1;
            else return 0;
        } else if (strcmp(eq, "!") == 0) {
            if (n < m) return 1;
            else return 0;
        } else {
            return -1; // Unknown equality condition
        }
    } else {
        return -1; // Unknown inequality condition
    }
}
