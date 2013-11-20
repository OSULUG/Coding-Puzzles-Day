#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int const MAX_VALUES = 50;
int NUMS[MAX_VALUES];
FILE* input;

void create_array() {
    int MAX_LENGTH = 1;
    char value[MAX_LENGTH];

    int i = 0;
    int v = 0;
    while (fgets(value, MAX_LENGTH, input) != NULL) {
        v = value;
        NUMS[i] = v;
        i++;
        if (i >= MAX_VALUES)
            break;
    }
}

void selection_sort(int *a, int n) {
    int i, j, m, t;
    for (i = 0; i < n; i++) {
        for (j = i, n = i; j < n; j++) {
            if (a[j] < a[m])
                m = j;
        }
        t = a[i];
        a[i] = a[m];
        a[m] = t;
    }
}

void create_output() {
    int *output = fopen("arrsort_out", "w");
    for (int i=0; i<MAX_VALUES; i++) {
        if (fprintf(output, "%s\n", NUMS[i]) > 0)
            perror("There was an error writing to the file");
    }
    fclose(output);
}


int main() {
    input = fopen("arrsort_in");
    if (input == NULL) {
        perror("Unable to open the file");
        exit(EXIT_FAILURE);
    }

    create_array();
    selection_sort(NUMS, MAX_VALUES);
    create_output();

    fclose(input);
}
