from urllib2 import urlopen

site = urlopen("http://oliverspohngellert.com")
print site.read()