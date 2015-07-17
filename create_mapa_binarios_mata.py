import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch


lista_classificada=grass.mlist_grouped ('rast', pattern='*classificada*') ['PERMANENT']

for i in lista_classificada:
    print i
    #grass.run_command('g.region' ,rast=i)
    #expressao2=i+"_binMata=if("+i+"==11 || "+i+"==12 || "+i+"==13,1,0)"
    #grass.mapcalc(expressao2, overwrite = True, quiet = True)    
