#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char *dna_strand(const char *dna)
{
  char *result = strdup(dna);
  for (char *cp = result; *cp; ++cp)
  {
    switch (*cp)
    {
    case 'A':
      *cp = 'T';
      break;
    case 'C':
      *cp = 'G';
      break;
    case 'G':
      *cp = 'C';
      break;
    case 'T':
      *cp = 'A';
      break;
    }
  }
  return result;
}
int main()
{
  char *t1 = dna_strand("ATTGC"); /* return "TAACG" */
  char *t2 = dna_strand("GTAT");  /* return "CATA"  */
  printf(" Resultado do teste 1: %s\n", t1);
  printf(" Resultado do teste 2: %s\n", t2);
}