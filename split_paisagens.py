import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch



#mapa='buffers_2k_raster_tif'
mapa='buffers_2k_raster_sem_desloc_tif'
mapa_veg='classificada_2014_binMata'
lista_classificada=grass.mlist_grouped ('rast', pattern='*binMata') ['PERMANENT']




del lista_classificada[-1]
for a in lista_classificada:
    grass.run_command('g.region',rast=a)
    x=grass.read_command('r.stats',input=mapa)
    y=x.split('\n')
    del y[-1]
    del y[-1]
    for i in y:
        print i
        format='00'+i
        format=format[-2:]
        expressao2=a+format+'=if('+mapa+'=='+i+','+a+',null())'
        grass.mapcalc(expressao2, overwrite = True, quiet = True)  