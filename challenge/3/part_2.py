li = []
cote_oxy = []
epsilon_list = []
list_ = []

with open("dict.txt","r") as f:
    line = [line.rstrip() for line in f]
    a = line[-1]
    index = line.index(a)
    for i in range(index+1):
        li = [i for i in line[i]]
        list_.append(li)
    
# Gamma
index = 0
index_l = 0
for i in range(12):
    one_bits = 0
    zero_bits = 0
    for l in list_:
        if l[index] == "1":
            one_bits = one_bits + 1
        if l[index] == "0":
            zero_bits = zero_bits + 1
    for l in list_:
        if one_bits > zero_bits:
            if l[index] == '0':
                list_.pop(index_l)
        if zero_bits > one_bits:
            if l[index] == '1':
                list_.pop(index_l)

        if one_bits == zero_bits:
            if l[index] == "0":
                list_.pop(index_l)
        index_l = index_l + 1
    index = index + 1
print(index_l)




gamma_decimal = int(''.join(cote_oxy),2)
print(''.join(cote_oxy))