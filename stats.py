import random

inp = input('roll for stats? (y/n)\n')
col, row = 4, 6
if inp == "y":
    raw_stats = [random.randint(1,6) for i in range(col) for j in range(row)]
    fin_stats = [sum(raw_stats(i)) - min(raw_stats(i)) for i in range(row) for j in range(row)]
    print(fin_stats(i) for i in range(row) for j in range(row))
else:
    print([15,14,13,12,10,8]) 
    
