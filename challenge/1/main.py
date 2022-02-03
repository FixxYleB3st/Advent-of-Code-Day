list_ = []

with open("dict.txt","r") as f:
    line = [line.rstrip() for line in f]

for i in line:
    list_.append(int(i))

counter = 0
index = 0
for l in list_:
    if l > list_[index-1] and index > 0:
        counter = counter + 1
    index = index + 1
    
print(counter)