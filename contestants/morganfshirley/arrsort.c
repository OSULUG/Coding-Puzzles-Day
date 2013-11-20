#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

const int MAX_VALUES = 50;

void adjust_up(int*,int);

int create_array(int *NUMS, FILE *input) {
    int MAX_LENGTH = 1024;
    char buf[MAX_LENGTH];
    char *p;

    int i = 0;
    int v = 0;
    p = fgets(buf, MAX_LENGTH, input);
    int n = 1;
    while(sscanf(p+=n, "%d%n", &v, &n) != 0) {
        NUMS[i] = v;
	adjust_up(NUMS, i);
        i++;
	n+=1;
        if (i >= MAX_VALUES)
            break;
    }
	return i;
}

void adjust_up(int *array, int pos) {
	int temp;
	if(array[pos] > array[(pos-1)/2]) {
		temp = array[pos];
		array[pos] = array[(pos-1)/2];
		array[(pos-1)/2] = temp;
		adjust_up(array, (pos-1)/2);
	}
}

void adjust_down(int *array, int size, int pos) {
	//Adjust down
	int left = 2*pos + 1;
	int right = 2*pos + 2;

	int temp, temp2; //fuck making code readable

	if(right<size) {
		if(array[right] < array[left]) {
			temp = left;
		}
		else {
			temp = right;
		}
		if(array[pos] < array[temp]) {
			temp2 = array[pos];
			array[pos] = array[temp];
			array[temp] = temp2;
			adjust_down(array, size, temp);
		}
	}
	if(left<size) {
		temp = left;
		if(array[pos] < array[temp]) {
			temp2 = array[pos];
			array[pos] = array[temp];
			array[temp] = temp2;
			adjust_down(array, size, temp);
		}
	}

}

void heap_sort(int *array, int size) {
	if(size == 0) {
		//We're done!
		return;
	}
	//Swap to back
	int temp = array[size-1];
	array[size-1] = array[0];
	array[0] = temp;
	size--;
	adjust_down(array, size, 0);
	heap_sort(array, size);

}

void create_output(int *NUMS, int size) {
    FILE *output = fopen("arrsort_out", "w");
    for (int i=0; i<size; i++) {
        if (fprintf(output, "%d\n", NUMS[i]) < 0)
            perror("There was an error writing to the file");
    }
    fclose(output);
}


int main() {
	int NUMS[MAX_VALUES];
	FILE* input;
    input = fopen("arrsort_in", "r");
    if (input == NULL) {
        perror("Unable to open the file");
        exit(EXIT_FAILURE);
    }

    int size = create_array(NUMS, input);
    heap_sort(NUMS, size);
    create_output(NUMS, size);

    fclose(input);
}
