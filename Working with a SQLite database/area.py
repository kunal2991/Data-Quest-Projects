import sqlite3
conn = sqlite3.connect('factbook.db')
cursor = conn.cursor()
query = 'select sum(area_land) from facts where area_land != "";'
area_land_sum = cursor.execute(query).fetchone()
total_area_land = area_land_sum[0]
query = 'select sum(area_water) from facts where area_land != "";'
area_water_sum = cursor.execute(query).fetchone()
total_area_water = area_water_sum[0]
print(total_area_land/total_area_water)