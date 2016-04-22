import read
from dateutil.parser import *
from datetime import *
df = read.load_data()
#print(df['submission_time'])
#now = parse(df['submission_time'])
#print(now.hour)
now = []
for row in df['submission_time']:
    temp = parse(row)
    now.append(temp)
    #print(now.hour)
dictionary_hours = {}
for row in now:
    if row not in dictionary_hours:
        dictionary_hours[row] = 1
    else:
        dictionary_hours[row] = dictionary_hours[row] + 1
print(dictionary_hours)
#if __name__ == "__main__":
#   df = read.load_data()
#    extract_hour(df)