// This is a testing file for intal (integer of arbitrary length) in C, to be used with the python file
// Author: Samyak S Sarnayak
// How to use
// 1. Compile this with your implementation file. Use `-o intal` while compiling
// 2. Run the python script to test it. (the python script will be here - https://gist.github.com/Samyak2/20eaef27510506fc74408f59cdcb3a2c)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "intal.h"

#define MAXDIGITS 1001

void read_multiple(int n, char **arr) {
    for(int i = 0; i < n; ++i) {
        scanf(" %s", arr[i]);
    }
}
double time_elapsed(struct timespec start, struct timespec end)
{
    double t;
    t = (end.tv_sec - start.tv_sec);                  //diff of tv_sec
    t += (end.tv_nsec - start.tv_nsec) * 0.000000001; //add diff of tv_nsec too
    return t;
}

int main(int argc, const char *argv[]) {
    char *result;
    struct timespec start, end;
    if (strcmp(argv[1], "array") == 0) {
        int n, temp;
        scanf(" %d", &n);
        /*char arr[n][MAXDIGITS];*/
        char **arr = (char**) malloc(n * sizeof(char*));
        for(int i = 0; i < n; i++) {
            arr[i] = (char*) malloc(MAXDIGITS * sizeof(char));
        }
        read_multiple(n, arr);
        if (strcmp(argv[2], "min") == 0) {
            result = (char*) malloc(sizeof(char) * (MAXDIGITS+1));
            clock_gettime(CLOCK_REALTIME, &start);
            temp = intal_min((char**) arr, n);
            clock_gettime(CLOCK_REALTIME, &end);
            sprintf(result, "%d", temp);
        } else if (strcmp(argv[2], "max") == 0) {
            result = (char*) malloc(sizeof(char) * (MAXDIGITS+1));
            clock_gettime(CLOCK_REALTIME, &start);
            temp = intal_max((char**) arr, n);
            clock_gettime(CLOCK_REALTIME, &end);
            sprintf(result, "%d", temp);
        } else if (strcmp(argv[2], "search") == 0) {
            result = (char*) malloc(sizeof(char) * (MAXDIGITS+1));
            char tosearch[MAXDIGITS];
            scanf(" %s", tosearch);
            clock_gettime(CLOCK_REALTIME, &start);
            temp = intal_search((char**) arr, n, tosearch);
            clock_gettime(CLOCK_REALTIME, &end);
            sprintf(result, "%d", temp);
        } else if (strcmp(argv[2], "binsearch") == 0) {
            result = (char*) malloc(sizeof(char) * (MAXDIGITS+1));
            char tosearch[MAXDIGITS];
            scanf(" %s", tosearch);
            clock_gettime(CLOCK_REALTIME, &start);
            temp = intal_binsearch((char**) arr, n, tosearch);
            clock_gettime(CLOCK_REALTIME, &end);
            sprintf(result, "%d", temp);
        } else if (strcmp(argv[2], "sort") == 0) {
            clock_gettime(CLOCK_REALTIME, &start);
            intal_sort((char**) arr, n);
            clock_gettime(CLOCK_REALTIME, &end);
            for(int i = 0; i < n; ++i) {
                printf("%s\n", arr[i]);
            }
            printf("%lf\n", time_elapsed(start, end));
            return 0;
        } else if (strcmp(argv[2], "coinrow") == 0) {
            clock_gettime(CLOCK_REALTIME, &start);
            result = coin_row_problem((char**) arr, n);
            clock_gettime(CLOCK_REALTIME, &end);
        } else {
            result = (char*) malloc(sizeof(char) * (MAXDIGITS+1));
            clock_gettime(CLOCK_REALTIME, &start);
            temp = intal_min((char**) arr, n);
            clock_gettime(CLOCK_REALTIME, &end);
            sprintf(result, "%d", temp);
        }
    } else if (strcmp(argv[1], "pow") == 0) {
        char num1[MAXDIGITS];
        scanf(" %s", num1);
        int num3;
        scanf(" %d", &num3);
        clock_gettime(CLOCK_REALTIME, &start);
        result = intal_pow(num1, num3);
        clock_gettime(CLOCK_REALTIME, &end);
    } else if (strcmp(argv[1], "fibo") == 0) {
        int num3;
        scanf(" %d", &num3);
        clock_gettime(CLOCK_REALTIME, &start);
        result = intal_fibonacci(num3);
        clock_gettime(CLOCK_REALTIME, &end);
    } else if (strcmp(argv[1], "fact") == 0) {
        int num3;
        scanf(" %d", &num3);
        clock_gettime(CLOCK_REALTIME, &start);
        result = intal_factorial(num3);
        clock_gettime(CLOCK_REALTIME, &end);
    } else if (strcmp(argv[1], "bincoeff") == 0) {
        int num3;
        int num4;
        scanf(" %d", &num3);
        scanf(" %d", &num4);
        clock_gettime(CLOCK_REALTIME, &start);
        result = intal_bincoeff(num3, num4);
        clock_gettime(CLOCK_REALTIME, &end);
    }


    else {
        char num1[MAXDIGITS];
        char num2[MAXDIGITS];
        scanf(" %s", num1);
        scanf(" %s", num2);
        if (strcmp(argv[1], "add") == 0) {
            clock_gettime(CLOCK_REALTIME, &start);
            result = intal_add(num1, num2);
            clock_gettime(CLOCK_REALTIME, &end);
        } else if (strcmp(argv[1], "diff") == 0) {
            clock_gettime(CLOCK_REALTIME, &start);
            result = intal_diff(num1, num2);
            clock_gettime(CLOCK_REALTIME, &end);
        } else if (strcmp(argv[1], "multiply") == 0) {
            clock_gettime(CLOCK_REALTIME, &start);
            result = intal_multiply(num1, num2);
            clock_gettime(CLOCK_REALTIME, &end);
        } else if (strcmp(argv[1], "mod") == 0) {
            clock_gettime(CLOCK_REALTIME, &start);
            result = intal_mod(num1, num2);
            clock_gettime(CLOCK_REALTIME, &end);
        } else if (strcmp(argv[1], "gcd") == 0) {
            clock_gettime(CLOCK_REALTIME, &start);
            result = intal_gcd(num1, num2);
            clock_gettime(CLOCK_REALTIME, &end);
        } else {
            clock_gettime(CLOCK_REALTIME, &start);
            result = intal_add(num1, num2);
            clock_gettime(CLOCK_REALTIME, &end);
        }
    }
    printf("%s\n", result);
    free(result);
    printf("%lf\n", time_elapsed(start, end));
    return 0;
}