#include <unistd.h>
int points(const char *const games[])
{
  int total_points = 0;
  for (int i = 0; i < 10; i++)
  {
    int t1 = atoi(games[i][0]);
    int t2 = atoi(games[i][2]);
    if (t1 > t2)
    {
      total_points += 3;
    }
    else if (t1 == t2)
    {
      total_points++;
    }
  }
  return total_points;
}

int main()
{
  return 0;
}