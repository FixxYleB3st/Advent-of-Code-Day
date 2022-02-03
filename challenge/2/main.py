
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

pos_horizontal = 0
profondeur = 0
index = 0
for l in list_["instruction"]:
    nb = list_["number"][index]
    if l == "forward":
        pos_horizontal = pos_horizontal + nb
    if l == "up":
        profondeur = profondeur - nb
    if l == "down":
        profondeur = profondeur + nb
    index += 1
calc = pos_horizontal*profondeur
print("Profondeur: "+str(profondeur))
print("Position Horizontal: "+str(pos_horizontal))
print("Résultat Final: "+str(calc))