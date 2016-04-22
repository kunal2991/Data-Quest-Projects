import read
df = read.load_data()
domain_count = df['url'].value_counts()
print(domain_count[0:100])