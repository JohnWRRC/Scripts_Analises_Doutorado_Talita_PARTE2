import arcpy
from arcpy import env

arcpy.env.workspace=r"E:\data_2015\___john\001.Thalita_p2\centroid_FINAL\split_2014"
fc=arcpy.ListFeatureClasses()

for i in fc:
    inp=i.replace('.shp',"")
    arcpy.AddField_management(inp, 'FG120_2014', "DOUBLE", 20, 20)
    arcpy.AddField_management(inp, 'FG060_2014', "DOUBLE", 20, 20)
    arcpy.AddField_management(inp, 'PTCH_2014', "DOUBLE", 20, 20)
    arcpy.AddField_management(inp, 'DL060_2014', "DOUBLE", 20, 20)
    arcpy.AddField_management(inp, 'DL120_2014', "DOUBLE", 20, 20)
    



import arcpy
from arcpy import env

arcpy.env.workspace=r"E:\data_2015\___john\001.Thalita_p2\centroid_FINAL\split_outros"
fc=arcpy.ListFeatureClasses()



lista_anos=[1984,1988,1992,1996,2000,2003,2005,2009]
for i in fc:
    for a in lista_anos:
        inp=i.replace('.shp',"")
        arcpy.AddField_management(inp, 'FG120_'+`a`, "DOUBLE", 20, 20)
        arcpy.AddField_management(inp, 'FG060_'+`a`, "DOUBLE", 20, 20)
        arcpy.AddField_management(inp, 'PTCH_'+`a`, "DOUBLE", 20, 20)
        arcpy.AddField_management(inp, 'DL060_'+`a`, "DOUBLE", 20, 20)
        arcpy.AddField_management(inp, 'DL120_'+`a`, "DOUBLE", 20, 20)
        