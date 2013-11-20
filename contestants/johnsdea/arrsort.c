#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int const MAX_VALUES = 50;
FILE* input;

void create_array(int NUMS[]) {
    int MAX_LENGTH = 1;
    char value[MAX_LENGTH];

    int i = 0;
    int v = 0;
    while (fgets(value, MAX_LENGTH, input) != NULL) {
        v = value[i];
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
            if (a[j] < a[i])
                m = j;
        }
        t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}

void create_output(int NUMS[]) {
    FILE * output = fopen("arrsort_out", "w");
    for (int i=0; i<MAX_VALUES; i++) {
        if (fprintf(output, "%d\n", NUMS[i]) > 0)
            perror("There was an error writing to the file");
    }
    fclose(output);
}


int main() {
    input = fopen("arrsort_in", "r");
    int NUMS[MAX_VALUES];
    if (input == NULL) {
        perror("Unable to open the file");
        exit(EXIT_FAILURE);
    }

    create_array(NUMS);
    selection_sort(NUMS, MAX_VALUES);
    create_output(NUMS);

    fclose(input);
}
