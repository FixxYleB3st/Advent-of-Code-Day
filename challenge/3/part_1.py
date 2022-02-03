from typing import get_args


list_ = []
li = []
gamma_list = []
epsilon_list = []

with open("dict.txt","r") as f:
    line = [line.rstrip() for line in f]

# Gamma
for i in range(12):
    one_bits = 0
    zero_bits = 0
    for l in line:
        li = [i for i in l]
        if li[i] == "1":
            one_bits = one_bits + 1
        if li[i] == "0":
            zero_bits = zero_bits + 1
    if one_bits > zero_bits:
        gamma_list.append("1")
    else:
        gamma_list.append("0")
gamma_decimal = int(''.join(gamma_list),2)

# Epilson
for i in range(12):
    one_bits = 0
    zero_bits = 0
    for l in line:
        li = [i for i in l]
        if li[i] == "1":
            one_bits = one_bits + 1
        if li[i] == "0":
            zero_bits = zero_bits + 1
    if one_bits < zero_bits:
        epsilon_list.append("1")
    else:
        epsilon_list.append("0")
epsilon_decimal = int(''.join(epsilon_list),2)

print(gamma_decimal)
print(epsilon_decimal)
print(gamma_decimal*epsilon_decimal)