#!/usr/bin/python
import urllib2
import sys

web = raw_input("web es http://")
userAgent = "NuestroNavegador"
headers = { 'User-Agent' : userAgent }
req = urllib2.Request("http://"+web , None, headers)
response = urllib2.urlopen(req)
print response.read()
response.close()

