import requests
import json
provincias = ['a coruna','lugo','ourense','pontevedra']
p = raw_input("escribe la provincia de galicia que quieres consultar sus coordenadas")
API_KEY = "tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p"
req = requests.get("http://servizos.meteogalicia.es/apiv2/getTidesInfo?",params={'location':provincias[p],'key':API_KEY}
dato = json.loads(p.text)
print "la coordenada de",provincias[p], "es:",dato['coordinates']
