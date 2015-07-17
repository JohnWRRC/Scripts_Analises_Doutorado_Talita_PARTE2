import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch
lista_arquivos=[]
LISTA=[]
LISTA=[]  

grupo=grass.mlist_grouped ('rast', pattern="**") ['PERMANENT']

for i in grupo:
    exp=i+"New=if("+i+"==128,null(),"+i+")"
    #print exp
    grass.run_command('g.region',rast=i)
    grass.mapcalc(exp, overwrite = True, quiet = True)
    grass.run_command('g.remove',rast=i,flags='f')
    