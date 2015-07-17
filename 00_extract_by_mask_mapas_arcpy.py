import arcpy
from arcpy import env
import os




# Process: Convert to ascii 2014
mapa_2014_classificada="classificada_2014_18052015_utm_final_rast.tif"
buffer_2014="buffer_vazio_2014"

env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extracts_buffers"
with arcpy.da.SearchCursor(buffer_2014, "id") as idtf:
    for idt in idtf:        
        query="id=%d"%idt
        print query
        idts2=int(idt[0])
        formato='0000'+`idts2`
        formato=formato[-2:]
        out_buffer="classificada_2014_id"+formato+".tif"
        arcpy.SelectLayerByAttribute_management(buffer_2014,"NEW_SELECTION",query)
        arcpy.gp.ExtractByMask_sa(mapa_2014_classificada, buffer_2014, out_buffer)
        arcpy.SelectLayerByAttribute_management(buffer_2014, "CLEAR_SELECTION")











# Process: Convert to ascii 2003
mapa_2003_classificada="classificada_20030813_18052015_v1_final_rast.tif"
buffer_outros="buffer_vazio_outros"

env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extracts_buffers"
with arcpy.da.SearchCursor(buffer_outros, "id") as idtf:
    for idt in idtf:        
        query="id=%d"%idt
        print query
        idts2=int(idt[0])
        formato='0000'+`idts2`
        formato=formato[-2:]
        out_buffer="classificada_2003_id"+formato+".tif"
        arcpy.SelectLayerByAttribute_management(buffer_outros,"NEW_SELECTION",query)
        arcpy.gp.ExtractByMask_sa(mapa_2003_classificada, buffer_outros, out_buffer)
        arcpy.SelectLayerByAttribute_management(buffer_outros, "CLEAR_SELECTION")
    




        
# Process: Convert to ascii 2000
mapa_2000_classificada="classificada_20000905_18052015_utm_final_rast.tif"
buffer_outros="buffer_vazio_outros"

env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extracts_buffers"
with arcpy.da.SearchCursor(buffer_outros, "id") as idtf:
    for idt in idtf:        
        query="id=%d"%idt
        print query
        idts2=int(idt[0])
        formato='0000'+`idts2`
        formato=formato[-2:]
        out_buffer="classificada_2000_id"+formato+".tif"
        arcpy.SelectLayerByAttribute_management(buffer_outros,"NEW_SELECTION",query)
        arcpy.gp.ExtractByMask_sa(mapa_2000_classificada, buffer_outros, out_buffer)
        arcpy.SelectLayerByAttribute_management(buffer_outros, "CLEAR_SELECTION")

#

###########
# Process: Convert to ascii 1996
    
mapa_2000_classificada="classificada_19960724_18052015_utm_final_rast.tif"
buffer_outros="buffer_vazio_outros"

env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extracts_buffers"
with arcpy.da.SearchCursor(buffer_outros, "id") as idtf:
    for idt in idtf:        
        query="id=%d"%idt
        print query
        idts2=int(idt[0])
        formato='0000'+`idts2`
        formato=formato[-2:]
        out_buffer="classificada_1996_id"+formato+".tif"
        arcpy.SelectLayerByAttribute_management(buffer_outros,"NEW_SELECTION",query)
        arcpy.gp.ExtractByMask_sa(mapa_2000_classificada, buffer_outros, out_buffer)
        arcpy.SelectLayerByAttribute_management(buffer_outros, "CLEAR_SELECTION")


###########
# Process: Convert to ascii 1992

mapa_2000_classificada="classificada_19920713_18052015_utm_final_rast.tif"
buffer_outros="buffer_vazio_outros"

env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extracts_buffers"
with arcpy.da.SearchCursor(buffer_outros, "id") as idtf:
    for idt in idtf:        
        query="id=%d"%idt
        print query
        idts2=int(idt[0])
        formato='0000'+`idts2`
        formato=formato[-2:]
        out_buffer="classificada_1992_id"+formato+".tif"
        arcpy.SelectLayerByAttribute_management(buffer_outros,"NEW_SELECTION",query)
        arcpy.gp.ExtractByMask_sa(mapa_2000_classificada, buffer_outros, out_buffer)
        arcpy.SelectLayerByAttribute_management(buffer_outros, "CLEAR_SELECTION")

#
# Process: Convert to ascii 1988
    
mapa_2000_classificada="classificada_19880904_18052015_utm_final_rast.tif"
buffer_outros="buffer_vazio_outros"

env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extracts_buffers"
with arcpy.da.SearchCursor(buffer_outros, "id") as idtf:
    for idt in idtf:        
        query="id=%d"%idt
        print query
        idts2=int(idt[0])
        formato='0000'+`idts2`
        formato=formato[-2:]
        out_buffer="classificada_1988_id"+formato+".tif"
        arcpy.SelectLayerByAttribute_management(buffer_outros,"NEW_SELECTION",query)
        arcpy.gp.ExtractByMask_sa(mapa_2000_classificada, buffer_outros, out_buffer)
        arcpy.SelectLayerByAttribute_management(buffer_outros, "CLEAR_SELECTION")
        
        
        
        
        
# Process: Convert to ascii 1984
mapa_2000_classificada="classificada_19840621_18052015_utm_final_rast.tif"
buffer_outros="buffer_vazio_outros"

env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extracts_buffers"
with arcpy.da.SearchCursor(buffer_outros, "id") as idtf:
    for idt in idtf:        
        query="id=%d"%idt
        print query
        idts2=int(idt[0])
        formato='0000'+`idts2`
        formato=formato[-2:]
        out_buffer="classificada_1984_id"+formato+".tif"
        arcpy.SelectLayerByAttribute_management(buffer_outros,"NEW_SELECTION",query)
        arcpy.gp.ExtractByMask_sa(mapa_2000_classificada, buffer_outros, out_buffer)
        arcpy.SelectLayerByAttribute_management(buffer_outros, "CLEAR_SELECTION")
        


# Process: Convert to ascii 2005
mapa_2000_classificada="classificada_20050802_18052015_utm_final_rast.tif"
buffer_outros="buffer_vazio_outros"

env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extracts_buffers"
with arcpy.da.SearchCursor(buffer_outros, "id") as idtf:
    for idt in idtf:        
        query="id=%d"%idt
        print query
        idts2=int(idt[0])
        formato='0000'+`idts2`
        formato=formato[-2:]
        out_buffer="classificada_2005_id"+formato+".tif"
        arcpy.SelectLayerByAttribute_management(buffer_outros,"NEW_SELECTION",query)
        arcpy.gp.ExtractByMask_sa(mapa_2000_classificada, buffer_outros, out_buffer)
        arcpy.SelectLayerByAttribute_management(buffer_outros, "CLEAR_SELECTION")
        
        
#    

# Process: Convert to ascii 2009
mapa_2000_classificada="classificada_20090728_18052015_utm_final_rast.tif"
buffer_outros="buffer_vazio_outros"

env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extracts_buffers"
with arcpy.da.SearchCursor(buffer_outros, "id") as idtf:
    for idt in idtf:        
        query="id=%d"%idt
        print query
        idts2=int(idt[0])
        formato='0000'+`idts2`
        formato=formato[-2:]
        out_buffer="classificada_2009_id"+formato+".tif"
        arcpy.SelectLayerByAttribute_management(buffer_outros,"NEW_SELECTION",query)
        arcpy.gp.ExtractByMask_sa(mapa_2000_classificada, buffer_outros, out_buffer)
        arcpy.SelectLayerByAttribute_management(buffer_outros, "CLEAR_SELECTION")

rasterList = arcpy.ListRasters()