#include <stdio.h>

int main() {
  int playerPOS[2][3];

  for (int i = 0; i < 3; i++) {
    scanf("%d %d", &playerPOS[0][i], &playerPOS[1][i]);
  }

  int cal1 = playerPOS[0][0] - playerPOS[0][1];
  int cal2 = playerPOS[1][0] - playerPOS[1][1];
  double inclination1 = (double)cal1 / cal2;
  if(cal1 == 0 || cal2 == 0){
    inclination1 = 0;
  }

  cal1 = playerPOS[0][2] - playerPOS[0][1];
  cal2 = playerPOS[1][2] - playerPOS[1][1];
  double inclination2 = (double)cal1 / cal2;
  if(cal1 == 0 || cal2 == 0){
    inclination2 = 0;
  }

  cal1 = playerPOS[0][2] - playerPOS[0][0];
  cal2 = playerPOS[1][2] - playerPOS[1][0];
  double inclination3 = (double)cal1 / cal2;
  if(cal1 == 0 || cal2 == 0){
    inclination3 = 0;
  }
  
  if (inclination1 == inclination2 && inclination1 == inclination3) {
    printf("WHERE IS MY CHICKEN?");
  } else {
    printf("WINNER WINNER CHICKEN DINNER!");
  }
}