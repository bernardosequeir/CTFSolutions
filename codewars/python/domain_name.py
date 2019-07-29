def domain_name(url):
  return url.split('//')[1].split('.')[0] if (len(url.split('.') == 1)) else url.split('.')[1].split('.')[0]
print(domain_name("http://google.com"))
  