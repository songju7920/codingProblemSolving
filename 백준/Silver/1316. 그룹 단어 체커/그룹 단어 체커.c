#include <stdio.h>
#include <string.h>

int main(void) {
  char str[101];
  int N;
  scanf("%d", &N);
  int Cnt = N;

  for (int i = 0; i < N; i++) {
    scanf("%s", str);

    for (int j = 0; j < strlen(str); j++)
      for (int k = j+1; k < strlen(str); k++)
        if(str[j] == str[k] && str[k-1] != str[k]){
          Cnt--;
          goto jump;
        }
    jump:;
  }

  printf("%d", Cnt);
  return 0;
}