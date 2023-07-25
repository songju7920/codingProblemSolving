#include <stdio.h>
#include <string.h>

int main() {
  int hour, min, sec;
  int wait;
  scanf("%d %d %d", &hour, &min, &sec);
  scanf("%d", &wait);

  sec += wait;
  min += sec / 60;
  sec -= (sec / 60) * 60;
  hour += min / 60;
  min -= (min / 60) * 60;
  hour %= 24;

  printf("%d %d %d", hour, min, sec);
}