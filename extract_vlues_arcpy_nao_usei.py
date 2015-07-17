import arcpy

from arcpy import env
from arcpy.sa import *
import os
arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace=r'E:\data_2015\___john\001.Thalita_p2\__Resultados_metricas_parte2\Conectividades'
List_Rt=arcpy.ListRasters()

dir_conect=r'E:\data_2015\___john\001.Thalita_p2\__Resultados_metricas_parte2\Conectividades/'


arcpy.env.workspace=r'E:\data_2015\___john\001.Thalita_p2\centroid_FINAL\split_2014'


list_shp_2014=arcpy.ListFeatureClasses()
dir_split_2014=r'E:\data_2015\___john\001.Thalita_p2\centroid_FINAL\split_2014/'

arcpy.env.workspace=r'E:\data_2015\___john\001.Thalita_p2\__Resultados_metricas_parte2\tables_2014'
cont=0
os.chdir(r'E:\data_2015\___john\001.Thalita_p2\__Resultados_metricas_parte2\tables_2014')
dir_out_table=r'E:\data_2015\___john\001.Thalita_p2\__Resultados_metricas_parte2\tables_2014/'
arcpy.CheckOutExtension("Spatial")



for i in List_Rt:
    if "2014" in i:
        if cont<=29 and "dila_60m" in i:
            format='00'+`cont`
            format=format[-2:]
            if format in i:
                out_table=i.replace('.tif','.txt')
                print list_shp_2014[cont],"*",i
                arcpy.ExtractValuesToTable_ga(dir_split_2014+list_shp_2014[cont],dir_conect+i,dir_out_table+out_table)
                cont=cont+1    
        if cont==30:
            cont=0  
        
   
    
