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
lista_vectors_outrostemp=grass.mlist_grouped ('vect', pattern='**') ['PERMANENT']
lista_vectors_outros=[]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
limpando a lista de vetores para eliminar os mapas de 2014
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

for i in lista_vectors_outrostemp:
    if not "2014" in i:
        lista_vectors_outros.append(i)
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------












"""
extraindo valores para os mapas de areas fragmentadas com 120 metros de erosao

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

lista_col_Fg120=["FG120_1984","FG120_1988","FG120_1992","FG120_1996","FG120_2000","FG120_2003","FG120_2005","FG120_2009"]
cont_map_vect=0
cont_cols=0
while len(lista_classificada_FRAG120m_mata_clump_AreaHA)>0:
    if not "2014" in lista_classificada_FRAG120m_mata_clump_AreaHA[0]:
        
        #print lista_classificada_FRAG120m_mata_clump_AreaHA[0],lista_vectors_outros[cont_map_vect],"***",lista_col_Fg120[cont_cols]
        grass.run_command('g.region',rast=lista_classificada_FRAG120m_mata_clump_AreaHA[0])
        """
        120
        """
        grass.run_command('v.what.rast', vector=lista_vectors_outros[cont_map_vect],raster=lista_classificada_FRAG120m_mata_clump_AreaHA[0], column=lista_col_Fg120[cont_cols])
        
        """
        controlando o contador de anos de colunas
        """
    
        """
        controlando o contador de mapas de vetor para seguir os raters par a par
        """        
        if cont_map_vect==29:
            cont_cols=cont_cols+1
            cont_map_vect=0
            
        else:
            cont_map_vect=cont_map_vect+1
            
    del lista_classificada_FRAG120m_mata_clump_AreaHA[0]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------












"""
extraindo valores para os mapas de areas fragmentadas com 60 metros de erosao

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

lista_col_Fg120=["FG060_1984","FG060_1988","FG060_1992","FG060_1996","FG060_2000","FG060_2003","FG060_2005","FG060_2009"]
cont_map_vect=0
cont_cols=0
while len(lista_classificada_FRAG60m_mata_clump_AreaHA)>0:
    if not "2014" in lista_classificada_FRAG60m_mata_clump_AreaHA[0]:
        
        #print lista_classificada_FRAG60m_mata_clump_AreaHA[0],lista_vectors_outros[cont_map_vect],"***",lista_col_Fg120[cont_cols]
        grass.run_command('g.region',rast=lista_classificada_FRAG60m_mata_clump_AreaHA[0])
        """
        120
        """
        grass.run_command('v.what.rast', vector=lista_vectors_outros[cont_map_vect],raster=lista_classificada_FRAG60m_mata_clump_AreaHA[0], column=lista_col_Fg120[cont_cols])
        
        """
        controlando o contador de anos de colunas
        """
    
        """
        controlando o contador de mapas de vetor para seguir os raters par a par
        """        
        if cont_map_vect==29:
            cont_cols=cont_cols+1
            cont_map_vect=0
            
        else:
            cont_map_vect=cont_map_vect+1
            
    del lista_classificada_FRAG60m_mata_clump_AreaHA[0]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------








"""
extraindo valores para os mapas de areas reais dos fragmentos sem alteracao

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

lista_col_Fg120=["PTCH_1984","PTCH_1988","PTCH_1992","PTCH_1996","PTCH_2000","PTCH_2003","PTCH_2005","PTCH_2009"]
cont_map_vect=0
cont_cols=0
while len(lista_classificada_patch_clump_mata_limpa_AreaHA)>0:
    if not "2014" in lista_classificada_patch_clump_mata_limpa_AreaHA[0]:
        
        #print lista_classificada_patch_clump_mata_limpa_AreaHA[0],lista_vectors_outros[cont_map_vect],"***",lista_col_Fg120[cont_cols]
        grass.run_command('g.region',rast=lista_classificada_patch_clump_mata_limpa_AreaHA[0])
        """
        120
        """
        grass.run_command('v.what.rast', vector=lista_vectors_outros[cont_map_vect],raster=lista_classificada_patch_clump_mata_limpa_AreaHA[0], column=lista_col_Fg120[cont_cols])
        
        """
        controlando o contador de anos de colunas
        """
    
        """
        controlando o contador de mapas de vetor para seguir os raters par a par
        """        
        if cont_map_vect==29:
            cont_cols=cont_cols+1
            cont_map_vect=0
            
        else:
            cont_map_vect=cont_map_vect+1
            
    del lista_classificada_patch_clump_mata_limpa_AreaHA[0]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
    













"""
extraindo areas de conectividades funcional(DILA) conseiderando a distancia de 120
"""  
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

lista_col_Fg120=["DL120_1984","DL120_1988","DL120_1992","DL120_1996","DL120_2000","DL120_2003","DL120_2005","DL120_2009"]
cont_map_vect=0
cont_cols=0
while len(lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA)>0:
    if not "2014" in lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA[0]:
        
        #print lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA[0],lista_vectors_outros[cont_map_vect],"***",lista_col_Fg120[cont_cols]
        grass.run_command('g.region',rast=lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA[0])
        """
        120
        """
        grass.run_command('v.what.rast', vector=lista_vectors_outros[cont_map_vect],raster=lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA[0], column=lista_col_Fg120[cont_cols])
        
        """
        controlando o contador de anos de colunas
        """
    
        """
        controlando o contador de mapas de vetor para seguir os raters par a par
        """        
        if cont_map_vect==29:
            cont_cols=cont_cols+1
            cont_map_vect=0
            
        else:
            cont_map_vect=cont_map_vect+1
            
    del lista_classificada_dila_120m_orig_clump_mata_limpa_AreaHA[0]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
        












"""
extraindo areas de conectividades funcional(DILA) conseiderando a distancia de 60
"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
lista_col_Fg120=["DL060_1984","DL060_1988","DL060_1992","DL060_1996","DL060_2000","DL060_2003","DL060_2005","DL060_2009"]
cont_map_vect=0
cont_cols=0
while len(lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA)>0:
    if not "2014" in lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA[0]:
        
        #print lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA[0],lista_vectors_outros[cont_map_vect],"***",lista_col_Fg120[cont_cols]
        grass.run_command('g.region',rast=lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA[0])
        """
        120
        """
        grass.run_command('v.what.rast', vector=lista_vectors_outros[cont_map_vect],raster=lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA[0], column=lista_col_Fg120[cont_cols])
        
        """
        controlando o contador de anos de colunas
        """
    
        """
        controlando o contador de mapas de vetor para seguir os raters par a par
        """        
        if cont_map_vect==29:
            cont_cols=cont_cols+1
            cont_map_vect=0
            
        else:
            cont_map_vect=cont_map_vect+1
            
    del lista_classificada_dila_60m_orig_clump_mata_limpa_AreaHA[0]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------