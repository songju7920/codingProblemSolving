#include <stdio.h>
#include <string.h>

int main(void) {
  char str[100];
  int result = 1;
  scanf("%s",str);

  size_t str_len = strlen(str);
  for(int i = 0; i < str_len; i++) {
    if(str[str_len - 1 - i] != str[i]) {
      result = 0;
      break;
    }
  }
  printf("%d",result);
}