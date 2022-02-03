a = [1,2,3,4,5,6]

index = 0
val_list = []
for l in a:
    nb_list = []
    index_ef = 0 + index
    if index + 2 > 5:
        break
    else:
        for i in range(2):
            index_ef = index_ef + 1
            print(index_ef)
            nb_list.append(a[index_ef])

        calc = nb_list[0] + nb_list[1] + l
        val_list.append(calc)
        index = index + 1
