st = input("Введите строку: ")
st1 = st.replace("о", "О")
i = st1.find("О")
st2 = st1.replace(st1[i], "о", 1)
j = st2.rfind("О")
# res = st2.replace(st2[j], "о", 1)
st2_list = list(st2)
st2_list[j] = "о"
res = "".join(st2_list)
print(res)

