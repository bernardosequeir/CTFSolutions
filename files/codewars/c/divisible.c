#include <stdbool.h>

bool isDivisible(int n, int x, int y)
{
  if (n % x == 0 && n % y == 0)
  {
    return true;
  }
  return false;
}

int main()
{
  printf(isDivisible(12, 4, 3) ? "true\n" : "false\n");
  printf(isDivisible(12, 3, 4) ? "true" : "false");
  printf(isDivisible(3, 3, 4) ? "true" : "false");
}