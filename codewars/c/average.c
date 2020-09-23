#include <stdio.h>

double find_average(double *array, int length)
{
  double avg = 0;
  for (size_t i = 0; i < length; i++)
  {
    avg += array[i];
  }
  avg = avg / length;
  printf("The average is: %f\n", avg);
}

int main(int argc, char const *argv[])
{
  double array[] = {17, 16, 16, 16, 16, 15, 17, 17, 15, 5, 17, 17, 16};
  find_average(array, (int)(sizeof(array) / sizeof(double)));
}
