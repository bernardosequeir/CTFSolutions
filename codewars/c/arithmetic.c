#include <string.h>
double arithmetic(double a, double b, char *operator)
{
  if (strcmp("add", operator) == 0)
  {
    return a + b;
  }
  else if (strcmp("subtract", operator) == 0)
  {
    return a - b;
  }
  else if (strcmp("multiply", operator) == 0)
  {
    return a * b;
  }
  else if (strcmp("divide", operator) == 0)
  {
    return a / b;
  }
}