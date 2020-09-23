#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
char *to_alternating_case(const char *s)
{
  char *alt_str;
  for (int i = 0; s[i] != '\0'; i++)
  {
    if (isalpha(s[i]))
    {
      if (islower(s[i]))
      {
        alt_str[i] = toupper(s[i]);
      }
      else
      {
        alt_str[i] = tolower(s[i]);
      }
    }
    else
    {
      alt_str[i] = s[i];
    }
  }
  return alt_str;
}

int main(int argc, char const *argv[])
{
}
