import re

regex = re.compile('[a-z]{4,}', re.IGNORECASE)

def replace(match):
  word = match.group(0)
  return word[0] + str(len(word) - 2) + word[-1]

def abbreviate(s):
  return regex.sub(replace, s)


print(abbreviate("internationalization"), "i18n")
print(abbreviate("accessibility"), "a11y")
print(abbreviate("Accessibility"), "A11y")
print(abbreviate("elephant-ride"), "e6t-r2e")
