a = input('Type smth:\n')
b = ""
i = 0
for x in a:
    if a[i].isupper() == True:
        b += a[i].lower()
    elif a[i].islower() == True:
        b += a[i].upper()
    i = i + 1
a = b
print (a)