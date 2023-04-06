#include <stdio.h>

int main (void)
{
  int location;
  char String[1000];
  scanf("%s", String);
  scanf("%d", &location);
  printf("%c", String[location - 1]);
}