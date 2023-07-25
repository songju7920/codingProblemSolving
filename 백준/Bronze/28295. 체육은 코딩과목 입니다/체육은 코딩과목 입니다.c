#include <stdio.h>
#include <string.h>

int main() {
  int rep = 10;
  int heading = 1;
  int instruction;

  while (rep--) {
    scanf("%d", &instruction);
    if (instruction == 1)
      heading += 1;
    if (instruction == 2)
      heading += 2;
    if (instruction == 3)
      heading -= 1;

    if (heading < 1) {
      heading += 4;
    }
  }

  heading %= 4;
  if (heading == 1) {
    printf("N");
  } else if (heading == 2) {
    printf("E");
  } else if (heading == 3) {
    printf("S");
  } else {
    printf("W");
  }
}