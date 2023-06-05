#include <stdio.h>
#include <string.h>

int main() {
  int n;
  char nickName[100];
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    int idx = 3, start = 0;
    char newNickName[100] = {0};
    newNickName[0] = 'g';
    newNickName[1] = 'o';
    newNickName[2] = 'd';
    
    scanf(" %[^\n]", nickName);

    for (int j = 0; j < strlen(nickName); j++) {
      if (nickName[j] == ' ') {
        start++;
        break;
      } else
        start++;
    }

    for (int j = start; j < strlen(nickName); j++) {
      if (nickName[j] == ' ')
        continue;
      else {
        newNickName[idx] = nickName[j];
        idx++;
      }
    }
    printf("%s\n", newNickName);
  }
}