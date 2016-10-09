import sqlite3
import pandas
import math

conn = sqlite3.connect('factbook.db')

facts = pandas.read_sql_query('select * from facts;',conn)
facts.dropna(axis = 0, inplace=True)

def growth_pop(df):
    final_pop = df['population'] * ((math.e)**((df['population_growth']/100)*35))
    return final_pop

#test_frame = facts[['population','population_growth']]
projected_pop = facts.apply(growth_pop, axis=1)
#print(projected_pop)
facts['projected_pop'] = projected_pop
facts.sort_values('projected_pop',inplace=True,ascending=False)
print(facts[0:10])