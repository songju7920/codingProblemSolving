#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) 
{
  int first;
	int second[3] = {0, };
	scanf("%d", &first);
  for(int i = 0; i < 3; i++)
    {
	    scanf("%1d", &second[i]);
    }
  printf("%d\n", first * second[2]);
  printf("%d\n", first * second[1]);
  printf("%d\n", first * second[0]);
  int result = first * second[2] + 10 * first * second[1]+ 100 * first * second[0];
  printf("%d\n", result);
  return 0;
}