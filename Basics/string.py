name  = "zacBRO"
print(name[0])
print(name[-1])

print(name[1 : 3])
print(name[1 : ])

print(name[ : : -1])  # back printing

print(name[ -1 : 0 : -1]) # z will not print


a = "abcd"
for letter in a:
    print(letter * 2)

# strings are immutable
    
password = "xyz"
print(password.isalpha())

password = "xyz23"
print(password.isalpha())