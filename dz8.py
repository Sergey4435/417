seller = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4812, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5828, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
}
for i in seller:
    print(i)
    for j in seller[i]:
        print(j, ": ", seller[i][j])
name = input("Имя: ")
region = input("Регион: ")
print(seller[name][region])
seller[name][region] = int(input("Новое значение: "))
print(seller[name])
