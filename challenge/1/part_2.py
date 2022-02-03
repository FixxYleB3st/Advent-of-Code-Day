list_ = []

def get_index():
    a = list_[-1]
    return list_.index(a)

with open("dict.txt","r") as f:
    line = [line.rstrip() for line in f]

for i in line:
    list_.append(int(i))

index = 0
val_list = []
for l in list_:
    nb_list = []
    index_ef = 0 + index
    if index + 2 > get_index():
        break
    else:
        for i in range(2):
            index_ef = index_ef + 1
            nb_list.append(list_[index_ef])

        calc = nb_list[0] + nb_list[1] + l
        val_list.append(calc)
        index = index + 1

counter = 0
index = 0
for l in val_list:
    if l > val_list[index-1] and index > 0:
        counter = counter + 1
    index = index + 1

print(counter)