import sqlite3
import pandas as pd
import math
conn = sqlite3.connect('factbook.db')
cursor = conn.cursor()
query = 'select * from facts;'
#test = cursor.execute(query).fetchall()
#print(test)
facts_df = pd.read_sql_query(query,conn)
facts_df.dropna(axis=0)
print(facts_df.columns)
facts_df = facts_df[facts_df['area_land'] > 0]
#final_estimate = []
initial_pop = facts_df['population']
growth_rate = facts_df['population_growth']
change = (initial_pop * (math.e**((growth_rate/100)*35)))
#final_estimate.append(change)
facts_df['Pop_Estimate_2050'] = change
    
#facts_df.apply(pop_estimate())
facts_df.sort('Pop_Estimate_2050',ascending=False, inplace=True)
print(facts_df.head(10))