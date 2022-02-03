l = []
with open("dict.txt","r") as f:
    line = [line.rstrip() for line in f]
    a = line[-1]
    index = line.index(a)
    for i in range(index):
        li = [i for i in line[i]]
        l.append(li)
