n = int(input("Количество кустов"))
list_1 = []
for i in range(n):
    list_1.append(int(input("Количество ягод")))
print(list_1)
list_2 = []
for i in range(len(list_1)):
    list_2.append(list_1[i-2]+list_1[i-1]+list_1[i])
print(max(list_2))