import read
import collections
df = read.load_data()
total_headline = " "
for row in df['headline']:
    total_headline += str(row)
#print(total_headline)
split_words = total_headline.split(' ')
#print(split_words)
for item in split_words:
    item = item.lower()
count_words = collections.Counter(split_words)
print(count_words.most_common(100))