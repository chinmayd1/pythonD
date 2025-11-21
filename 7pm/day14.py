info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "city":"pune"
}

a = info.get("firstName")
b = info.get("lastName")
print(a)
print(b)


info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "city":"pune"
}
info.clear()
print(info)

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "city":"pune"
}

info.popitem()
info.pop('age')
print(info)


info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "city":"pune"
}
info.update({"language":"marathi"})
print(info)


info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "city":"pune"
}

print(info.values())
print(info.keys())
print(info.items())

for k in info.keys():
    print(k)

for v in info.values():
    print(v)

for k,v in info.items():
    print(k,v)
    
    
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "city":"pune"
}

w = info.setdefault("city","nagpur")
print(w)

wa = info.setdefault("language","marathi")
print(wa)
print(info)


info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "city":"pune"
}

dictA = dict.fromkeys(['key1','key2','key3'])
print(dictA)

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "city":"pune"
}

info33 = info.copy()
print(info33)
info33['city'] = "nagpur"
print(info33)

