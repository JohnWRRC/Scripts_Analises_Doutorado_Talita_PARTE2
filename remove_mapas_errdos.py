import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch

lista_classificada_FRAG120m_mata_clump_AreaHA=grass.mlist_grouped ('rast', pattern='**') ['PERMANENT']
for i in lista_classificada_FRAG120m_mata_clump_AreaHA:
    
        #print i
        grass.run_command('g.remove',flags='f',rast=i)
    