#include <stdio.h>

int main() {
    FILE *file = fopen("input.txt", "r");
    char line[10000];
    
    while (fgets(line, sizeof(line), file)) {
        int floor = 0;
        int bii = 0;

        for (int i = 0; line[i] != '\0'; ++i) {
            if (line[i] == '(') {
                floor += 1;
            } else if (line[i] == ')') {
                floor -= 1;
            }

            if (floor < 0 && bii == 0) {
                bii = i + 1;
            }
        }

        printf("Part1: %d\n", floor);
        printf("Part2: %d\n", bii);
    }

    fclose(file);
    return 0;
}