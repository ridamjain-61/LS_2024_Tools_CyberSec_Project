#include <stdio.h>
#include <stdlib.h>

#define TAPE_SIZE 30000

void execute_brainfuck(const char *code) {
    char tape[TAPE_SIZE] = {0};
    // standard tape size of 30000
    char *ptr = tape;
    // pointer which points at the cells of the array
    // const char *pc = code;

    while (*code) {
        switch (*code) {
            case '>':
                // TODO
                ptr++;
                break;
            case '<':
                // TODO
                ptr--;
                break;
            case '+':
                // TODO
                (*ptr)++;
                break;
            case '-':
                // TODO
                (*ptr)--;
                break;
            case '.':
                putchar(*ptr);
                // TODO
                break;
            case ',':
                *ptr = getchar();
                // TODO
                break;
            case '[':
                // TODO
                // beginning of loop
                if (*ptr == 0) {
                    int count = 1;
                    while (count > 0) {
                        ++code;
                        if (*code == '[') count++;
                        if (*code == ']') count--;
                    }
                }
                break;
            case ']':
                // TODO
                if (*ptr != 0) {
                    int count = 1;
                    while (count > 0) {
                        --code;
                        if (*code == '[') count--;
                        if (*code == ']') count++;
                    }
                }
                break;
            default:
				// TODO
                // do nothing if something else encountered
                break;
        }
        ++code;
        // move to the next
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s \"<brainfuck code>\"\n", argv[0]);
        return 1;
    }

    execute_brainfuck(argv[1]);

    return 0;
}
