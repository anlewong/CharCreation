import random

inp = input('roll for stats? (y/n)\n')
col, row = 4, 6
if inp == "y":
    raw_stats = [[random.randrange(1,6) for i in range(col)] for j in range(row)]
    fin_stats = [(sum(raw_stats[i])-min(raw_stats[i])) for i in range(row)]
    if "n" == input("see rolls? (y/n)"):
        print(fin_stats)
    else:
        for i in range(row):
            stats = raw_stats[i]
            print("Stat Value: " + str(fin_stats[i]) + "\nrolls " + str(stats) + " removed lowest roll " + str(min(stats)) + "\n")  

else:
    print([15,14,13,12,10,8]) 