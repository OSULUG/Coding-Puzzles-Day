/* by mouche */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_VALUES 50

int NUMS[MAX_VALUES];
FILE* input;

int create_array() {
	char ch;
	char buf[10] = { 0 };

	int value;
	int nums_i = 0;
	int buf_i = 0;
    while ((ch = fgetc(input)) != EOF)
	{
		// Skip these
		if (ch == '[') continue;
		if (ch == ' ') continue;

		// End current number
		if (ch == ',' || ch == ']' && buf[0] != 0)
		{
			buf[buf_i] = '\0';
			value = atoi(buf);	
			NUMS[nums_i] = value;
			nums_i++;

			// Quit if we've hit the max number of values
			if (nums_i >= MAX_VALUES)
				break;

			// Reset buf
			buf_i = 0;
			buf[0] = '\0';
		}
		else
		{
			// Add new char to buf
			buf[buf_i] = ch;
			buf_i++;
		}
    }
	return nums_i;
}

void selection_sort(int *a, int n) {
    int i, j, m, t;
    for (i = 0; i < n; i++) {
		m = i;
        for (j = i; j < n; j++) {
            if (a[j] < a[m])
                m = j;
        }
		if (m != i)
		{
			t = a[i];
			a[i] = a[m];
			a[m] = t;
		}
    }
}

void create_output(num_inputs) {
	FILE *output = fopen("arrsort_out", "w");
	int i;
	fprintf(output,"[");
    for (i=0; i<num_inputs; i++) {
        if (fprintf(output, "%d", NUMS[i]) < 0)
            perror("There was an error writing to the file");
		if (i != num_inputs - 1)
			fprintf(output, ", ");
    }
	fprintf(output, "]\n");
    fclose(output);
}


int main() {
    input = fopen("arrsort_in","r");
	int num_inputs = 0;
    if (input == NULL) {
        perror("Unable to open the file");
        exit(EXIT_FAILURE);
    }

    num_inputs = create_array();
    selection_sort(NUMS, num_inputs);
    create_output(num_inputs);

    fclose(input);
}
