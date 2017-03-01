import urllib2
try:
    urllib2.urlopen('http://www.example.com/some_page')
except urllib2.HTTPError, e:
    print(e.code)
except urllib2.URLError, e:
:x
