#include <stdio.h>
#include <string.h>

int main() {
  char Board[5][16] = { 0 };
  
  for(int i = 0; i < 5; i++){
    scanf("%s", Board[i]);
  }
  
  for(int i = 0; i < 15; i++){
    for(int j = 0; j < 5; j++){
      if(Board[j][i] == '\0') continue;
      else printf("%c", Board[j][i]);
    }
  }
}