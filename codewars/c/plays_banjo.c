#include <string.h>
char *are_you_playing_banjo(const char *name)
{
  if (name[0] == "r" || name[0] == "R")
  {
    return (name + " plays banjo");
  }
}