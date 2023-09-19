import random

#rand testing
#num = random.randrange(1,6)
#print(num)


col, row = 4, 6
#makes stats for one block
#raw_stat = [random.randrange(1,6) for i in range(col)]
#all stats all rolls
raw_stats = [[random.randrange(1,6) for i in range(col)] for j in range(row)]
print(raw_stats)
#all stats fin stats

fin_stats = [(sum(raw_stats[i])-min(raw_stats[i])) for i in range(row)]
print(fin_stats)

