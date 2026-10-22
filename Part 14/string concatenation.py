# String Concatenation...

l = ["Aswin", "Appu", "Mallu", "PY"]
st = ""

for i in l:
    st = st + i + '_'

st = st[:-1]
print(st)

a = "_".join(l)
print(a)