import csv
import re

# with open('secondtry.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in spamreader:
#         print(row)



# f = open('data3.csv','r')
# f2 = open('data5.csv','r')
# r = f.readlines()
# r2 = f2.readlines()
#
# r = list(r[i].split(',') for i in range(len(r)))
# r2 = list(r2[i].split(',') for i in range(len(r2)))
# # print(r2)
# r = [x for x in r if len(x) == 6]
# r2 = [x for x in r2 if len(x) == 6]
# for place in r:
#     place[0] = float(place[0])
#     place[1] = float(place[1])
#     place[2] = place[2].replace('\"','')
#     place[3] = float(place[3])
#     place[4] = place[4].replace('\"','')
#     place[5] = place[5].replace('\"','').replace('\n','')
#
# for place in r2:
#     place[0] = float(place[0])
#     place[1] = float(place[1])
#     place[2] = place[2].replace('\"','')
#     place[3] = float(place[3])
#     place[4] = place[4].replace('\"','')
#     place[5] = place[5].replace('\"','').replace('\n','')
# # print(place)
# r_set = set(map(tuple,r))
# r2_set = set(map(tuple,r2))
# total = list(r_set.union(r2_set))
# print(total)
# fp = open('datafinal.csv','w',newline='')
# writer = csv.writer(fp)
# writer.writerows(total)
