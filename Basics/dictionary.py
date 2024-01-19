dic = {'zaz' : 96, 
       12 : 100,
        'bro' : 12}

print(dic["zaz"])
print(dic[12])

# if same key is already present, value gets updated, as in set


# we can access keys and value by:
# dic.keys()
# dic.values()
# dic.items() for keys and values

#### DICTIONARY METHODS

# update()
fir = {"name" : "zaz", "roll" : 18}
sec = {"nam" : " bro"}

fir.update(sec)

print(fir)

#clear()
sec.clear()
print(sec)

#pop()
fir.pop("name")  # removes item as we ask
print(fir)

#popitem
fir.popitem()  # removes last item
print(fir)

# del
del dic # delete all dictionary
# print(dic)