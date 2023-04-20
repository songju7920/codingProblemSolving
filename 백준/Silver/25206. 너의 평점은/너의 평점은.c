#include <stdio.h>
#include <string.h>

int main(void) {
  char Rating[3], SubjectName[51];
  float Grade, result = 0, sum = 0;

  for (int i = 0; i < 20; i++) {
    scanf("%s %f %s", SubjectName, &Grade, Rating);
    if(strcmp(Rating, "P") != 0)
      sum += Grade;
    if (strcmp(Rating, "A+") == 0)
      result += Grade * 4.5;
    else if (strcmp(Rating, "A0") == 0)
      result += Grade * 4.0;
    else if (strcmp(Rating, "B+") == 0)
      result += Grade * 3.5;
    else if (strcmp(Rating, "B0") == 0)
      result += Grade * 3.0;
    else if (strcmp(Rating, "C+") == 0)
      result += Grade * 2.5;
    else if (strcmp(Rating, "C0") == 0)
      result += Grade * 2.0;
    else if (strcmp(Rating, "D+") == 0)
      result += Grade * 1.5;
    else if (strcmp(Rating, "D0") == 0)
      result += Grade * 1.0;
    else
      result += Grade * 0.0;
  }
  
  printf("%f", result / sum);
  return 0;
}