#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Never use magic numbers
int const MAX_VALUES = 50;
// Our array of numbers that needs to be filled and sorted
int NUMS[MAX_VALUES];
// The input file (arrsort_in)
FILE* input;

void create_array() {
    // Max line length of a positive 32bit integer and the endline
    int MAX_LENGTH = 11;
    char value[MAX_LENGTH];

    // Index into the NUMS array
    int i = 0;
    // Integer value to be inserted into the array
    int v = 0;
    // While reading lines
    while (fgets(value, MAX_LENGTH, input) != NULL) {
        // Convert from ascii characters to an integer
        v = atoi(value);
        // Insert that integer into the nums array at position i
        NUMS[i] = v;
        // Increment our index into the MUMS array
        i++;
        // In case there are more lines than room in the array, break
        if (i >= MAX_VALUES)
            break;
    }
}

void selection_sort(int *a, int n) {
    // https://en.wikipedia.org/wiki/Selection_sort
    // Code : https://rosettacode.org/wiki/Sorting_algorithms/Selection_sort#C
    int i, j, m, t;
    for (i = 0; i < n; i++) {
        for (j = i, m = i; j < n; j++) {
            if (a[j] < a[m])
                m = j;
        }
        t = a[i];
        a[i] = a[m];
        a[m] = t;
    }
}

void create_output() {
    // Open arrsort_out
    FILE *output = fopen("arrsort_out", "w");

    for (int i=0; i<MAX_VALUES; i++) {
        if (fprintf(output, "%d\n", NUMS[i]) < 0)
            perror("There was an error writing to the file");
    }

    // Clean up
    fclose(output);
}


int main() {
    // Open arrsort_in
    input = fopen("arrsort_in", "r");
    if (input == NULL) {
        perror("Unable to open the file");
        exit(EXIT_FAILURE);
    }

    // Do all the work
    create_array();
    selection_sort(NUMS, MAX_VALUES);
    create_output();

    // Clean up
    fclose(input);
}
