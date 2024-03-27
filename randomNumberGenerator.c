#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Modify the code below
int getRandomNumber(int a, int b) {
  int randomNumber = rand() % (b - a + 1) + a; //20 - 10 + 1 = 11 ; 10 ; 50 % 11 = 6
  return randomNumber;
}

int main(void) {
  srand(time(NULL));
  // Modify the code below

  int randomNumber = getRandomNumber(10, 20);
  printf("My random number is: %d", randomNumber);
}
