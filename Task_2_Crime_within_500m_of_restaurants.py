import arcpy
import os
gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_4_Working_with_Selections\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
crime_fc_name = "Wilson_Crimes96"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
crime_fc_path = os.path.join(gdb_path, crime_fc_name)

# Converting a feature class to feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_layer")
arcpy.management.MakeFeatureLayer(crime_fc_path, "crime_layer")


arcpy.management.SelectLayerByLocation("crime_layer","WITHIN_A_DISTANCE", "restaurant_layer", "500 meters")
count = arcpy.GetCount_management("crime_layer")
print("Crimes committed within a distance of 500 meters from restaurants is" ,count)

print("Process Completed")