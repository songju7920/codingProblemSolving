#include <stdio.h>
#include <string.h>

int main(void) {
  int Cnt[27], best = 0, Alpabet = 0, result = 0;
  for(int i = 0; i < 26; i++)
    Cnt[i] = 0;
  char str[1000001];
  scanf("%s", str);
  
  size_t str_len = strlen(str);
  
  for (int i = 0; i < str_len; i++)
    for(int j = 65; j < 91; j++)
      if(str[i] == j || str[i] - 32 == j)
        Cnt[j-65]++;
  
  for (int i = 0; i < 26; i++) {
    if(Cnt[i] > best) {
      best = Cnt[i];
      Alpabet = i + 65;
    }
  }
  for(int i = 0; i < 26; i++)
    if(best == Cnt[i]) {
      result++;
    }
  if(result > 1)
    printf("?");
  else
    printf("%c", Alpabet);
}