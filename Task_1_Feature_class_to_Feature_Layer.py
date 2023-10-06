import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_4_Working_with_Selections\ProProject_Selections\ProProject_Selections.gdb"
crime_fc_name = "Wilson_Crimes96"

crime_fc_path = os.path.join(gdb_path, crime_fc_name)
arcpy.management.MakeFeatureLayer(crime_fc_path, "crime_layer")

feature_count = arcpy.GetCount_management("crime_layer")
print(" Count of the crime is ",feature_count)