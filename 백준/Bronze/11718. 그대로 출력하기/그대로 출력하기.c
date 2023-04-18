#include <stdio.h>
#include <string.h>

int main(void) {
  char str;
  while (scanf("%c", &str) != -1)
    printf("%c", str);
  return 0;
}