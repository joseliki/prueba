import urllib2
import json
request = urllib2.Request('http://servizos.meteogalicia.es/apiv2/getTidesInfo?coord=-8.350573861318628,43.3697102138535&format=application/json&lang=es&startTime=2014-02-07&endTime=2014-03-07&API_KEY=tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p')
open = urllib2.build_opener()
f = opener.open(request)
json = json.loads(f.read())
print json

