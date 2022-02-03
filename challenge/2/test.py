
def get_index(_list,item):
    return _list.index(item)

list_ = {}
list_["instruction"] = []
list_["number"] = []

with open("dict.txt","r") as f:
    line = [line.rstrip() for line in f]

for l in line:
    a = l.split(" ")
    list_["instruction"].append(a[0])
    list_["number"].append(int(a[1]))

breakpoint()

pos_horizontal = 0
profondeur = 0
index = 0
for l in list_["instruction"]:
    index = get_index(list_["instruction"],l) 
    nb = list_["number"][index]
    if l == "forward":
        forward_counter = forward_counter + 1
        pos_horizontal = pos_horizontal + nb

print(pos_horizontal)