import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch


'''
para cada paisagem(buffer) separadamente, foram extraidas algumas metricas de conectividade
sendo elas: conectividade funcional, fragmentacao e area de fragmento.

'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
lista_classificada_FRAG120m_mata_clump_AreaHA=grass.mlist_grouped ('rast', pattern='*FRAG120m_mata_clump_AreaHA*') ['PERMANENT']
lista_classificada_FRAG60m_mata_clump_AreaHA=grass.mlist_grouped ('rast', pattern='*FRAG60m_mata_clump_AreaHA*') ['PERMANENT']
lista_classificada_patch_clump_mata_limpa_AreaHA=grass.mlist_grouped ('rast', pattern='*patch_clump_mata_limpa_AreaHA*') ['PERMANENT']
lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA=grass.mlist_grouped ('rast', pattern='*dila_120m_orig_clump_mata_limpa_AreaHA*') ['PERMANENT']
lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA=grass.mlist_grouped ('rast', pattern='*dila_60m_orig_clump_mata_limpa_AreaHA*') ['PERMANENT']
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Criando grupo de vetor de 2014
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
lista_vectors_2014=grass.mlist_grouped ('vect', pattern='*2014*') ['PERMANENT']
#---------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
extraindo valores para os mapas de areas fragmentadas com 120 metros de erosao

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
cont_map_vect=0
while len(lista_classificada_FRAG120m_mata_clump_AreaHA)>0:
    if "2014" in lista_classificada_FRAG120m_mata_clump_AreaHA[0]:
        #print lista_classificada_FRAG120m_mata_clump_AreaHA[0],lista_vectors_2014[cont_map_vect]
        grass.run_command('g.region',rast=lista_classificada_FRAG120m_mata_clump_AreaHA[0])
        """
        120
        """
        grass.run_command('v.what.rast', vector=lista_vectors_2014[cont_map_vect],raster=lista_classificada_FRAG120m_mata_clump_AreaHA[0], column="FG120_2014")
        cont_map_vect=cont_map_vect+1
    del lista_classificada_FRAG120m_mata_clump_AreaHA[0]


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
extraindo valores para os mapas de areas fragmentadas com 60 metros de erosao

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
cont_map_vect=0
while len(lista_classificada_FRAG60m_mata_clump_AreaHA)>0:
    if "2014" in lista_classificada_FRAG60m_mata_clump_AreaHA[0]:
        #print lista_classificada_FRAG60m_mata_clump_AreaHA[0],lista_vectors_2014[cont_map_vect]
        grass.run_command('g.region',rast=lista_classificada_FRAG60m_mata_clump_AreaHA[0])
        """
        60
        """
        grass.run_command('v.what.rast', vector=lista_vectors_2014[cont_map_vect],raster=lista_classificada_FRAG60m_mata_clump_AreaHA[0], column="FG060_2014")
        cont_map_vect=cont_map_vect+1
        
        
    
    del lista_classificada_FRAG60m_mata_clump_AreaHA[0]  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------    


"""
extraindo valores para os mapas de areas reais dos fragmentos sem alteracao

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
cont_map_vect=0 
while len(lista_classificada_patch_clump_mata_limpa_AreaHA)>0:
    if "2014" in lista_classificada_patch_clump_mata_limpa_AreaHA[0]:
        #print lista_classificada_patch_clump_mata_limpa_AreaHA[0],lista_vectors_2014[cont_map_vect]
        grass.run_command('g.region',rast=lista_classificada_patch_clump_mata_limpa_AreaHA[0])
        """
        patch
        """
        grass.run_command('v.what.rast', vector=lista_vectors_2014[cont_map_vect],raster=lista_classificada_patch_clump_mata_limpa_AreaHA[0], column="PTCH_2014")
        cont_map_vect=cont_map_vect+1
        
    del lista_classificada_patch_clump_mata_limpa_AreaHA[0]   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------------------    

"""
extraindo areas de conectividades funcional(DILA) conseiderando a distancia de 120 
"""
cont_map_vect=0 
while len(lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA)>0:
    if "2014" in lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA[0]:
        #print lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA[0],lista_vectors_2014[cont_map_vect]
        grass.run_command('g.region',rast=lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA[0])
        """
        120
        """
        grass.run_command('v.what.rast', vector=lista_vectors_2014[cont_map_vect],raster=lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA[0], column="DL120_2014")
        cont_map_vect=cont_map_vect+1
    del lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA[0]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
extraindo areas de conectividades funcional(DILA) conseiderando a distancia de 60
"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
cont_map_vect=0 
while len(lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA)>0:
    if "2014" in lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA[0]:
        #print lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA[0],lista_vectors_2014[cont_map_vect]
        grass.run_command('g.region',rast=lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA[0])
        """
        60
        """
        grass.run_command('v.what.rast', vector=lista_vectors_2014[cont_map_vect],raster=lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA[0], column="DL060_2014")
        cont_map_vect=cont_map_vect+1
    del lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA[0]
 #---------------------------------------------------------------------------------------------------------------------------------------------------------------       