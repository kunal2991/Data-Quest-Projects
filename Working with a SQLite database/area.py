import sqlite3
conn = sqlite3.connect('factbook.db')

cursor = conn.cursor()
query = 'SELECT SUM(area_land) FROM facts WHERE area_land != "";'
cursor.execute(query)
total_area_land = cursor.fetchall()[0][0]
#print(total_area_land)

query = 'SELECT SUM(area_water) FROM facts WHERE area_water != "";'
cursor.execute(query)
total_area_water = cursor.fetchall()[0][0]

print(total_area_land / total_area_water)