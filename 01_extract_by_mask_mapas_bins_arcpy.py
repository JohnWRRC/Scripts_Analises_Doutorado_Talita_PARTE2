import arcpy
from arcpy import env
import os


buffer_2014="buffer_vazio_outros"

""
env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extrract_buffers_bin"
List_Rt=arcpy.ListRasters()

lista2014=[]
for i in List_Rt:
    if "1992" in i:
        lista2014.append(i)
        
    

cont_lista_raster=0
env.workspace = r"E:\data_2015\___john\001.Thalita_p2\Mapeamento_revisado_2015_05_d19\rasters\extrract_buffers_bin_extract"
with arcpy.da.SearchCursor(buffer_2014, "id") as idtf:
    for idt in idtf:        
        query="id=%d"%idt
        
        
        arcpy.SelectLayerByAttribute_management(buffer_2014,"NEW_SELECTION",query)
        
        outputName_extract=lista2014[0].replace("reclassify.tif","bin.tif")
        print outputName_extract,"  ",query
        arcpy.gp.ExtractByMask_sa(lista2014[0], buffer_2014, outputName_extract)
        del lista2014[0]
        
    








