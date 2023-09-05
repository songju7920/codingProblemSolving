#include <stdio.h>

int main(void) {
  char MS[2];
  char TK[2];

  scanf("%c %c %c %c", &MS[0], &MS[1], &TK[0], &TK[1]);

  if (MS[0] == MS[1]) {
    if (MS[0] == 'R' && TK[0] == 'P' || MS[0] == 'R' && TK[1] == 'P') {
      printf("TK");
      return 0;
    }
    if (MS[0] == 'P' && TK[0] == 'S' || MS[0] == 'P' && TK[1] == 'S') {
      printf("TK");
      return 0;
    }
    if (MS[0] == 'S' && TK[0] == 'R' || MS[0] == 'S' && TK[1] == 'R') {
      printf("TK");
      return 0;
    }
  }

  if (TK[0] == TK[1]) {
    if (TK[0] == 'R' && MS[0] == 'P' || TK[0] == 'R' && MS[1] == 'P') {
      printf("MS");
      return 0;
    }
    if (TK[0] == 'P' && MS[0] == 'S' || TK[0] == 'P' && MS[1] == 'S') {
      printf("MS");
      return 0;
    }
    if (TK[0] == 'S' && MS[0] == 'R' || TK[0] == 'S' && MS[1] == 'R') {
      printf("MS");
      return 0;
    }
  }

  printf("?");
}